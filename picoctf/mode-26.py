text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
lower_case = [97, 122]
upper_case = [65, 90]
def decipher(cipher : str) -> str:
    deciphered  = ''
    for char in cipher:
        ascii_value = ord(char)
        if  ascii_value >= lower_case[0] and ascii_value <= lower_case[1]:
            d =  ascii_value + 12
            if d >= lower_case[1]:
                pad =  lower_case[0] + (d - lower_case[1])
                de_char = chr(pad)
            else:
               de_char = chr(ascii_value + 13)
        elif ascii_value >= upper_case[0] and ascii_value <= upper_case[1]:
            d =  ascii_value + 12
            if d >= upper_case[1]:
                pad =  upper_case[0] + (d -  upper_case[1])
                de_char = chr(pad)
            else : 
                de_char  = chr(ascii_value + 13)
        else :
            de_char = char

        deciphered = deciphered + de_char
    return deciphered 
            
if __name__ == "__main__":
    print(decipher(text))
    