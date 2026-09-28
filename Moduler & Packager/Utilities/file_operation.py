import os

def file_menu():
    folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    while True:

        print("""
            File Operation

1. Create a New File
2. Write to a File
3. Read from a File
4. Append to a File
5. Back to Main Menu
""")
        inner_user = int(input("Enter a choice: "))
        
        if inner_user == 1:
                    
                    name = input("Enter a name of a file: ")
                    file_path = os.path.join(folder_path, name)
                    with open(file_path,"x") as f:
                        pass
                    print("File Created Successfully In your Given path")
        
        elif inner_user == 2:
                   
                    name = input("Enter a name of a file: ")
                    file_path = os.path.join(folder_path, name)
                    data = input("Enter your Data here: ")
                    try:
                        with open(file_path,"w") as f:
                            f.write(data)
                        print("Your Data Added Successfully ")
                    except FileNotFoundError as e:
                                    print("File Not Found ") 
        
        elif inner_user == 3:
                   
                    name = input("Enter a name of a file: ")
                    file_path = os.path.join(folder_path, name)
                    try:
                        with open(file_path,"r") as f:
                            data = f.read()
                            print(data)
                    except FileNotFoundError as e:
                        print("File not Found...")
        
        elif inner_user == 4:
                   
                    name = input("Enter a name of a file: ")
                    file_path = os.path.join(folder_path, name)
                    data = input("Enter your Data here: ")
                    try:
                        with open(file_path,"a") as f:
                            f.write(f"\n{data}")
                            print("Your Data Appended Successfully ")
                    except FileNotFoundError as e:
                            print("File not Found...")
        
        elif inner_user == 5:
                    print("Going Back to the Main Menu ")
                    break
        else:
                          print("Invaid input ")