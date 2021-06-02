# this is a simple quiz
#initial score

score = 0
#ask for name
while True:
    name = input ("Enter your name : ")
    if name.isalpha():
        break
    print("Please enter character A-Z only")
print(name)

def greet(name):
	name=input("enter your name : ")
	print("hello {} your score is  {}".format(name) )


#Ask for age
age = int(input("What is your age? : "))
 
#Ask for year level
yrlvl = int(input("Enter your year level: "))


def instructions():

  first_time = input("Would you like to read the instructions? ")

  if first_time == "no":
    return ""

  else:
    print()
    print("******* Aryans Instructions ********")
    print()
    print("Either choose a number or the question ")
    print()
    print("The rules are simple...")
    print("if u get the right awnser ")
    print("youll gain a point")
    print("more points = higher chance to win")
    print()
    print("Have fun!")
    print()


# set of questions that are asked
#Question One
answer1 = input("What Phone has 108Megapixels camera that came out in 2020? \nA. S20 Ultra \nB. Iphone 12 pro \nC. S40 Pro \nAnswer : ")
if answer1 == "A" or answer1 == "a" or answer1 == "S20 Ultra":
    score += 1
    print("Correct!")
    print("Score : ", score)
    print("\n")
else:
    print("Incorrect, The answer is S20 Ultra 5g! Samsung created the first 108 mega pixel senor for a phone!")
    print("Score: ", score)
    print("\n")

    #Question 2

answer1 = input("Which AMD Graphics card is simuliar to a RTX 2060 graphics card? \nA. RX5600XT 6GB \nB. RX580 8GB\nC. RX5800XT  \nAnswer : ")
if answer1 == "A" or answer1 == "a" or answer1 == "RX5600XT 6GB":
    score += 1
    print("Correct!")
    print("Score : ", score)
    print("\n")
else:
    print("Incorrect, The answer RX5600xt as it is the closest graphics card to rival the Rtx 2060!")
    print("Score: ", score)
    print("\n")

    #question 3

answer1 = input("Who created the trackpoint? \nA. IBM Thinkpad \nB. Dell Inc \nC. Apple inc \nAnswer : ")
if answer1 == "A" or answer1 == "a" or answer1 == "IBM Thinkpad":
    score += 1
    print("Correct!")
    print("Score : ", score)
    print("\n")

else:
    print("Incorrect, The answer is IBM thinkpad! they were the frist to create the trackpoint")
    print("Score: ", score)
    print("\n")


answer1 = input("What CPU brand uses Pins on the back of their processors ? \nA. AMD \nB. Intel \nC. M1 by apple \nAnswer : ")
if answer1 == "A" or answer1 == "a" or answer1 == "AMD":
    score += 1
    print("Correct!")
    print("Score : ", score)
    print("\n")

else:
    print("Incorrect, The answer is AMD! intel does not use pins!")
    print("Score: ", score)
    print("\n")

greet()    







