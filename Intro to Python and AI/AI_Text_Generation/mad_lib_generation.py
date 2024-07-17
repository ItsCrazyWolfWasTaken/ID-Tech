from openai import OpenAI

client = OpenAI(
    api_key = "Use your own API key im not giving you mine"
)

subject = ["emotion", "color", "family member", "country", "state", "noun", "food", "ocean", "verb", "type of metal", "job", "animal", "adjective", "instrument", "musician", "name", "building"]

list_of_words = []
string_of_words = ""

for x in range(17):
    get_input = input("Please type in a(n) " + str(subject[x]) + ": ")
    list_of_words.append(get_input)

system_data = [
    {"role": "system", "content": "Generate a funny two-paragraph Mad Lib story using the words."},
    {"role": "user", "content": string_of_words.join(list_of_words)}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=system_data
)

assistant_response = response.choices[0].message.content
system_data.append({"role": "assistant", "content": assistant_response})
print("Assistant: " + assistant_response)
