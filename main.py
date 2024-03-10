import hashlib as hash  # for encrypting password
import os  # for clearing screen
import os.path  # for checking file existence
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

    print(Textcolor.OKGREEN + '\n' * 2 + " PASSWORD ENCRYPTED SUCCESSFULLY." + Textcolor.ENDC)

    return encrypted_pass


def decrypt(password):
    salt = os.urandom(32)  # Ein neues salt für jedes Passwort
    hash_object = hash.sha256()
    hash_object.update(salt + password.encode())
    decrypted_pass = hash_object.hexdigest()  # Verschlüsseltes Passwort

    print(Textcolor.OKGREEN + '\n' * 2 + "PASSWORD DECRYPTED SUCCESSFULLY." + Textcolor.ENDC)

    return decrypted_pass


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

    print(Textcolor.OKGREEN + '\n' * 2 + ' ADDED SUCCESSFULLY' + Textcolor.ENDC)


def search(url=""):
    df = pd.read_csv('data.csv')  # read data from csv file
    if url == "":
        data = pd.read_csv('data.csv')  # read data from csv file
        return data
    else:
        data = pd.read_csv('data.csv')  # read data from csv file
        data = data[data['Url/App name'] == url]  # search data
        return data


def edit():
    pass


def delete(index):
    pass


def backup():
    df = pd.read_csv("data.csv")  # read the orignal file
    dp = os.getcwd()  # get the default path, initial directory
    os.chdir("..")  # change the current working directory, one dir back
    cp = os.getcwd()  # get the current path
    cp = cp + "\MYPmanager_Backup\data.csv"  # add FolderName & FileName to obtained path

    if os.path.isdir('MYPmanager_Backup') == False:  # If 'BackupMYPmanager' not exists

        os.makedirs('MYPmanager_Backup')  # Create one, for back up

    df.to_csv(cp, index=False)  # save a copy of same, cp = path
    os.chdir(dp)  # Restoring the default path
    print(Textcolor.OKGREEN + '\n' * 2 + " BACKUP SUCCESSFULLY CREATED." + Textcolor.ENDC)


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

print('\n\n NOTE: MASTER PASSWORD IS A USER DEFINED VALUE\
       \n NEEDED TO ENCRYPT & DECRYPT DATA CORRECTLY.')

while True:

    try:  # try block to handle exceptions

        os.system('cls')  # clear all

        print("\n" * 3 + " [01] STORE A PASSWORD\
        \n\n [02] SEARCH CREDENTIAL\
        \n\n [03] EDIT CREDENTIAL\
        \n\n [04] DELETE CREDENTIAL")

        menu_option = int(input("\n" * 3 + " SELECT AN OPTION & PRESS ENTER : "))  # input menu option

        if menu_option == 1:

            os.system('cls')  # clear all

            print(Textcolor.BOLD + "\n" * 2, "ADD NEW CREDENTIAL\n" + Textcolor.ENDC)
            url = input("\n ENTER URL OR APP NAME, YOU WANT TO SAVE: ")
            name = input("\n ENTER NAME/USERNAME, YOU WANT TO SAVE: ")
            password = input(
                "\n ENTER PASSWORD, YOU WANT TO SAVE OR TYPE 'GENERATE' TO CREATE A SECURE PASSWORD: ")  # this will be encrypted

            if (name == ''):  # if found empty, replace it by 'Unavailable' label
                name = 'UNAVAILABLE'
            if (password == ''):
                password = 'UNAVAILABLE'
            if (password == "GENERATE"):
                # Generate a random password with secrets module
                password = ''.join(secrets.choice(alpha) for i in range(12))
                print(Textcolor.OKGREEN + '\n' * 2 + " PASSWORD GENERATED SUCCESSFULLY." + Textcolor.ENDC)
            if (url == ''):
                while (url == ''):
                    print(Textcolor.WARNING + '\n WARNING: PLEASE ENTER A URL OR APP NAME: ' + Textcolor.ENDC)
                    url = input("\n ENTER URL OR APP NAME, YOU WANT TO SAVE: ")

            encrypted_pass = encrypt(password)  # call encrypt function to encrypt password
            add(name, encrypted_pass, url)  # call function to add user data



        # search a credential
        elif menu_option == 2:
            os.system('cls')  # clear all

            url = input("\n ENTER URL OR APP NAME, YOU WANT TO SEARCH: ")
            data = search(url)
            data = data.to_markdown(tablefmt="orgtbl", index=False)

            print("\n")
            print(data)


        # edit a credential
        elif menu_option == 3:
            os.system('cls')  # clear all
            print(Textcolor.OKGREEN + " EDIT A CREDENTIAL" + Textcolor.ENDC)
            url = input("\n ENTER URL OR APP NAME, YOU WANT TO DELETE: ")
            data = search(url)
            data = data.to_markdown(tablefmt="orgtbl", index=False)

            print("\n")
            print(data)

        # delete a credential
        elif menu_option == 4:
            os.system('cls')
            print(Textcolor.OKGREEN + " DELETE A CREDENTIAL" + Textcolor.ENDC)
            url = input("\n ENTER URL OR APP NAME, YOU WANT TO DELETE: ")
            data = search(url)
            data = data.to_markdown(tablefmt="orgtbl", index=False)

            print("\n")
            print(data)

            confirmation = input("\n ARE YOU SURE TO DELETE THIS CREDENTIAL? (Y/N): ")

            if confirmation == 'Y':
                delete(url)
            else:
                print(Textcolor.WARNING + " CANCELLED." + Textcolor.ENDC)

        print("\n" * 2)
        Continue = input("\n PRESS ENTER TO 'OK' ")
        backup()  # Back up the changes made

    except:  # all error/any error encountered
        print(Textcolor.FAIL + '\n ERROR: NOT FOUND !' + Textcolor.ENDC)
        print("\n" * 2)
        Continue = input("\n PRESS ENTER TO 'OK' ")
        continue  # skip error , restart the loop ( try: block )

# End of the program
