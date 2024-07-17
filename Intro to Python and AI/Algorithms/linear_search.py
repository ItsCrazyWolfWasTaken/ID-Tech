entries = [32, 14, 89, 62, 10, 20, 88, 40, 22, 91, 88, 65]
correct_answer = input("What is the correct answer? ")
complete = False
counter = 1
for i in entries:
    if i == correct_answer and complete == False:
        print("Student " + str(counter) + " got it correct first.")
        complete = True
    elif i == correct_answer:
        print("Student " + str(counter) + " also got it correct.")
    else:
        print("Student " + str(counter) + " got it incorrect.")
    counter += 1
