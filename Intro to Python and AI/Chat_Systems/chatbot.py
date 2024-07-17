from openai import OpenAI

client = OpenAI(
    api_key = "sk-proj-zb7dRzvTbArDGy6is6oYT3BlbkFJl6JISDKrE1OmOTXMcgbO"
)

end_program = False

while not end_program:
    get_input = input("Please ask for engineering ideas in a specific field: ")
    if get_input.lower() == "goodbye" or get_input.lower() == "exit":
        end_program = True
        print("Toodaloo mother...")
    else:
        system_data = [
            {"role": "system", "content": "You are an assitant that generate ideas for engineering projects related to what the user asks kindly. You also should be able to tell the user where to purchase the materials required to make those ideas. You should also be able to give them a step by step process on building the idea if they ask for it. You should be very nice, but also a little sassy and funny, but always kind to everyone."},
            {"role": "user", "content": get_input}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=system_data
        )
        assistant_response = response.choices[0].message.content
        system_data.append({"role": "assistant", "content": assistant_response})
        print("From the assistant: " + assistant_response)
