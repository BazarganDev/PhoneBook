# PhoneBook Module
# This file contains every function that can be used in the "main.py" file

# A path to save the file containing phone numbers
phonebook = r"H:\Bazargan_Dev\Programming\Python_Workspace\FunProject\Simple_Phonebook\phone_numbers.txt"

# Define functions
def AddNumbers(contact, number):
    """
    Add a number to the phone book.

    Args:
        number (int): Number that needs to be saved
    """
    print(f"Adding {contact.title()}, {number} to the list...")
    text_format = f" [{contact.title()}] \t................. [{number}]"
    try:
        with open(phonebook, 'a') as phonebook_file:
            phonebook_file.write(text_format)
            phonebook_file.write(",")
    except FileNotFoundError:
        print("Oops! File not found!!!")
    else:
        print("Number has been added successfully :)\n")

def ShowNumbers():
    """
    Show all numbers in the phone book.
    """
    try:
        with open(phonebook, 'r') as phonebook_file:
            AllNumbers = phonebook_file.read()
    except FileNotFoundError:
        print("Oops! File not found!!!")
    else:
        AllNumbers = AllNumbers.split(",")
        print("Phone book:")
        for number in AllNumbers:
            print(f"\t -{number}")

def DeleteNumbers(number):
    """
    Delete a number from the phone book.

    Args:
        number (int): Number that needs to be deleted
    """
    print(f"Deleting {number} from the list...")
    try:
        with open(phonebook, 'r') as phonebook_file:
            AllNumbers = phonebook_file.read()
    except FileNotFoundError:
        print("Oops! File not found!!!")
    else:
        AllNumbers = AllNumbers.split(",")
        # Check the number if it is deleted from the list.
        # If not, then delete it and save the file.
        for n in AllNumbers:
            if number in n:
                AllNumbers.remove(n)
                with open(phonebook, 'w') as phonebook_file:
                    phonebook_file.write(",".join(AllNumbers))
                print("The number has been deleted successfully :)\n")
            else:
                pass

def SearchNumbers(contact):
    """
    Search a number from the phonebook.

    Args:
        contact (str): Phone number or contact name
    """
    try:
        with open(phonebook, 'r') as phonebook_file:
            AllNumbers = phonebook_file.read()
    except FileNotFoundError:
        print("Oops! File not found!!!")
    else:
        # Check the phonebook whether the target contact is saved or not.
        if contact.title() in AllNumbers:
            print("\nFound.\nThe contact is in the phonebook.")
            for n in AllNumbers.split(","):
                if contact.title() in n:
                    print(n)
                else:
                    pass
        else:
            print("\nNot Found!\nThe contact is not in the phonebook.")
