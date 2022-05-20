# Summary

This is an educational script written in Python to demonstrate encrypting and decrypting files in a directory, acting like ransomware.    


# Usage

Clone Repo.

```
git clone https://github.com/raresteak/python-file-encryption.git
```

Execute locker.py to encrypt files.   This will encrypt files in the same directory.

```
./locker.py
```
## Output
```
$ ./locker.py 
Encrypting: spreadsheet1.ods
Encrypted: spreadsheet1.ods.encrypted
Encrypting: file2.txt
Encrypted: file2.txt.encrypted
Encrypting: spreadsheet2.xlsx
Encrypted: spreadsheet2.xlsx.encrypted
Encrypting: file1.txt
Encrypted: file1.txt.encrypted
Encrypting: document1.odt
Encrypted: document1.odt.encrypted
Encrypting: document2.docx
Encrypted: document2.docx.encrypted
Your files are encrypted, have a nice day.
```

Encrypt key written to 
```
.key
```

Execute unlocker.py to decrypt files.  

```
./unlocker.py
```

## Output
```
$ ./locker.py 
Encrypting: spreadsheet1.ods
Encrypted: spreadsheet1.ods.encrypted
Encrypting: file2.txt
Encrypted: file2.txt.encrypted
Encrypting: spreadsheet2.xlsx
Encrypted: spreadsheet2.xlsx.encrypted
Encrypting: file1.txt
Encrypted: file1.txt.encrypted
Encrypting: document1.odt
Encrypted: document1.odt.encrypted
Encrypting: document2.docx
Encrypted: document2.docx.encrypted
Your files are encrypted, have a nice day.
```



# Disclaimer

This code is provided for educational purposes and testing.  Use at your own risk, I am not responsible for any misuse or mischief. 
