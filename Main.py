def da():
    d = int(input("Enter date:  "))
    m = int(input("Enter month:  "))
    y = int(input("Enter year:  "))
    return date(y,m,d)







print('~'*100)
print('~'*100)
print("                                       किट्टू फ्रॉड बैंक में आपका स्वागत है                                       ")
print("                                       Welcome to Kittu Fraud Bank                                      ")
print('~`'*50)
print("                                                 Spotlight                                               ")
print("                           Kittu Fraud Bank receives PCI PIN Certification\n                              Kittu Fraud Bank wins'STAR PERFORMER-RANK 1'\n                           Financial Results for the Quartwe ended December 31,2023\n                           Kittu Fraud Bank secures 2nd Rank in EASE reforms")
print('~`'*50)
print('~`'*50)
import Account
from Account import *
import Username_Password_Generator
from Username_Password_Generator import *
import first_login
from first_login import *
import Account_Card_PIN_Generator
from Account_Card_PIN_Generator import *
import ATM
from ATM import *
aa = int(input("Enter 1 if you have already registered or enter any number if you have not registered:  "))
if aa == 1:
    ccc = int(input("Do you want to reset your username and password ???\nIf 'yes' type 1 else type any number:  "))
    if ccc == 1:
        ddd = first_login.username_reset()
        eee = first_login.password_reset()
        print("Your new Username is: "+ddd,"\nYour new Password is: "+eee)
    print('\n')
    print('*'*60)
    print('\n')
    print("You have successfully registered yourself in Kittu Fraud Bank !!!!")
    print("It's time to recieve your Bank Account Number, Card Number and PIN")
    print('.'*60)
    hhh = Account_Card_PIN_Generator.account_n()
    iii = Account_Card_PIN_Generator.card()
    jjj = Account_Card_PIN_Generator.pin()
    print("Bank Account Number: "+hhh,"\nCard Number: "+iii,"\nPIN: "+jjj)
    print('\n')
    print('*'*60)
    print('\n')
else:
    print("First you have to create an account to get username and password!!")
    print("Provide us with your personal details.")
    acc = {'name':input("Enter Your Fullname:  "),'dob':da(),'address':input("Enter Your Address(City and State only):  "),'pan_card':str(input("Enter Your Pan-Card ID:  ")),'aadhar_card': int(input("Enter Your Aadhar-Card Number:  ")),'contact_number':int(input("Enter Your Contact Number:  ")),'e_mail':input("Enter Your e-mail address:  "),'balance':float(input("Enter Your Income per year:  "))}
    print("~"*50)
    print("Preview your account details")
    for i,j in acc.items():
        print(i,'  :  ',j)
    print("~"*50)
    print("Your Account has been created successfully!!!!!\nThank You for choosing us")
    print("Your username and password is:  ")
    print("Loading.....")
    aaa = Username_Password_Generator.username()
    bbb = Username_Password_Generator.password()
    print("Username: "+aaa,'\n',"Password: "+bbb)
    print('*'*60)
    print("Now first, you have to login into your account!!")
    print('\n')
    first_login.first_time_login()
    print('\n')
    ccc = int(input("Do you want to reset your username and password ???\nIf 'yes' type 1 else type any number:  "))
    if ccc == 1:
        first_login.username_reset()
        eee = first_login.password_reset()
        print("\nYour new Password is: ",eee)
    print('\n')
    print('*'*60)
    print('\n')
    print("You have successfully registered yourself in Kittu Fraud Bank !!!!")
    print("It's time to recieve your Bank Account Number, Card Number and PIN")
    print('.'*60)
    hhh = Account_Card_PIN_Generator.account_n()
    iii = Account_Card_PIN_Generator.card()
    jjj = Account_Card_PIN_Generator.pin()
    print("Bank Account Number: "+hhh,"\nCard Number: "+iii,"\nPIN: "+jjj)
    print('\n')
    print('*'*60)
    print('\n')
    print("Proceeding towards ATM Machine.......")
    print("Loading......")




    #Working of ATM Machine
gggg = iii
print(gggg)
while (1):
    Card = str(input("Enter last 4-digits of your card number:  "))
    if Card in gggg:
        i=3
        while(i>0):
            pin = str(input("Enter PIN:  "))
            aaaa = jjj
            if pin == aaaa:
                while(1):
                    print("Enter 1 for Account Info")
                    print("Enter 2 for PIN Change")
                    print("Enter 3 for Balance Inquiry")
                    print("Enter 4 for Withdrawal")
                    print("Enter 5 for Deposit")
                    print("Enter 6 for Recipit")
                    se = int(input("Select Option:  "))
                    if se == 1:
                        print('Account Information: ')
                        print('Name: ', acc['name'], end='\n')
                        print('Account Number: ', hhh, end='\n')
                        print('Phone Number: ', acc['contact_number'], end='\n')
                    elif se == 2:
                        a=3
                        b = Account_Card_PIN_Generator.pin()
                        while(a>0):
                            pi=str(input("Enter Original PIN:   "))
                            if pi == b:
                                new_pin = str(input("Enter New PIN:  "))
                                b = new_pin
                                break
                            else:
                                a=a-1
                                print("PIN incorrect,",a,"tries left")
                            if a==0:
                                print("Account Blocked!!!!!!")
                    elif se == 3:
                        print("Account Balance:  ",acc['balance'])
                    elif se == 4:
                        ll = acc['balance']
                        print("Account Balance:  ",ll)
                        amount = float(input("Enter Amount to be withdrawn:  "))
                        if amount <= ll:
                            ll = ll - amount
                            print("Successfully Withdrawled!!!!!!!")
                            print("New Account Balance is :  ", ll)
                        else:
                            print("Insufficient Balance in Account!")
                    elif se == 5:
                        nn = acc['balance']
                        amou = float(input("Enter Amount to be deposited:  "))
                        nn = nn + amount
                        print("New Account Balance:  ", nn)
                    elif se == 6:
                        dt = datetime.now()
                        g = Account_Card_PIN_Generator.card()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Kittu Fraud Bank~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Date and Time:  ",dt)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("\n")
                        print("CardNo: XXXX XXXX XXXX ",g)
                        print("Amount:  ",amount,"Rs")
                        yy = Account_Card_PIN_Generator.account_n()
                        print("Account No:  ",yy)
                        zz = amou
                        if tt >= 0:
                            a = ww - tt
                            print("Available Balance: ",a,"Rs")
                        elif zz >= 0:
                            b == ww + zz
                            print("Available Balance: ",a,"Rs")
                        else:
                            print("Available Balance: ",a,"Rs")
                        print("ATM Opertor fee: ",5,"Rs")
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e = input("Enter Y to exit, press any other key to continue operations:  ")
                    if e == "y" or e == "Y":
                        print("Thank You!!!!!")
                        break
                    else:
                        continue
                break
            else:
                i = i - 1
                print("PIN incorrect,",i,"tries left")
        if i == 0:
            print("Account Blocked!!!!!!")
        break
            

