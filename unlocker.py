#!/usr/bin/env python3
# Author raresteak
# This script is for experimentation only
# and this is the partner script to locker.py
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "locker.py" or file == "unlocker.py" or \
      file == ".key" or file == "!evil_message.txt" or os.path.isdir(file):
        continue
    else:
        files.append(file)
if len(files) > 0:
    try:
        keyFh = open('.key', 'rb')
    except FileNotFoundError:
        print("Missing key file")
        exit()
    key = keyFh.read()
    keyFh.close()
    for file in files:
        print("Decrypting: " + file)
        # Read contents of file
        ro_fh = open(file, 'rb')
        encryptedContents = ro_fh.read()
        ro_fh.close()
        # load key
        fernetHandle = Fernet(key)
        # Decrypt file contents
        contents = fernetHandle.decrypt(encryptedContents)
        # create new file name dropping encrypted extension
        fileTuple = os.path.splitext(file)
        delimeter = "."
        newFileName = delimeter.join(fileTuple[:-1])
        # Write the new file
        rw_fh = open(newFileName, 'wb')
        rw_fh.write(contents)
        rw_fh.close()
        # Remove old file
        os.remove(file)
        print("Encrypted: " + newFileName)
    mymessage = "Your files are decrypted, have a nice day."
    print(mymessage)
    os.remove('!evil_message.txt')
    os.remove('.key')
