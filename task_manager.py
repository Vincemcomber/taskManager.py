#I asked for help from Andile and Mpho.
#I got some idea from stack overflow.

#import statement
import os
from datetime import date


#functions defined
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def Menu():
    if usrnm:
        print("Login Sucess : " + usrnm + "\n")
    print("'r' : register a user")
    print("'a' : add a task")
    print("'va' : view all task")
    print("'vm' : view your task")
    print("'c' : clear console")
    print("Enter to exit ")

#The code must read usernames and password from the user.txt file
#Use a list or dictionary to store a list of usernames and passwords from the file.
#Use loop to validate your user name and password.
global isLogin
isLogin = False
def ShowSelectMenu(select):
    if select == 'l' and not isLogin:
        Login()
    #In this block you will write code to add a new user to the user.txt file
    #You can follow the following steps:
            # Request input of a new username
            # Request input of a new password
            # Request input of password confirmation.
            # Check if the new password and confirmed password are the same.
            # If they are the same, add them to the user.txt file,
            # Otherwise you present a relevant message
    elif select == 'r' and not isLogin:
        Register()

    #In this block you will put code that will allow a user to add a new task to task.txt file
        # You can follow these steps:
            # Prompt a user for the following: 
                # A username of the person whom the task is assigned to,
                # A title of a task,
                # A description of the task and 
                # the due date of the task.
            # Then get the current date.
            # Add the data to the file task.txt and
            # You must remember to include the 'No' to indicate if the task is complete.
    elif select == 'a':
        AddTask()

    #In this block you will put code so that the program will read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf file page 6.
         #You can do it in this way:
            # Read a line from the file.
            # Split that line where there is comma and space.
            # Then print the results in the format shown in the Output 2 in L1T19 pdf
            # It is much easier to read a file using a for loop.
    elif select == 'va':
        ViewAllTask()

    #In this block you will put code the that will read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf file page 6.
         #You can do it in this way:
            # Read a line from the file.
            # Split the line where there is comma and space.
            # Check if the username of the person logged in is the same as the username you have read from the file.
            # If they are the same you print the task in the format of output 2 shown in L1T19 pdf
    elif select == 'vm':
        ShowSpecificTask()

    #To clear or exit the program.
    elif select == 'c':
        clearConsole()
        Menu()
        ShowSelectMenu(input("\n Select Options: "))

#The username of the person to whom the task is assigned.
#The title of the task.
#A description of the task.
#The date that the task was assigned to the user.
#The due date for the task.
#Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.
def AddTask():
    srnm = input("username to which task assign : ")
    title = input("Title : ")
    describe = input("Description : ")
    dateToday = date.today()
    dueDate = input("Due Date (dd/mm/yy): ")

    f = open('./tasks.txt', 'a')
    f.write(usrnm + ', ' + title + ', ' + describe + ', ' + str(dateToday) + ', ' + dueDate + '\n')
    f.close()
    clearConsole()
    Menu()
    print("\nAdd Task Success")
    ShowSelectMenu(input("\nSelect Options: "))


def ViewAllTask():
    with open('./tasks.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)            
    ShowSelectMenu(input("Select Options : "))


def ShowSpecificTask():
    print('\n')
    with open('./tasks.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            word = line.split(',')
            if word[0] == usrnm:
                print(word[1] + ' ' + word[2] + ' ' + word[3] + ' ' + word[4])
    ShowSelectMenu(input("Select Options: "))


def Login():
    print("\nLogin with username and password : \n")
    global usrnm
    usrnm = input("Username: ")
    username = usrnm
    pwd = input("Password: ")

    with open('./user.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            word = line.split(',')
            word[len(word)-1] = word[len(word)-1].replace('\n', '').replace(' ', '')
            if word[0] == usrnm and word[1] == pwd:
                isLogin = True
                clearConsole()
                Menu()
                ShowSelectMenu(input("\nSelect Options: "))
                return

    print("Login Fail")
    print("Press 'l' to login again")
    select = input("\nSelect Options: ")
    clearConsole()
    ShowSelectMenu(select)


def Register():
    print("\nRegister with username and password : \n")
    usrnm = input("Username: ")
    pwd = input("Password: ")

    f = open('./user.txt', 'a')
    f.write(usrnm + ', ' + pwd + '\n')

    #close the program.
    f.close()

    clearConsole()

# Menu()
    print("\nRegister Success")
    Login()

# main
print("Welcome to Task Manager\n'r' : user register")
print("'l' : user login")

select = input("\n Select (l or r) : ")
ShowSelectMenu(select)
