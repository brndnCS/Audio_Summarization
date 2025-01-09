## Summarization of an Audio Transcription ##
## BL Program ##

Details: <br />
This Python program transcribes audio files from YouTube videos and outputs a summary of it, using various API calls and modules. <br /><br />


How it works (a simple summary): <br />
A user will input a URL to a YouTube video of their choice. Using the Pytube library, a local download of that video's audio file will occur. That audio file will then be transcribed using OpenAI's speech recognition model known as "whisper". After transcription, the OpenAI API is utilized to summarize that chunk of text, which is then outputted for the user to see. A .txt file of both the original transcription and its respective summary will also be locally downloaded. <br /><br />

How to start: <br />
To get started, some modules have to be installed prior to its usage -> <br />
// pip install openai // https://pypi.org/project/openai/ <br />
// pip install pytube // https://pypi.org/project/pytube/ <br />
// pip install pytubefix // https://pypi.org/project/pytubefix/ <br />
// pip install openai-whisper // https://pypi.org/project/openai-whisper/ for the initial set-up <br />
// You will also need to get an API key from OpenAI. <br /><br />


Possible modification(s) one can make: <br />
// The chat completion model can be adjusted to fit one's needs <br />
  -the model itself <br />
  -the content/context <br />

// whisper's model details <br /><br />


Some test cases to demonstrate // *your outputs will obviously vary* <br />
---------------------------------------------------------------------------------------------------------------------------------------------------------------
#1 <br />
Input: <br />
https://youtu.be/jiudBq7z8wk?si=aU58qAA6P5XTuGgM <br />

Output: <br />
Title of YouTube Video: Mark Zuckerberg Says He Is Not a Lizard Person | Inverse <br />

Summary: <br />
During a live Q&A session, Mark Zuckerberg addressed a humorous question regarding a theory that he is secretly a lizard. He responded by denying the claim, stating, "I am not a lizard," and encouraged more entertaining comments, highlighting that the session featured a lot of amusing moments. <br />
---------------------------------------------------------------------------------------------------------------------------------------------------------------
#2 <br />
Input: <br />
https://youtu.be/Cwkej79U3ek?si=cpP2f7j8vBZecBgH <br />

Output: <br />
Title of YouTube Video: Vanessa Carlton - A Thousand Miles <br />

Summary: <br />
The text is a lyrical exploration of longing and desire for someone who is no longer present. The narrator describes a journey, both physical and emotional, as they walk through a city and navigate their feelings of
missing and needing this person. They wonder if time would pass differently if they could see their loved one again and express a willingness to go great distances to reunite. The repetition of certain phrases 
underscores their deep yearning and emotional struggle. <br />
---------------------------------------------------------------------------------------------------------------------------------------------------------------

<br />
Known issue(s) at the moment: <br />
// Depending on the video of your choice, the clarity of the audio may affect the ability of OpenAI-Whisper's transcriptions, negatively affecting the accuracy of the summarization process. <br />

//Longer videos can take a bit of time to transcribe. <br />
