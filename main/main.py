#BL Programming

#Modules
from openai import OpenAI
from pytube import YouTube
from pytubefix import YouTube #error-fixes for pytube
import whisper


#Your API key entered here
client = OpenAI(api_key="yourKeyHere")


#Retrieves user-input and creates an object of that URL.
#The audio portion of that object is downloaded locally
def userInputConvertedToAudioFile(youtubeURL):
    obj = YouTube(youtubeURL)
    streamOfInterest = obj.streams.filter(only_audio=True).first()

    #local download
    audioFile = streamOfInterest.download(filename="audioFile.mp4")


#The local audio file is transcribed via OpenAI's whisper 
#(their open source speech recognition system)
#Returns the transcription (a list)
def transcribingAudioFile():
    model = whisper.load_model("turbo")
    result = model.transcribe("audioFile.mp4", fp16=False)
    
    #print(result["text"])
    return result


#Args: A list of strings; this is the transcription of the YouTube video
#Void function; simply outputs a conversation between the user and the GPT model within the console interface
def summarizeV2(transcribedText: list):
    #Feel free to adjust the prompt here
    exitCondition = ['break', 'exit', 'leave', 'quit', 'terminate']
    messages = []
    messages.append({f"role" : "system", "content": "You are an advanced AI designed to summarize text accurately and concisely while retaining key details. Maintain the original meaning, avoid redundancy, and ensure readability. After stating the summary, you will discuss about it and respond to user inputs."})
    messages.append({f"role" : "user", "content" : transcribedText})

    
    while True:
        chatGPTResponse = client.chat.completions.create(
        #Feel free to adjust the following settings to match your preferences
        #Turbo was chosen because it's designed to be more faster and cost efficient (while still being similar in accuracy)
        model = "gpt-4-turbo",
        messages = messages
        )

        GPTreply = chatGPTResponse.choices[0].message.content
        messages.append({f"role" : "system", "content" : GPTreply})
        print("\nChatGPT:\n" + GPTreply)

        userReply = input("\nDiscuss -> You:\n")
        messages.append({"role" : "user", "content" : userReply})

        if userReply.lower() in exitCondition:
            break


#Main function of our console application
#Requests user input for a URL, and proceeds from there
def main():
    exitCondition = ['break', 'exit', 'leave', 'quit', 'terminate']
    while True:
        userInput = input("Input 'exit' to terminate the program; When you're talking to the GPT, input 'exit' to break.\n\nEnter the URL of your YouTube video: ")

        if userInput.lower() in exitCondition:
            break
        
        userInputConvertedToAudioFile(userInput)
        transcription = transcribingAudioFile()
        transcriptionText = transcription["text"]
        summarizeV2(transcriptionText)


if __name__ == "__main__":
    main()