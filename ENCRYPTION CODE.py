#ENCRYPTION BY RAMA TAANI
import string

def rot13_char(c):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + 13) % 26 + base)
    return c

def rot5_digit(c):
    if c.isdigit():
        return str((int(c) + 5) % 10)
    return c

def symbol_rot5(c):
    if not c.isalnum():
        code = ord(c)
        new_code = (code + 5) % 256
        return chr(new_code)
    return c

def transform(text):
    result = []
    for ch in text:
        if ch.isalpha():
            result.append(rot13_char(ch))
        elif ch.isdigit():
            result.append(rot5_digit(ch))
        else:
            result.append(symbol_rot5(ch))
    return ''.join(result)

# Modified: Ask user for input instead of using a fixed statement
statement = input("Enter text to encrypt: ")
encrypted = transform(statement)
decrypted = transform(encrypted)


print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
