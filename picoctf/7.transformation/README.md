# Transformation
We have an ecrypted flag `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽` that was decrypted with the following code:
```python
ecryoted_flag = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

```
we need to reverse the ecrypthion method.The original key is a comination of ascii characters so we need to traverse all ascii character and reverse the encryption method letter by letter.
```python
import strings
### get all ascii character which are part of the original flag
ascii_letters = string.ascii_letters + string.punctuation + string.digits
enc_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
index = 0
while True:
    for i in ascii_letters:
        for j in ascii_letters:
            # Left shift the ascii valye of i by 8 bits
            first = ord(i) << 8
            second = ord{j}
            charater = chr(first + second)
            if character == enc_flag[index]:
                print(f"{i}{j}")
                index = index + 1

```
```bash
python3 decrypt.py
```
### Flag
> picoCTF{16_bits_inst34d_of_8_d52c6b93}