import os.path  # for checking file existence
import secrets  # for generating random password
import string  # for generating random password and for string operations

from formating import Textcolor  # import Textcolor from formating.py
from functions import encrypt, add, search, delete, backup, start  # import functions from functions.py

os.system('color')
alpha = string.ascii_letters + string.digits


print(Textcolor.HEADER + """\n
 ╔╦╗╦ ╦╔═╗┌┬┐┌─┐┌┐┌┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║║║╚╦╝╠═╝│││├─┤││││││├┤ │ ┬├┤ ├┬┘
 ╩ ╩ ╩ ╩  ┴ ┴┴ ┴┘└┘┘└┘└─┘└─┘└─┘┴└─
""" + Textcolor.ENDC)
start()  # call start function





# Main Menu
while True:  # infinite loop
    try:  # try block to handle exceptions

        #os.system('cls')  # clear all

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

            print(textcolor.BOLD + "\n" * 2, "SEARCH CREDENTIAL \n" + Textcolor.ENDC)
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
                show = search()  # call function with no argument
                show = show.to_markdown(tablefmt="orgtbl", index=False)  # Pretty Print (Dataframe To Markdown)
                print('\n')
                print(show)


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

            show = search(url)  # call fun, to show respective data related to url
            show_md = show.to_markdown(tablefmt="orgtbl", index=False)  # Pretty Print
            print('\n')
            print(show_md)
            print('\n' * 2)

            # multiple credentials found, len = rows
            if (len(show) > 1):
                index = int(input("\n SELECT AN INDEX VALUE & PRESS ENTER : "))
            else:
                index = show.index.values  # take default index
                index = int(index)

            confirmation = input("\n ARE YOU SURE TO DELETE THIS CREDENTIAL? (Y/N): ")

            if confirmation == 'Y' or confirmation == 'y':
                delete(index)  # call fun, to delete respective data
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
