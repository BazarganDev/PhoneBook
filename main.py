# Import "phonebook.py" and relevant modules
import subprocess
import phonebook

# Change font color to green
subprocess.call('color A', shell=True)

# NOTE: In each function, you will see the reference to the "Home" function.
# It's because every time that client is done with the operations, maybe the
# client wants to do another operation. Maybe the client wants to delete some
# numbers right after adding a few numbers or tries to check a number in the phonebook.
# That's why after finishing each operation, the program should go back to the home page :)

# Functionality of each option
def option_1():
    """
    Option for adding multiple numbers.
    This function stores phone numbers inside a list (in this case,
    "given_numbers") and then add them to the phonebook one by one.
    """
    given_numbers = {}
    print("\nEnter numbers you want to add\nPress <Enter> after each phone number")
    print("Enter 'q' to quit")
    while True:
        try:
            contact_name = input("\nContact >>> ")
            if contact_name == 'q':
                break
            number = input("Number >>> ")
            if number == 'q':
                break
            else:
                number = int(number)
        except ValueError:
            print("Please enter a number not a text.\n")
            continue
        else:
            given_numbers[contact_name] = number
    for contact_name, number in given_numbers.items():
        phonebook.AddNumbers(contact_name, number)
    Home()

def option_2():
    """
    Option for deleting multiple numbers.
    This function stores phone numbers inside a list (in this case,
    "given_numbers") and then delete them from the phonebook one by one.
    """
    given_numbers = []
    print("\nEnter numbers you want to delete\nPress <Enter> after each phone number")
    print("Enter 'q' to quit")
    while True:
        try:
            number = input("\nNumber >>> ")
            if number == 'q':
                break
            else:
                #! Please not that the type of the variable "number" must not be changed to <integer>
                #! because in phonebook.py inside the "DeleteNumbers()" function, the number that user entered
                #! (which must be a string) is being searched through the items of list "AllNumbers" (which are strings).
                #! See lines 59 and 64.
                #! Basically, we can't find integers in a string. Right? ;)
                number = int(number)
        except ValueError:
            print("Please enter a number not a text.\n")
            continue
        else:
            number = str(number)
            given_numbers.append(number)
    for number in given_numbers:
        phonebook.DeleteNumbers(number)
    Home()

def option_3():
    """
    Search a specific phone number from the phonebook
    """
    print("\nEnter the contact name or phone number that you're looking for.")
    print("Enter 'q' to quit")
    target_contact = input("\nContact >>> ")
    if target_contact == 'q':
        Home()
    phonebook.SearchNumbers(target_contact)
    Home()

def option_4():
    """
    Option for showing all numbers in the phonebook
    """
    phonebook.ShowNumbers()
    Home()

def option_5():
    """
    Exit program
    """
    exit()

def Home():
    """
    Home page of the program.
    """
    available_options = (1,2,3,4,5)
    while True:
        try:
            selected_option = input("\nSelect an option -> ")
            if selected_option == 'q':
                quit()
            else:
                selected_option = int(selected_option)
        except ValueError:
            print("Please enter the number of the option.\n")
            continue
        else:
            if selected_option not in available_options:
                print("The option is not available.\nTry another one.\n")
                continue
            else:
                break

    if selected_option == 1:
        option_1()
    elif selected_option == 2:
        option_2()
    elif selected_option == 3:
        option_3()
    elif selected_option == 4:
        option_4()
    elif selected_option == 5:
        option_5()

# Program starts from here :)
def Display_Header():
    header = """
    ___________________________________________
    | Welcome!                                 |
    | Simple command-line based phonebook      |
    |_________________   ______________________|
                      \  \                 
                        ^_ _^              
                        (o o)\_________    
                        (_ _)\         )/\/
                          U   ||----W||    
                              ||     ||    

    ### Available options:
        [1] Add a number
        [2] Delete a number
        [3] Search a number
        [4] Show all numbers
        [5] Exit

    """
    print(header)

Display_Header()
Home()
