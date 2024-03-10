import hashlib as hash
import os

import pandas as pd

from formating import *


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


def add(name, dataBase_password, url, salt):
    user_data = {'Url/App name': [url], 'Username': [name],
                 'Password': [dataBase_password], 'Salt': [salt]}  # will save in same order (,) to csv file

    df = pd.DataFrame(user_data)  # pack user data into data frame
    df.to_csv('data.csv', mode='a', header=False, index=False)  # Save to CSV file, append New row

    print(Textcolor.OKGREEN + '\n' * 2 + ' ADDED SUCCESSFULLY' + Textcolor.ENDC)


def generate_salt():
    salt = os.urandom(32)
    return salt


def encrypt(password, salt):
    hash_object = hash.sha256()
    hash_object.update(salt + password.encode())
    dataBase_password = hash_object.hexdigest()
    return dataBase_password


def decrypt(dataBase_password, salt):
    hash_object = hash.sha256()
    hash_object.update(salt + dataBase_password.encode())
    dec_password = hash_object.hexdigest()

    print(f"Decrypted Password: {dec_password}")
    return dec_password


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

        dataBase_password = dfS.loc[index, 'Password']  # go through all the rows of Password column ; get passwords
        salt = dfS.loc[index, 'Salt']  # go through all the rows of Salt column ; get salts
        dec_password = decrypt(dataBase_password, salt)  # decrypt that
        password.append(dec_password)

    dfS = dfS.set_index(index_d)  # set to default/original index for reference
    dfS['Password'] = password  # update password column with decrypted passwords

    return dfS


def create_csv():
    data = {'Url/App name': [], 'Username': [], 'Password': [], 'Salt': []}  # empty value dict
    df = pd.DataFrame(data)  # create new pandas DataFrame
    df.to_csv('data.csv', index=False)  # Write DataFrame to a new CSV file
    print(Textcolor.OKGREEN + "Data file created successfully." + Textcolor.ENDC)


def edit(index, new_name, new_password):
    df = pd.read_csv("data.csv")  # using 0th column (Url) as index

    # Edit row at given 'index'

    df.loc[index, ['Username', 'Password']] = [new_name, new_password]  # replace it with new user data
    df.to_csv('data.csv', index=False)  # save it

    print(Textcolor.OKGREEN + '\n' * 2 + ' EDITED SUCCESSFULLY' + Textcolor.ENDC)


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
    cp = cp + "\Backups\data.csv"  # add FolderName & FileName to obtained path

    if os.path.isdir('Backups') == False:  # If 'BackupMYPmanager' not exists

        os.makedirs('Backups')  # Create one, for back up

    df.to_csv(cp, index=False)  # save a copy of same, cp = path
    os.chdir(dp)  # Restoring the default path
    print(Textcolor.OKGREEN + '\n' * 2 + " BACKUP SUCCESSFULLY CREATED." + Textcolor.ENDC)
