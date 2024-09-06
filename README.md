## Internship At Prodigy Infotech

I'm excited to share the amazing experience I had during my internship at **Prodigy Infotech**.

🔐 **Caesar Cipher-based encryption tool**  
- Learn about cryptography and developed basic encryption tool
  ```bash
    python PRODIGY_CS_01.py -h                         
    usage: 
                python PRODIGY_CS_01.py -m e -s 10 -t "This is part of internship at prodigy_infotech"
                python PRODIGY_CS_01.py -m d -s 10 -t "Drsc sc zkbd yp sxdobxcrsz kd zbynsqi_sxpydomr" 
        
    
    ....SIMPLE SCRIPT TO ENCRYPT DECRYPT USING CAESAR CIPHER ALGHORITHEM....
    
    options:
      -h, --help            show this help message and exit
      -t TEXT, --text TEXT  Input text for encypt or decrypt
      -s SHIFT, --shift SHIFT
                            digit to shift
      -m MODE, --mode MODE  mode e/d [e for encrypt/d for decrypt]
  
  ```
# [Examples]
## To Encrypt data / text
       >> python PRODIGY_CS_01.py -m e -s 10 -t "This is part of internship at prodigy_infotech" 
       << Drsc sc zkbd yp sxdobxcrsz kd zbynsqi_sxpydomr
## TO Decrypt data / text
      >> python PRODIGY_CS_01.py -m d -s 10 -t "Drsc sc zkbd yp sxdobxcrsz kd zbynsqi_sxpydomr" 
      << This is part of internship at prodigy_infotech
          
🖼️ **Image Encryption using Pixel Manipulation**  
- Developed an image encryption tool using pixel manipulation, which gave me practical experience in image processing and secure data handling.
  ``` bash
  python PRODIGY_CS_02.py -h                            
  usage: python PRODIGY_CS_02.py test.png 123 e
  
  Simple image encryption tool using pixel manipulation
  
  positional arguments:
    image_path  Enter image path
    key         Enter your key
    {e,d}       Specify whether to encrypt (e) or decrypt (d) the image.
  
  options:
    -h, --help  show this help message and exit

# [Examples]
## To Encrypt Image
    python PRODIGY_CS_02.py test.png 1234 e
## To Decrypt Image
    python PRODIGY_CS_02.py encrypted_test.png 1234 d

🔑 **Password Complexity Checker**  
- Created a password strength checker,based on password policies
  ```bash
    usage: python PRODIGY_CS_03.py password@123 

    Simple Password Complecity Checker
    
    positional arguments:
        password    Enter Password
    
    options:
        -h, --help  show this help message and exit
  ```
# [Examples]
    >> python PRODIGY_CS_03.py Test@123
    << Password should be at least 12 characters long.
    
    >> python PRODIGY_CS_03.py admin123       
    << Password should be at least 12 characters long.
    << Password must include at least one uppercase letter.
    << Password must include at least one special character.
    << Password is too common. Choose a more unique password.
    
    >> python PRODIGY_CS_03.py TestmeBest@12365
    << Password is strong.
  
⌨️ **Keylogger Development**  
- Built a keylogger using the `pynput` library to monitor and log keystrokes.
    ```bash
    >> python PRODIGY_CS_04.py
    << Press Enter to stop...
        'h'
        h'e'
        e'l'
        l'l'
        l'o'
        oKey.space
         'w'
        w'o'
        o'r'
      >> After pressing ctrl+c it will create keyfile.txt logfile.
    ```
    
🌐 **Packet Sniffer Development**  
- Developed a packet sniffer using the `pyshark` library, which allowed me to analyze IP packets and understand how network traffic can be monitored for security purposes.
```bash
  >> python PRODIGY_CS_05.py    and start attack in next terminal ping -c 20 8.8.8.8
  << Enter the interface to sniff (e.g., eth0): wlan0
    Source IP: 192.168.1.105  Destination IP: 8.8.8.8  Protocol: None
    ICMP Packet: Type=8, Code=0
    Source IP: 8.8.8.8  Destination IP: 192.168.1.105  Protocol: None
    ICMP Packet: Type=0, Code=0