from openai import OpenAI

client = OpenAI(
    api_key="Use your own API key"
)

audio_file= open("my_audio.m4a", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)
