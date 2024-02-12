import assemblyai as aai
from api_secrets import API_KEY_ASSEMBLYAI

aai.settings.api_key = API_KEY_ASSEMBLYAI
tracscriber = aai.Transcriber()

audio = './Extras/Sample voice.wav'

tracscript = tracscriber.transcribe(audio)

# Printing the entire response object
# print(dir(tracscript))

if tracscript.error:
    print(tracscript.error)
else:
    # Print transcription text
    print(tracscript.text)
    print(tracscript.sentiment_analysis)
    print(tracscript.summary)