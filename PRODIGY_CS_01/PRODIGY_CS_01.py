#!/usr/bin/python3.12

'''simple tool to encrypt/decrypt text using caesar cipher'''

import argparse

def caesar_cipher(text,shift,mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            if mode == 'e':
                result_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'd':
                result_char = chr((ord(char) - base - shift) % 26 + base)
            result += result_char
        else:
            result += char
    return result
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="....SIMPLE SCRIPT TO ENCRYPT DECRYPT USING CAESAR CIPHER ALGHORITHEM.... ",
    usage="""
            python PRODIGY_CS_01.py -m e -s 10 -t "This is part of internship at prodigy_infotech"
            python PRODIGY_CS_01.py -m d -s 10 -t "Drsc sc zkbd yp sxdobxcrsz kd zbynsqi_sxpydomr" 
    """)
    
    # input_text shift encrypt-decrypt
    parser.add_argument("-t","--text",type=str,help="Input text for encypt or decrypt")
    parser.add_argument("-s","--shift",type=int,help="digit to shift")
    parser.add_argument("-m","--mode",type=str,help="mode e/d [e for encrypt/d for decrypt]")

    args = parser.parse_args()

    text=args.text
    shift=args.shift
    mode=args.mode
    if mode:
        print(caesar_cipher(text,shift,mode))
    else:
        print("[!] didn't get anything ! use >> python PRODIGY_CS_01.py -h")