import string 

stri = string.ascii_letters + string.punctuation + string.digits
enc_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
flag = ""
counter = 0
while True:
    for i in stri:
        for j in stri:
            first = ord(i) << 8
            second = ord(j)
            char = chr(first + second)
            if(counter >= len(enc_flag)):
                exit(0)
            if char == enc_flag[counter]:
                flag = flag + i + j
                counter = counter + 1
                print(flag)

