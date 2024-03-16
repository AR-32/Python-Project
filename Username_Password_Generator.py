import random
from random import *
def username():
    user = input("Your Name:  ")
    random_integer = randint(1,6)
    username_generator = str(user[0:3] + str(random_integer))
    return username_generator
def password():
    pan_ID = [randint(1,20)]
    aadhar_ID = [randint(1,10)]
    password_generator =  pan_ID[2:5] + aadhar_ID[1:5]
    return str(password_generator)

