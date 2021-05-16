
'''
#Asking Name
while True:
    name = input("Please enter your name : ")
    if name.isalpha():
        break
    print("Please enter letter only.")

#Asking Age
while True:
    age = input("Please enter your age : ")
    if age.isnumeric():
        break
    print("Please enter numbers only.")

#Asking Year level
while True:
    yearlvl = input("Please enter your year level : ")
    if yearlvl.isnumeric():
        break
    print("Please enter numbers only.")

#Asking Status
while True:
    status = str(input("Please enter y to start the quiz and n to stop the quiz : "))
    if status.isalpha():
        break
    print("Please enter letter only.")
