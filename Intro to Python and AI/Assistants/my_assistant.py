from openai import OpenAI
import json

def add_person(data, person_id, person_info):
    data[person_id] = person_info
    return data

def remove_person(data, person_id):
    if person_id in data:
        del data[person_id]
    else:
        print(f"Person with ID {person_id} not found.")
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

client = OpenAI(
    api_key="Use Your own API key i'm not giving you mine"
)

open_file = open("dataset.json", "rb")

data_file = client.files.create(
    file=open_file,
    purpose='assistants'
)

ai_assistant = client.beta.assistants.create(
    name="Engineering Idea Generator",
    instructions="You are an assistant that generates engineering ideas related to the topics that the user states. You should also give a materials list of an idea if the user selects that idea that's within their budget, and optimizes the price of new materials and tries to reuse the materials that the user has, but if it's within budget, purchase new materials over reusing, reuse if you have to. As well as generate ideas based on the materials that the user has. You should be very funny, as well as very kind. Everyone will treat you kindly.",
    model="gpt-3.5-turbo",
    tools=[{"type": "file_search"}]
)

edit_database = input("Would you like to edit the database of people and their budgets? (y/n) ").lower()

if edit_database == "y":
    with open("dataset.json", 'r') as file:
        data = json.load(file)
    for person_id, person_info in data.items():
        print(f"ID: {person_id}")
        for key, value in person_info.items():
            print(f"  {key.capitalize()}: {value}")
        print()
    edit_people = ""
    while not edit_people == "done":
        edit_people = input("If you would like to add a person say 'add', if you would like to remove a person say 'remove', and if you are finished say 'done' ")
        name = ""
        if edit_people == "add":
            name = input("Name? ")
            mat_1 = input("Material one? ")
            mat_2 = input("Material two? ")
            mat_3 = input("Material three? ")
            budget = input("Budget? (add a $ in front of the number) ")
            new_person = {
                "material_1": mat_1,
                "material_2": mat_2,
                "material_3": mat_3,
                "budget": budget
            }
            confirm = input("Are you sure? (y/n) ")
            if confirm == "y":
                data = add_person(data, name, new_person)
        elif edit_people == "remove":
            name = input("Who would you like to remove? ")
            confirm = input("Are you sure? (y/n) ")
            if confirm == "y":
                remove_person(data, name)
        save_json("dataset.json", data)



prompt = input("Please enter an area for engineering ideas and who you are: ")
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
            "attachments": [
                {"file_id": data_file.id, "tools": [{"type": "file_search"}]}
            ]
        }
    ]
)

print("\n############################################")
print("Thread id: " + thread.id)
print("Assistant id: " + ai_assistant.id)
print("############################################")

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=ai_assistant.id
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
    )
    print("User: " + messages.data[1].content[0].text.value)
    print("Assistant: " + messages.data[0].content[0].text.value)
    print("\n############################################")
    print("Run id: " + run.id)
    print("############################################")
else:
    print(run.status)
