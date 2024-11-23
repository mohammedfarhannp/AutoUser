# Import Section
import re
import tkinter

from os import system

# Functions
## Function for checking input word with input rule.
def Validate(RULE, WORD):
    return False if re.search(RULE, WORD) == None else True

## Function to display a message.
def Display_Msg(Prompt, Color):
    Message.config(text=Prompt, fg=Color,justify='left')

## Function to clear input fields of tkinter window
def Clean():
    User_Input.delete(0, tkinter.END)
    Pass_Input.delete(0, tkinter.END)

## Function of Pop button
def Pop():
    Username = User_Input.get()
    if Username in USERS.keys():
        del USERS[Username]
        Display_Msg("User Deleted!", "green")

    else:
        Display_Msg("User not found!", "red")
    Clean()

## Function of Add button
def Add():
    Username = User_Input.get()
    if not Validate(REGEX_USER, Username):
        Display_Msg("Invalid Username!\nlowercase letters only\nlength 4 to 20 characters!","red")
        return None
    Password = Pass_Input.get()
    if not Validate(REGEX_PASS, Password):
        Display_Msg("Invalid Password!\nRequirements\nAtleast 1 Lowercase\nAtleast 1 Uppercase Letter\nAtleast 1 digit\nAtleast 1 special character\nPassword Length between 6 and 18 characters", "red")
        return None

    USERS.update({Username:Password})
    Display_Msg("User Added!","green")
    Clean()

## Function of Make Account button
def Make():
    for User, Pass in USERS.items():
        Command = CMD.format(User, Pass)
        system(Command)
    Display_Msg(f"{len(USERS)} Users has been\ncreated on this system", "blue")
    USERS.clear()

# Variables
## Regex Rules
REGEX_PASS = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;\"'<>,.?/-]).{6,18}$"
REGEX_USER = r"^[a-z]{4,20}$"

## Window Variables
TITLE = "User Create Automation"
SIZE = "500x500"

## User Creation Variables
USERS = {}
CMD = "sudo useradd -m -s /bin/bash {0} && echo \"{0}:{1}\" | sudo chpasswd"

# Main
## Window Creation
window = tkinter.Tk()
window.title(TITLE)
window.geometry(SIZE)

## User Input
User_Label = tkinter.Label(window, text="USERNAME", font=("Arial", 14), fg="green")
User_Label.place(x=30, y=70)

User_Input = tkinter.Entry(window)
User_Input.place(x=150, y=70, width=200, height=30)

## Password Input
Pass_Label = tkinter.Label(window, text="PASSWORD", font=("Arial", 14), fg="green")
Pass_Label.place(x=30, y=130)

Pass_Input = tkinter.Entry(window, show="*")
Pass_Input.place(x=150, y=130, width=200, height=30)

## Add Button
Add_Button = tkinter.Button(window, text="Add", font=("Arial",14),fg="white",bg="green",command=Add)
Add_Button.place(x=400, y=80)

## Pop Button
Pop_Button = tkinter.Button(window, text="Pop", font=("Arial", 14),fg="white",bg="red",command=Pop)
Pop_Button.place(x=400, y=150)

## Make Accounts Button
Make_Button = tkinter.Button(window, text="Make Accounts", font=("Arial", 14), fg="white", bg="blue", command=Make)
Make_Button.place(x=300, y=450)

## Message Label for displaying messages as a response to user interaction
Message = tkinter.Label(window, text="", font=("Arial", 12))
Message.place(x=100,y=200)

# Loop
window.mainloop()

