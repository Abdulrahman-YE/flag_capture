# Information
This challeng took me time to find the flag becuase I did hex dump the img and read the dumped text to find the flag.Long story short, Use `exiftool` to extract the image information all seems good but the license is a bit confusing `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` it looks like a base64 encoded string. Use `base64 -d` to decode the string to see if its really a base64 encoded string.
```bash
echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d 
```
We find the flag.
### Flag
>  picoCTF{the_m3tadata_1s_modified}

