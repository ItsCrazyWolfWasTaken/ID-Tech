a = "hello"
var = "hi"+a



password = "test123!"
guessed_password = input("password")
while not guessed_password == password:
    guessed_password = input("password")
adj_1 = input("adjective")
name_1 = input("name")
adj_2 = input("adjective")
name_2 = input("name")
plane_1 = input("plane")
plane_2 = input("plane")
air2air = input("air to air missle")
opinion = input("opinion")
story = "Once upon a time, a "+adj_1+" fighter pilot named "+name_1+" flew the "+plane_1+". \n"+adj_1+" "+name_1+" "+opinion+" flying the "+plane_1+".\nThe "+adj_2+" fighter pilot named "+name_2+" flies the "+plane_2+".\n"+adj_1+" "+name_1+" and "+adj_2+" "+name_2+" got into a dog fight.\nthe "+plane_1+" got a missle lock on the "+plane_2+", and fired "+air2air+".  \nThe "+plane_2+" was able to deploy flares, and dodged the "+air2air+", and fired their cannons on "+plane_1+". \n the "+plane_1+" was blown out of the sky."
print(story)
