import Username_Password_Generator
from Username_Password_Generator import *
def first_time_login():
    username = input("Enter Username:  ")
    original_password = Username_Password_Generator.password() 
    guess_count = 2
    password1 = input("Enter Password:  ")
    while guess_count != 0:
         if password1 == original_password:
           print("Loading....\nHomepage of Kittu Fraud Bank",end = "")
           break
         else:
           guess_count -= 1
           print("try again")
           password1 = int(input("enter again:  "))
    if guess_count == 0:
      print("Try after 15 minutes")
def username_reset():
    old_username = input("Enter Old Username:  ")
    new_username = input("Enter New Username:  ")
    print("Your Username has been changed. Your new username is" + new_username)
def password_reset():
    old_password = input("Enter Old Password:  ")
    new_password = input("Enter New Password:  ")
    old_password = new_password
    print("Your Password has been changed.")
    return old_password
