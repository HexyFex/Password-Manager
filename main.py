import hashlib as hash  # for encrypting password
import os  # for clearing screen
import secrets  # for generating random password
import string  # for generating random password and for string operations

import pandas as pd  # for handling csv file

from formating import Textcolor  # import Textcolor from formating.py

os.system('color')

alpha = string.ascii_letters + string.digits


def encrypt(password):
    salt = os.urandom(32)  # Ein neues Salz für jedes Passwort
    hash_object = hash.sha256()
    hash_object.update(salt + password.encode())
    encrypted_pass = hash_object.hexdigest()  # Verschlüsseltes Passwort

    print(Textcolor.OKGREEN + "Password encrypted successfully." + Textcolor.ENDC)
    print(Textcolor.OKGREEN + "Encrypted password: " + encrypted_pass + Textcolor.ENDC)

    return encrypted_pass


def decrypt(encrypted_pass, password):
    pass

# Function to create a csv file
def create_csv():
    data = {'Url/App name': [], 'Username': [], 'Password': []}  # empty value dict
    df = pd.DataFrame(data)  # create new pandas DataFrame
    df.to_csv('data.csv', index=False)  # Write DataFrame to a new CSV file
    print(Textcolor.OKGREEN + "Data file created successfully." + Textcolor.ENDC)


def add(name, encrypted_pass, url):
    user_data = {'Url/App name': [url], 'Username': [name],
        'Password': [encrypted_pass]}  # will save in same order (,) to csv file

    df = pd.DataFrame(user_data)  # pack user data into data frame
    df.to_csv('data.csv', mode='a', header=False, index=False)  # Save to CSV file, append New row

    if df.empty:
        print(Textcolor.FAIL + '\n' * 2 + ' ERROR: NOT ADDED' + Textcolor.ENDC)

    else:
        print(Textcolor.OKGREEN + '\n' * 2 + ' ADDED SUCCESSFULLY' + Textcolor.ENDC)


def search(url):
    if url == "":
        data = pd.read_csv('data.csv')  # read data from csv file
        return data
    else:
        data = pd.read_csv('data.csv')  # read data from csv file
        data = data[data['Url/App name'] == url]  # search data
        return data



def edit():
    pass


def delete():
    pass


print(Textcolor.HEADER + """\n
 ╔╦╗╦ ╦╔═╗┌┬┐┌─┐┌┐┌┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║║║╚╦╝╠═╝│││├─┤││││││├┤ │ ┬├┤ ├┬┘
 ╩ ╩ ╩ ╩  ┴ ┴┴ ┴┘└┘┘└┘└─┘└─┘└─┘┴└─
""" + Textcolor.ENDC)

data_file = os.path.isfile('data.csv')  # check whether data file is there or not

if not data_file:  # if not then, create one
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
while True:  # infinite loop

    try:  # try block to handle exceptions
        print("\n" * 3 + " [01] STORE A PASSWORD\
        \n\n [02] SEARCH CREDENTIAL\
        \n\n [03] EDIT CREDENTIAL\
        \n\n [04] DELETE CREDENTIAL")

        menu_option = int(input("\n" * 3 + " SELECT AN OPTION & PRESS ENTER : "))

        if menu_option == 1:

            os.system('cls')  # clear all

            print(Textcolor.BOLD + "\n" * 2, "ADD NEW CREDENTIAL\n" + Textcolor.ENDC)
            url = input("\n ENTER URL OR APP NAME, YOU WANT TO SAVE: ") # this will be saved as it is
            name = input("\n ENTER NAME/USERNAME, YOU WANT TO SAVE: ") # this will be saved as it is
            password = input("\n ENTER PASSWORD, YOU WANT TO SAVE: ")  # this will be encrypted

            if name == "":
                name = "UNAVAILABLE"
            if password == "GENERATE":  # This will be generate a encrypted password
                print(Textcolor.OKGREEN + "\n Password will be generated... " + Textcolor.ENDC)
                password = "".join(secrets.choice(alpha) for i in range(20))  # for a 20-character password
            if password == "":
                password = "UNAVAILABLE"
            if url == "":
                while (url == ""):
                    print(Textcolor.WARNING + '\n WARNING: PLEASE ENTER A URL OR APP NAME: ' + Textcolor.ENDC)
                    url = input("\n ENTER URL OR APP NAME, YOU WANT TO SAVE: ")

            encrypted_pass = encrypt(password)  # call encrypt function to encrypt password
            add(name, encrypted_pass, url)  # call function to add user data to csv file

        elif menu_option == 2:  # search a credential

            os.system('cls')  # clear all

            print(Textcolor.BOLD + "\n" * 2, "SEARCH CREDENTIAL \n" + Textcolor.ENDC)
            print("\n [01] SEE A SPECIFIC SAVED CREDENTIAL\
                      \n\n [02] SEE ALL SAVED CREDENTIALS")
            sub_option = int(input("\n" * 3 + " SELECT AN OPTION & PRESS ENTER : "))

            if (sub_option == 1):

                url = input("\n ENTER URL OR APP NAME,, YOU WANT TO SEARCH: ")
                show = search(url)  # call function to search/extract user data from csv
                show = show.to_markdown(tablefmt="orgtbl", index=False)  # Pretty Print (Dataframe To Markdown)
                print('\n')
                print(show)

            else:
                pass


        elif menu_option == 3:  # edit a credential
            print(Textcolor.OKGREEN + "Edit a credential" + Textcolor.ENDC)  # update_password()

        elif menu_option == 4:
            print(Textcolor.OKGREEN + "Delete a credential" + Textcolor.ENDC)  # delete_password()


        else:
            print(Textcolor.FAIL + "Invalid choice. Please try again." + Textcolor.ENDC)  # application()

    except:  # all error/any error encountered
        print(Textcolor.FAIL + '\n ERROR: NOT FOUND !' + Textcolor.ENDC)
        print("\n" * 2)
        Continue = input("\n PRESS ENTER TO 'OK' ")
        continue  # skip error , restart the loop ( try: block )

# End of the program
