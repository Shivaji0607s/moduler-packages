import uuid


def uuid_menu():

    while True:
        print("""
       Generate Unique Identifiers

1. Generate Version 4 UUID (Random)
2. Generate Multiple UUIDs
3. Back to Main Menu
""")
        inner_user = int(input("Enter your Choice: "))
        
        if inner_user == 1:
                    unique_id = uuid.uuid4()
                    print(f"Generated UUID: {unique_id}")
        
        elif inner_user == 2:
                    count = int(input("How many UUIDs do you want to generate? "))
                    print("\nGenerated UUIDs:")
                    for i in range(count):
                        print(f"{i + 1}. {uuid.uuid4()}")
        
        elif inner_user == 3:
                    print("Going Back to Main Menu...")
                    break
        
        else:
                    print("Invalid Choice!")
                    break