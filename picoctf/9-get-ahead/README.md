# GET aHEAD
Opening the given URL `http://mercury.picoctf.net:34561` will result in a webpage with 2 buttons that will change the background color of the page. The interesting thing is that each button will use different HTTP METHOD the red button uses `GET` and the blue button uses
`POST`. I literaly tried all method I know `PUT, PATCH,DELETE` but I did not receive the flag. I opened the challenge again and I observed the name of the challenge `GET aHEAD` and I remembered that there is a `HEAD` http method.
### HEAD HTTP METHOD
- This method asks for a response like `GET` method but without the response body. for example , if a url requested with `GET` method will download a file, a `HEAD` request will read its Content-Length header without downloading the file. 
- `HEAD` asks for information about a document , not for the document itself. "Meta data of the document"
 
```bash
curl --head http://mercury.picoctf.net:34561
```
- This is the result
```
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_8f878508}
Content-type: text/html; charset=UTF-8
```

### Flag : 
> picoCTF{r3j3ct_th3_du4l1ty_8f878508}