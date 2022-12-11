# Stonks
Reading the source code provided with the challenge give us aa insight of how the program is working. after reading the source code one function `buy_stonks` got my attention for the following reasons:
- It is the only funtions that read the api key from the file
```c
char api_buf[FLAG_BUFFER];
FILE *f = fopen("api","r");
if (!f) {
    printf("Flag file not found. Contact an admin.\n");
	exit(1);
}
fgets(api_buf, FLAG_BUFFER, f);
```
- It accept user input beside `main` functions.
```c
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);

```
The intersting part is the line that print the user_buf.It does not use format string for printing the array `user_buf`. Therefor , it is a format string vulnerability.
### Format string vulnerability:
- Where user input is passed as format string to `printf`, `scanf` and the rest of the family.If we pass `%x` it will print one value at the stack.


## Exploitation 
```bash
pip install nclib
python3 exploit.py
```
`nclib` is used to interact with netcat.
`exploit.py` is well commented, I think.
### Flag : 
> picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}  