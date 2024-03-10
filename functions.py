import hashlib as hash
import os

import pandas as pd

from formating import Textcolor

def start():
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

def encrypt(password):
    salt = os.urandom(32)  # Ein neues Salz für jedes Passwort
    hash_object = hash.sha256()
    hash_object.update(salt + password.encode())
    encrypted_pass = hash_object.hexdigest()  # Verschlüsseltes Passwort

    return encrypted_pass


def decrypt(find_password):
    # Extract the salt from the encrypted password
    salt = bytes.fromhex(find_password)[:32]

    # Recreate the hash using the provided password and extracted salt
    hash_object = hash.sha256()
    hash_object.update(salt + find_password.encode())
    dec_password = hash_object.hexdigest()

    return dec_password


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
    # Extract form CSV file

    df = pd.read_csv('data.csv')

    # pass a string (word) to search like or related words in dataframe
    dfS = df[df['Url/App name'].str.contains(url, na=False, case=False)]
    dfS.head()  # if on argument were pass (url='') ,then it will fetch entire dataframe

    index_d = dfS.index.values  # take default index

    # Logic/Sontrol str. to decrypt all found passwords

    password = []  # empty list to store decrypted password from for loop data
    dfS = dfS.reset_index()  # make sure indexes pair with number of row

    for index, row in dfS.iterrows():  # iterate over all rows

        find_password = dfS.loc[index, 'Password']  # go through all the rows of Password column ; get passwords
        dec_password = decrypt(find_password)  # decrypt that
        password.append(dec_password)

    dfS = dfS.set_index(index_d)  # set to default/original index for reference
    dfS['Password'] = password  # update password column with decrypted passwords

    return dfS


def edit():
    pass


def delete(index):
    df = pd.read_csv("data.csv")

    # Delete row at given 'index'

    df.drop([index], axis=0, inplace=True)
    df.to_csv('data.csv', index=False)  # save it

    print(Textcolor.OKGREEN + '\n' * 2 + ' DELETED SUCCESSFULLY' + Textcolor.ENDC)


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



