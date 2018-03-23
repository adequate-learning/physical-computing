# import subprocess
# pip install pydub gtts
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

audio_file = "hello.mp3"
tts = gTTS(text="Hello World!", lang="en")
tts.save(audio_file)
# return_code = subprocess.call(["afplay", audio_file])
song = AudioSegment.from_mp3(audio_file)
play(song)
