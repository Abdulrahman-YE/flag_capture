# Nice netcat ..
Using netcat to connect to the desired address. Once the connection is successfully made the server will return a list of ascii representation of charaters. I created `nice-netcat.py` to run the command `nc` and get the output remove `\n`  and space characters to get the full flag.
```bash
python3 nice-netcat.py
```
### Flag
> picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}