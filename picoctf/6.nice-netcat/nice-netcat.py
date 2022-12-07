import subprocess



if __name__ == "__main__":
    # Run netcat command and get stout to PIPE
    result = subprocess.run(['nc', 'mercury.picoctf.net', '21135'], stdout=subprocess.PIPE)
    result =  ''.join([chr(int(i)) for i in result.stdout.decode('utf-8').split()])
    print(result)
