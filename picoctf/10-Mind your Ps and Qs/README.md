# Mind Your Ps and Qs
Given the public key for the encryption
```

n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```
And the encrypted messege
```
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
```
First we need to find the prime factors p and q which n = p * q.  Go to [factordb](http://www.factordb.com/index.php) and put `n` to get the factors p and q.
```
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003
```
Find phi where phi = (p-1) * (q-1)
```
phi = 1311097532562595991877980619849724606783491897137083280307201653693412798558164280
```
Find d where d = e ^ -1 mod phi

```
d = 693529123416505412979446025120625035374876994645029007711823240743237277989774953
```
Find the message m where m = c ^ d mod n

```
m = 13016382529449106065927291425342535437996222135352905256639573959002849415739773
```
Convet long to byte using `Crypto.Utils.numbers.long_to_bytes` will convert m to byte string .

```bash
python3 decrypt.pu
```
- This is the result
```
b'picoCTF{sma11_N_n0_g0od_13686679}'
```

### Flag : 
> picoCTF{sma11_N_n0_g0od_13686679}
