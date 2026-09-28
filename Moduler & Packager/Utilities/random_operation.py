import random
import string


def random_menu():

    while True:
         print("""
         Random Data Generation

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu
""")
         inner_user = int(input("Enter your choice: "))
        
         if inner_user == 1:
                    num = random.randint(0,100)
                    print(f"Your random Number is: {num}")
        
         elif inner_user == 2:
                    print(f'f"Your Random List is: {random.sample(range(0,100),10)}')
        
         elif inner_user == 3:
                    import string
                    len  =  int(input("Enter the length of the password: "))
                    char = string.ascii_letters + "123456789" + "!@#$%^&*"
                    password = "".join(random.sample(char, len))
                    print(f"Your Password is: {password}")
        
         elif inner_user == 4:
                    print("Generating OTP: ")
                    otp = "".join(random.sample(string.digits,6))
                    print(f"Your OTP: {otp}")
        
         elif inner_user == 5:
                     print("Going back to the main menu ") 
                     break
         else:
                    print("Invaid input ")