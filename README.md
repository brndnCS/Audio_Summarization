# YouTube Summarizer (a Python application) <hr>
BL Program <hr>

Details: <br>
This Python program transcribes audio files from YouTube videos and outputs a summary of it, using various API calls and modules. <br> <hr>

How it works (a simple summary): <br>
A user will input a URL of a YouTube video of their choice. Using the Pytube library, a local download of that video's audio file will then occur. That audio file will then be transcribed using OpenAI's speech recognition model known as "whisper". After transcription, the OpenAI API will be utilized to summarize that chunk of text; that summary is then outputted for the user to see. Users may then discuss and interact with the GPT for additional details/information.<br><hr>

How to start (instructions): <br>
As of right now, Python 3.11 is the latest version of Python supported by OpenAI's whisper. <br>
This version of Python also happens to be supported by the other modules imported as well. <br>
Initially, some packages have to be installed prior to its usage (pip install) -> <br>
// pip install openai // https://pypi.org/project/openai/ <br>
// pip install pytube // https://pypi.org/project/pytube/ <br>
// pip install pytubefix // https://pypi.org/project/pytubefix/ <br>
// pip install openai-whisper // https://pypi.org/project/openai-whisper/ for the initial set-up <br>
// You will also need to purchase some credits from OpenAI in order to create an API key. // https://openai.com/api/ <br>
// Then download the 'main' folder, run 'main.py', and follow the given instructions within the console. <br><hr>

Possible modification(s) one can make: <br>
// The chat completion model can be adjusted to fit one's needs <br>
  -the model itself // https://platform.openai.com/docs/models<br>
  -the content/context <br>

// OpenAI's Whisper model details <br><hr>

Some personal test cases to demonstrate this project// *your outputs will obviously vary* <br><br>
Test Case #1 <br>

Input: <br>
https://youtu.be/jiudBq7z8wk?si=aU58qAA6P5XTuGgM (Mark Zuckerberg Says He Is Not a Lizard Person | Inverse)<br>

Output: <br>
Mark Zuckerberg humorously addressed a bizarre question during a live Q&A session where he was asked if he was secretly a lizard. He denied the allegations, encouraging participants to continue sending in high-quality and humorous comments to make the session entertaining.
<br>
The summary provides a concise overview of Zuckerberg's response to an unusual question in a live session, highlighting his light-hearted engagement with the audience. This approach aids in maintaining a relaxed and enjoyable interaction during public engagements.
<br>
Discuss -> You: <br>

Input: <br>
Who is this figure? <br>

Output: <br>
The figure mentioned in the summary is Mark Zuckerberg, the CEO of Meta Platforms, Inc., previously known as Facebook. He is well-known for his involvement in technology and social media. <br>

<br>
<hr>
<br>

Test Case #2 <br>
Input: <br>
https://youtu.be/Cwkej79U3ek?si=cpP2f7j8vBZecBgH (Vanessa Carlton - A Thousand Miles)<br>

Output: <br>
The text appears to be lyrics that describe a person's emotional journey as they walk through a city, reflecting on their longing and desire to be with someone they miss deeply. The central theme revolves around the idea of walking a thousand miles just to see this person, highlighting a strong feeling of attachment and yearning. The repetitive lines emphasize the longing and the hypothetical questions about falling into the sky and whether time would pass them by suggest a feeling of wanting to escape reality or change their circumstances dramatically to be with the person they miss. The concluding lines indicate a bittersweet farewell to these intense emotions. <br>

This analysis highlights the speaker's deep emotional investment and the lengths they would go to reconnect with someone important to them. The lyrics also portray a sense of urgency and a profound sense of loss, as reflected in the wishful thinking about altering time and space to reunite with a loved one. <br>

Discuss -> You: <br>

Input: <br>
What year did this song come out? <br>

Output: <br>
The song "A Thousand Miles" by Vanessa Carlton was released in the year 2002. 

<br>
<hr>
<br>

Known issue(s) at the moment: <br>
// Depending on the video of your choice, the clarity of the audio may affect the ability of OpenAI-Whisper's transcriptions, negatively affecting the accuracy of the summarization process. <br>
//Longer videos can take a bit of time to transcribe. <br><hr>

Future plans for this project: <br>
~<s>My goal for the near future is to implement interactability with the chat completion model after the output of the video's summary. This will allow users to ask questions, and discuss about information regarding the contents of the video.</s> <br><hr>




