## Audio_Summarization
## BL Program

This Python program transcribes audio files from YouTube videos and outputs a summary using various API calls.


To get started, some modules have to be installed prior to its usage:
// pip install openai
// pip install pytube
// pip install pytubefix
// pip install openai-whisper # https://pypi.org/project/openai-whisper/ for the initial set-up
// You will also need to get an API key from OpenAI.


How it works (a simple summary): 
A user will input a URL to a YouTube video of their choice. Using the Pytube library, a local download of that video's audio file will occur. That audio file will then be transcribed using OpenAI's speech recognition model known as "whisper". After transcription, the OpenAI API is utilized to summarize that chunk of text, which is then outputted for the user to see. A .txt file of both the original transcription and its respective summary will also be locally downloaded.


Possible modification(s) one can make:
// The chat completion model can be adjusted to fit one's needs
  -the model itself
  -the content/context

// whisper's load model


Some test cases // *your outputs will obviously vary* // Examples:
---------------------------------------------------------------------------------------------------------------------------------------------------------------
#1
Input:
https://youtu.be/jiudBq7z8wk?si=aU58qAA6P5XTuGgM

Output:
Title of YouTube Video: Mark Zuckerberg Says He Is Not a Lizard Person | Inverse

Summary:
During a live Q&A session, Mark Zuckerberg addressed a humorous question regarding a theory that he is secretly a lizard. He responded by denying the claim, stating, "I am not a lizard," and encouraged more entertaining comments, highlighting that the session featured a lot of amusing moments.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
#2
Input: 
https://youtu.be/Cwkej79U3ek?si=cpP2f7j8vBZecBgH

Output: 
Title of YouTube Video: Vanessa Carlton - A Thousand Miles

Summary: 
The text is a lyrical exploration of longing and desire for someone who is no longer present. The narrator describes a journey, both physical and emotional, as they walk through a city and navigate their feelings of
missing and needing this person. They wonder if time would pass differently if they could see their loved one again and express a willingness to go great distances to reunite. The repetition of certain phrases 
underscores their deep yearning and emotional struggle.
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Known issue(s) at the moment:
// Depending on the video of your choice, the clarity of the audio may affect the ability of OpenAI-Whisper's transcriptions, negatively affecting the accuracy of the summarization process.

//Longer videos can take a bit of time to transcribe.







