#BL Programming

#Modules
from openai import OpenAI
from pytube import YouTube
from pytubefix import YouTube #error-fixes for pytube
import whisper
import openai

#Your API key entered here
client = OpenAI(api_key="here")


#Retrieves user-input and creates an object of their URL.
#The audio portion of that object is then downloaded locally
#Returns the 'youtube' object
def userInputConvertedToAudioFile() -> YouTube:
    youtubeURL = input("Enter the URL of your Youtube video: ")

    #blank input, exit program
    if youtubeURL == "":
        return None
    
    else:
        obj = YouTube(youtubeURL)
    
    streamOfInterest = obj.streams.filter(only_audio=True).first()

    #local download onto your machine
    audioFile = streamOfInterest.download(filename="audioFile.mp4")

    return obj 


#The local audio file is transcribed via OpenAI's whisper 
#(their open source speech recognition system)
#Returns the transcription (list)
def transcribingAudioFile():
    model = whisper.load_model("turbo")
    result = model.transcribe("audioFile.mp4", fp16=False)
    
    #print(result["text"])

    #file writing
    with open("originalTranscription.txt", "w") as og:
        og.write(result["text"])
    
    return result


#Arg: Takes in a list of strings (presumably, the transcription of the audio file)
#Returns: The chatGPT api response (the summary of the transcription)
def summarizeTranscription(obj: YouTube, transcribedText: list):
    chatGPTResponse = client.chat.completions.create(

        #Feel free to adjust the following settings to match your preferences
        model = "gpt-4o",

        #Some examples:
        #You are an assistant that summarizes information based off of chunks of text transcribed from an audio file
        #You are an assistant that identifies the song based off texts of the lyrics
        messages = [
            {f"role" : "system", "content": "You are an assistant that summarizes information based off of chunks of text transcribed from an audio file. To set the context, the title of the video is" + obj.title},
            {f"role": "user", "content": transcribedText}
        ]
    )

    #file writing
    with open("summarizedTranscription.txt", "w") as sum:
        sum.write(chatGPTResponse.choices[0].message.content)

    #output
    print("Summary: ")
    print(chatGPTResponse.choices[0].message.content)
    print("\n\n")

    
def main():
    urlObj = userInputConvertedToAudioFile()

    while urlObj != None:
        print(f"Title of Youtube Video: {urlObj.title}")
        transcription = transcribingAudioFile()
        transcription2 = transcription["text"]
        summarizeTranscription(urlObj, transcription2)

        #new video link
        urlObj = userInputConvertedToAudioFile()

    print("Goodbye.")


if __name__ == "__main__":
    main()