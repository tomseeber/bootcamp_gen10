# Intial Comment for python file

myword = "Mississippi"
correctletters = []

for char in myword:
    correctletters.append("_")

#print(correctletters)

#if "i" in myword:
#    print("I did soemthing")
    
myword_list = list(myword)
#print(myword_list)
guess = "i"

for position in range(len(myword_list)):
    if myword_list[position] == guess:
        print(position)
        print(myword_list[position])
        correctletters[position] = guess
        

print(myword_list) 
print(correctletters)