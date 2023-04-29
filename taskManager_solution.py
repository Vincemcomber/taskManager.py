#I asked for help from my friends Adrian, Mpho and Andile to solve this task.
# Initialize the file names.
user_options = "r"
user_username = "admin"

# Only the user logged in as 'admin', will be able to access this menu.
if user_options == "r":   

    if user_username != "admin":
        
        print ("You are not an admin user, only admin can register new users.")

    elif user_username == "admin":

# Create a new menu to display for admin.
        admin_menu = (input("""
Please select one of the following options:
r - register a new user
d - display statistics = Total number of tasks & users
e – exit
"""))

        if admin_menu == "r":

            new_user = (input("Please enter a new user name: "))
            new_user_password = (input("Please enter a new password: "))

            new_password = False
            while new_password == False:   # Add a 'while loop' untill the condition is met(True).
                confirm_new_password = input("Please retype your password to confirm: ")

                if new_user_password == confirm_new_password:
                    new_password = True

                elif new_password == False:
                    print("Your passwords do not match!")

            with open ('user.txt', 'a')as user_file:
                user_file.write(f"\n{new_user}, {new_user_password}")

        elif admin_menu == "d":

# These varibles will only count the lines inside the 'txt' files,
# but since we are storing every new task & user on a new line,
# we can just count the lines for the desired results.
            tasks_num = 0
            users_num = 0

            with open("tasks.txt", "r") as task_file:
                for line in task_file:
                    tasks_num += 1
            print (f"\nTotal number of tasks: {tasks_num}")

            with open("user.txt", "r") as username:
                for line in username:
                    users_num += 1
            print (f"Total number of users: {users_num}")

        elif admin_menu == "e":
            exit

