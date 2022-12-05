# Python Wrangling
Copy the password from `pw.txt` and run the script `ende.py` . The script read the text from the file `flag.txt.en` and asks the user to enter the password which will be encoded to base64 string. The encode password will be used as a key to `Fernet` module that implements symmetric encryption and decryption.
```bash
python3 ende.py -d flag.txt.en ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
```
### Flag
>  picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}
