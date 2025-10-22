import os,json
from datetime import datetime

class InvalidFileError(Exception):
    '''This class is for Invalid File'''
    pass
class InvalidChoiceError(Exception):
    '''This class is for Invalid Choice'''
    pass
class InvalidNameError(Exception):
    '''This class is for Invalid name'''
    pass

#This fucntion is for bringing old data back.
def init_storage(file_path):
    folder=os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder,exist_ok=True)
    if not os.path.exists(file_path):
        reset_file(file_path)
        return
    try:
        with open(file_path,'r') as f:
            data=json.load(f)
        if not isinstance(data,list):
            reset_file(file_path)
    except json.JSONDecodeError:
        reset_file(file_path)
    
#This function is for validating that the field is not left empty
def validate_non_empty(input_name):
    if input_name.strip() == "":
        raise InvalidNameError("This field cannot be empty")
    return input_name

#This function is for validating choice 
def validate_choice(choice,max_choice):
    try:
        choice=int(choice)
    except ValueError:
        raise InvalidChoiceError("Choice must be a number")
    else:
        if choice<1 or choice>max_choice:
            raise InvalidChoiceError(f"Choice must be between 1-{max_choice}")
        return choice

#This function is for validating files
def validate_file(f):
    if f==[]:
        raise InvalidFileError("File is empty")
    return f

#This function is for displaying entries based on the date
def view_by_date(file_path):
    target_date=input("Enter date (YYYY-MM-DD): ").strip()
    data=[]
    try:
        with open(file_path,"r") as f:
            content=json.load(f)
        validate_file(content)
    except (FileNotFoundError,json.JSONDecodeError,InvalidFileError):
        print("No entries yet")
        return
    count=0
    for entry in content:
        if entry['date'].startswith(target_date):
            data.append(entry)
            count+=1
    if count==0:
        print("No entries on that date\n")
    else:
        display_entries(data)
    
#This function is for displaying the entries
def display_entries(data):
    col1=15
    col2=10
    col3=10
    col4=20
    print("-"*(col1+col2+col3+col4+9))
    print(f"{'Habit'.ljust(col1)} | {'Duration'.ljust(col2)} | {'Emotion'.ljust(col3)} | {'Date'.ljust(col4)}")
    print("-"*(col1+col2+col3+col4+9))
    for entry in data:
        print(f"{entry['habit'].ljust(col1)} | {entry['duration'].ljust(col2)} | {entry['emotion'].ljust(col3)} | {entry['date'].ljust(col4)}")
    print("-"*(col1+col2+col3+col4+9))
    
#This function is for viewing all entries
def view_entry(file_path):
    try:
        with open(file_path,"r") as f:
            data=json.load(f)
        validate_file(data)
        display_entries(data)
    except FileNotFoundError:
        print("No Entries Yet (No file found)")
        return
    except json.JSONDecodeError:
        print("No Entries Yet (File is empty or corrupted)")
        return
    except InvalidFileError:
        print("No Entries Yet")
        return

#This function helps in reseting the file
def reset_file(file_path):
    with open(file_path, "w") as f:
        json.dump([], f, indent=4)

#This function is for adding new entry
def add_entry(file_path):
    habit=validate_non_empty(input("Enter habit: ").title())
    duration=validate_non_empty(input("Enter duration: "))
    emotion=validate_non_empty(input("Enter emotion: ").title())
    try:
        with open(file_path,"r") as f:
            data=json.load(f)
            validate_file(data)
    except (InvalidFileError,FileNotFoundError,json.JSONDecodeError) as e:
        data=[]
    entry={
        "habit": habit,
        "duration": duration,
        "emotion": emotion,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    data.append(entry)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print("Habit added successfully!\n")

#This function is for displaying the menu
def display_menu():
    print("1. Add a habit")
    print("2. View all habits")
    print("3. View habits by date")
    print("4. Exit")

#This is the main function
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "Data")
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "habits.json")
    init_storage(file_path)
    while True:
        max_choice=4
        display_menu()
        try:
            choice=validate_choice(input("Enter your choice: "),max_choice)
        except InvalidChoiceError as e:
            print(e)
        else:
            if choice==1:
                add_entry(file_path)
            elif choice==2:
                view_entry(file_path)
            elif choice==3:
                view_by_date(file_path)
            elif choice==4:
                print("Thank you! for using Digital Habit Tracker")
                break

if __name__=="__main__":
    main()
