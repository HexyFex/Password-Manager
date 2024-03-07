import os

import pandas as pd

os.system('color')

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class Textcolor:
    # Ansi color codes

    HEADER = '\033[31m'
    OKGREEN = '\033[92m'
    WARNING = '\033[33m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


# Function to create a csv file
def create_csv():
    data = {'Url/App name': [], 'Username': [], 'Password': []}  # empty value dict
    df = pd.DataFrame(data)  # create new pandas DataFrame
    df.to_csv('data.csv', index=False)  # Write DataFrame to a new CSV file


# TODO: Function to store a password
# TODO: Function to retrieve a password
# TODO: Function to update a password
# TODO: Function to delete a password
# TODO: Function to list all passwords
# TODO: Function to encrypt a password
# TODO: Function to decrypt a password
# TODO: Function to generate a random password
# TODO: Function to check the strength of a password


print(Textcolor.HEADER + """\n
 ╔╦╗╦ ╦╔═╗┌┬┐┌─┐┌┐┌┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║║║╚╦╝╠═╝│││├─┤││││││├┤ │ ┬├┤ ├┬┘
 ╩ ╩ ╩ ╩  ┴ ┴┴ ┴┘└┘┘└┘└─┘└─┘└─┘┴└─
""" + Textcolor.ENDC)

data_file = os.path.isfile('data.csv')  # check whether data file is there or not

if data_file == False:  # if not then, create one
    create_csv()  # call function

    # First time instructions:
    print(Textcolor.BOLD + "\n WELCOME TO MY PASSWORD MANAGER" + Textcolor.ENDC)

    print("\n THIS APPLICATION USES A MASTER PASSWORD\
           \n TO ENCRYPT & DECRYPT YOUR DATA.\
           \n USE ANY ALPHANUMERIC PASSWORD (RECOMMENDED)\
           \n AND REMEMBER THAT.\
           \n\n WARNING: IF YOU LOSE YOUR MASTER PASSWORD, THEN YOU\
           \n WILL NOT BE ABLE TO RECOVER YOUR SAVED PASSWORDS.")

    input("\n\n PRESS 'ENTER' TO CONTINUE")

# Application main menu loop
while True:

    try:  # try block to handle exceptions
        print("\n" * 3 + " [01] STORE A PASSWORD\
        \n\n [02] SEARCH CREDENTIAL\
        \n\n [03] EDIT CREDENTIAL\
        \n\n [04] DELETE CREDENTIAL\
        \n\n [05] LIST ALL CREDENTIALS")

        menu_option = int(input("\n" * 3 + " SELECT AN OPTION & PRESS ENTER : "))

        if menu_option == 1:
            print(Textcolor.OKGREEN + "Store a password" + Textcolor.ENDC)  # store_password()

        elif menu_option == 2:
            print(Textcolor.OKGREEN + "Search a credential" + Textcolor.ENDC)  # retrieve_password()

        elif menu_option == 3:
            print(Textcolor.OKGREEN + "Edit a credential" + Textcolor.ENDC)  # update_password()

        elif menu_option == 4:
            print(Textcolor.OKGREEN + "Delete a credential" + Textcolor.ENDC)  # delete_password()

        elif menu_option == 5:
            print(Textcolor.OKGREEN + "List all credentials" + Textcolor.ENDC)  # list_passwords()

        else:
            print(Textcolor.FAIL + "Invalid choice. Please try again." + Textcolor.ENDC)  # application()

    except:  # all error/any error encountered
        print(Textcolor.FAIL + '\n ERROR: NOT FOUND !' + Textcolor.ENDC)
        print("\n" * 2)
        Continue = input("\n PRESS ENTER TO 'OK' ")
        continue  # skip error , restart the loop ( try: block )
