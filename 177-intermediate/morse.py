# Morse Dictionary
morse = [
        ".-", # A  
        "-...", # B
        "-.-.", # C
        "-.." , # D
        ".", # E
        "..-.", # F
        "--.", # G
        "....", # H
        "..", # I
        ".---", # J
        "-.-", # K
        ".-..", # L
        "--", # M
        "-.", # N
        "---", # O
        ".--.", # P
        "--.-", # Q
        ".-.", # R
        "...", # S
        "-", # T
        "..--", # U
        "...-", # V
        ".--", # W 
        "-..-", # X
        "-.--", # Y
        "--.." # Z
]

# Ascii Table
ascii = [ 97,98,99,100,101,102,103,104,105,106,107,108,109,110,
111,112,113,114,115,116,117,118,119,120,121,122
]

message = raw_input("Message to translate: ")
message.lower()
translated = ""
for i in range(0, len(message)):
    for j in range(0, 26):
        if (ord(message[i]) == (ascii[j])):
            translated += (morse[j])
print(translated)