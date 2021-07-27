import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + bcolors.BOLD + "Password Strength Determinator." + bcolors.ENDC)
print("===============================================================")

running = True
i = 0

while running:
    password = input("Enter Password: ")

    if len(password) <= 9:
        print("Password Strength: " + bcolors.FAIL + "Too Weak." + bcolors.ENDC + "(Try a longer password).")

    elif password.isdigit():
        print("Password Strength: " + bcolors.OKBLUE + " Moderate." + bcolors.ENDC + " (Try adding alphebets and special characters to make it stronger).")

    elif password.islower():
        print("Password Strength: " + bcolors.OKBLUE + " Moderate." + bcolors.ENDC + "(Try using atleast 1 Upper case letter to make it stronger.)")

    elif password.isupper():
        print("Password Strength: " + bcolors.OKBLUE + " Moderate." + bcolors.ENDC + "(Try using Lower case letters to make it stronger. )")

    elif password.isalpha():
        print("Password Strength:" +bcolors.OKGREEN + " Strong." + bcolors.ENDC + "(Try adding numbers and special characters to make it stronger).")

    elif password.isalnum():
        print("Password Strength:"+ bcolors.OKGREEN + " Super Strong." + bcolors.ENDC + "(Tip: Use special characters to make your password Ultra-Strong.)")

    elif not re.match('.,:;-A-Za-z1234567890!#%&*@[_\W]+$', password):
        print("Password Strength:" + bcolors.OKGREEN + bcolors.BOLD + " Ultra Strong." + bcolors.ENDC + "(Congratulations!! Your password is PSD certified :) )")

    else:
        print("Password is Invalid.")






