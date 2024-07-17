from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-zb7dRzvTbArDGy6is6oYT3BlbkFJl6JISDKrE1OmOTXMcgbO"
)

audio_file= open("my_audio.m4a", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)