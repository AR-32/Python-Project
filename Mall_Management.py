import pandas as pd
from datetime import datetime

class Owner:
    def __init__(self):
        #self.database = None
        self.emp = None
        self.choice = input('EMPLOYEE or SHOP or EXIT:-  ').lower()
        if self.choice == 'employee':
             self.employee()
        elif self.choice == 'shop':
             self.shop()
        elif self.choice == 'exit':
             exit()
        else:
             print('Invalid choice')
             Owner()

    def employee(self):
        print('''1-->Employee Details
2-->Edit Employee Details
3-->Salary of Employee
4-->Exit''')
        while True:  
            choice = int(input("Enter choice:-  "))
            if choice == 1:
                self.emp_information()
                break  
            elif choice == 2:
                self.emp_edit()
                break
            elif choice == 3:
                self.emp_salary()
                break
            elif choice == 4:
                Owner()
            else:
                print("Invalid choice")

    def emp_information(self):
        emp_id = ['50012324', '50023421', '50023432', '50067432']
        emp_name = ['Raj', 'Karan', 'Arjun', 'Viraj']
        emp_sname = ['Kumar', 'Singh', 'Gosai', 'Singh']
        emp_salary = [12000,10000,13000,11000]
        emp_job = ['Watchman', 'Cleaner', 'Security Guard', 'Parking Guard']
        mobile = [7089365241, 9876578321, 6789054321, 8907654321]
        self.emp = {'Employee ID': emp_id, 'Name': emp_name, 'Surname': emp_sname, 'Salary': emp_salary, 'Job': emp_job, 'Mobile Number': mobile}
        emp_print = pd.DataFrame(self.emp, index=[1, 2, 3, 4])
        print(emp_print)
        self.employee()

    def emp_edit(self):
        #global emp
        print("""1-->add employee
2-->remove employee
3-->edit employee info
4-->exit""")
        o_choice = int(input("enter your choice sir :"))
        if o_choice == 1:
            new_emp = input("name of the new employee :")
            new_id = new_emp[:2]+"123"
            self.emp[new_emp] = new_id
            print(f"{new_emp} got the job ")
            self.emp_edit()
        elif o_choice == 2:
            emp_name = input("enter the name of the employee :")
            if emp_name in self.emp.keys():
                self.emp.pop(emp_name)
            else:
                print(f"{emp_name} does not exist")
            self.emp_edit()
        elif o_choice == 3:
            old_emp = input("enter the employe name")
            if old_emp in self.emp.keys():
                self.emp.pop(old_emp)
                new_emp = input("enter the employee name to edit. :")
                new_id = new_emp[:2]+"123"
                self.emp[new_emp] = new_id
            else:
                print(f"{old_emp} does not exist")
            self.emp_edit()
        elif o_choice == 4:
            self.employee()
        else:
            print("invalid choice")
            self.emp_edit()
        self.employee()

    def emp_salary(self):
        if self.emp:
            num_employees = len(self.emp['Employee ID'])
            for i in range(num_employees):
                emp_id = self.emp['Employee ID'][i]
                emp_name = self.emp['Name'][i]
                emp_salary = self.emp['Salary'][i]  
                print(f"Employee ID: {emp_id}, Name: {emp_name}, Salary: {emp_salary}")
        else:
            print("Employee information is not available.")
        self.employee()

    def shop(self):
        print('''1-->Tenure
2-->Rent
3-->Agreements
4-->Payments
5-->Exit''')
        while True:
            choice = int(input("Enter choice:-  "))
            if choice == 1:
                self.tenure()
                break  
            elif choice == 2:
                self.rent()
                break  
            elif choice == 3:
                self.agreement()
                break
            elif choice == 4:
                self.payment()
            elif choice == 5:
                Owner()
            else:
                print("Invalid choice")

    #Tenure
    def tenure(self):
        cust_tenure = {'Name': ['Akshat', 'Kritika', 'Vedika', 'Kittu', 'Aayush', 'Nilaksh', 'Sajid', 'Akshita', 'Bhupendra'],
                       '  Phone No.': [9368804819, 9571099887, 9746214710, 7649872100, 8763400124, 7562910241, 6212946728, 9104621488, 8104623939],
                       '  Address': ['Jaipur-234567', 'Delhi-123456', 'Bangalore-987655', 'Alwar-563871', 'Pune-282234', 'Mumbai-761212', 'Srinagar-912356', 'Puri-341001', 'Chennai-280001'],
                       '  Gmail': ['akshat12@gmail.com', 'kritika12@gmail.com', 'vedika12@gmail.com', 'kittu12@gmail.com', 'aayush12@gmail.com', 'nilaksh12@gmail.com', 'sajid12@gmail.com', 'akshita12@gmail.com', 'bhupendra12@gmail.com']}
        cust = pd.DataFrame(cust_tenure, index=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(cust)
        self.shop()

    #Rent
    def rent(self):
        shops = [
            {'name': 'Jwellary Store', 'is_rented': True, 'items_sold': 'Jwellary, Silver Coins'},
            {'name': 'Shoes Store', 'is_rented': True, 'items_sold': 'Branded Shoes'},
            {'name': 'Shop A', 'is_rented': False, 'rent_price': 15000, 'dimensions': '900 sq ft', 'location': 'First Floor'},
            {'name': 'Book Store', 'is_rented': True, 'items_sold': 'Magazines, Story Books, Comics etc.'},
            {'name': 'Eat & Fat Food Store', 'is_rented': True, 'items_sold': 'Fast Food, Ice Cream'},
            {'name': 'Shop B', 'is_rented': False, 'rent_price': 25000, 'dimensions': '1100 sq ft', 'location': 'Second Floor'},
            {'name': 'Game Store', 'is_rented': True, 'items_sold': 'Game Zone, Video Games'},
            {'name': 'Laptop Store', 'is_rented': True, 'items_sold': 'Laptops'},
            {'name': 'Smartphone Store', 'is_rented': True, 'items_sold': 'Smartphones, Chargers, Headphones'},
            {'name': 'Shop C', 'is_rented': False, 'rent_price': 50000, 'dimensions': '15abc00 sq ft', 'location': 'Second Floor'},
            {'name': 'Make Up Store', 'is_rented': True, 'items_sold': 'Make up Accessories'},
            {'name': 'Fancy Clothes Store', 'is_rented': True, 'items_sold': 'Clothing, Accessories'},
        ]
        rented_shops = [shop for shop in shops if shop['is_rented']]
        not_rented_shops = [shop for shop in shops if not shop['is_rented']]

        print(f"Number of shops on rent: {len(rented_shops)}")
        print(f"Number of shops not on rent: {len(not_rented_shops)}\n")

        if rented_shops:
            print("Shops on Rent:")
            for shop in rented_shops:
                print(f"Name: {shop['name']}, Items Sold: {shop['items_sold']}")
            print()

        if not_rented_shops:
            print("Shops Not on Rent:")
            for shop in not_rented_shops:
                print(f"Name: {shop['name']}, Rent Price: {shop['rent_price']}, Dimensions: {shop['dimensions']}, Location: {shop['location']}")
        self.shop()
                
    #Agreement
    def agreement(self):
        cust_agmen = {'Renter Id': ['Aks213', 'Kri583', 'Ved123', 'Kit900', 'Aay365', 'Nil873', 'Saj109', 'Aks366', 'Bhu591'],
                      '  Renter Name': ['Akshat', 'Kritika', 'Vedika', 'Kittu', 'Aayush', 'Nilaksh', 'Sajid', 'Akshita', 'Bhupendra'],
                      '  Rent in Rs': [90000, 40000, 45000, 50000, 55000, 63000, 85000, 60000, 92500],
                      '  Area': ['1800 sq foot', '800 sq foot', '900 sq foot', '1000 sq foot', '1100 sq foot', '1260 sq foot', '1700 sq foot', '1200 sq foot', '1850 sq foot'],
                      '  Shop holdings': ['Jwellary Store', 'Shoes Store', 'Book Store', 'Eat & Fat Food Store', 'Game Store', 'Laptop Store', 'Smartphone Store', 'Make Up Store', 'Fancy Clothes Store']}
        cust = pd.DataFrame(cust_agmen, index=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(cust)
        self.shop()

    #Payment
    def payment(self):
        database = [
            {'user_id': 'Aks213', 'payment_done': True, 'due_date': datetime(2024, 4, 5)},
            {'user_id': 'Kri583', 'payment_done': False, 'due_date': datetime(2024, 3, 30)},
            {'user_id': 'Ved123', 'payment_done': True, 'due_date': datetime(2024, 4, 7)},
            {'user_id': 'Aay365', 'payment_done': False, 'due_date': datetime(2024, 4, 4)},
            {'user_id': 'Kit900', 'payment_done': True, 'due_date': datetime(2024, 4, 8)},
            {'user_id': 'Nil873', 'payment_done': False, 'due_date': datetime(2024, 4, 1)},
            {'user_id': 'Bhu591', 'payment_done': True, 'due_date': datetime(2024, 4, 13)},
            {'user_id': 'Aks366', 'payment_done': False, 'due_date': datetime(2024, 3, 12)},
            {'user_id': 'Saj109', 'payment_done': False, 'due_date': datetime(2024, 2, 29)}
        ]
        report = []
        for user in database:
            if user['payment_done']:
                status = 'Payment completed'
                fine = 0
                #report.append(f"User {user['user_id']}: {status}, Fine: {fine * 100}%")
            else:
                status = 'Payment not completed'
                fine = self.calculate_fine(user['due_date'])
            report.append(f"User {user['user_id']}: {status}, Fine: {fine * 100}%")
        print('\n'.join(report))
        self.shop()

    def calculate_fine(self, due_date):
        current_date = datetime.now()
        due_days = (current_date - due_date).days

        if due_days <= 0:
            return 0
        elif due_days in range(1, 11):
            return 0.10  # 10% fine
        elif due_days in range(11, 21):
            return 0.20  # 20% fine
        else:
            return 0.30  # 30% fine

def main():    
    print("Welcome Sir \n\n")
    password = 'abc'
    for i in range(3):
        user = input('Password:  ')
        if user == password:
            E1 = Owner()
            break
        else:
            print("incorrect password, try again.")
            if i == 2:
                print("Anonymous")
                exit()
#MAIN
main()