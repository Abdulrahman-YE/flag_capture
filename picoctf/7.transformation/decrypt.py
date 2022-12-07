import string 
#all possiable letters in the flag
ascii_letters = string.ascii_letters + string.punctuation + string.digits
# Encrypted flag
enc_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
# variable to store the decrypted flag
dec_flag = ""
#To access the encrypted flag letter by letter
counter = 0
while True:
    #Try all possiable combination of letters
    for i in ascii_letters:
        for j in ascii_letters:
            # the reverse of how the ecryption done.
            # Get the unicode value of var i and left shift it by 8 bits
            first = ord(i) << 8
            # Get the unicode value of var j
            second = ord(j)
            # Get the character with unicode value of (i + j) unicode values
            char = chr(first + second)
            # if counter reach the end of encrypted flag then we found the decrypted flag
            if(counter >= len(enc_flag)):
                exit(0)
            # see if the character is equal to the character at index counter 
            if char == enc_flag[counter]:
                dec_flag = dec_flag + i + j
                counter = counter + 1
                print(dec_flag)

