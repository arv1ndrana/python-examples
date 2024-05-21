ASCII = "abcdefghijklmnopqrstuvwxyz"

message = "My name is Arvind Rana."
def rot13(message):
    secret_message = ""
    for alphabet in message:
        if alphabet.lower() in ASCII:
            alphabet_index = ASCII.index(alphabet.lower())
            alphabet_index_rotated = alphabet_index + 13

            if alphabet_index_rotated > (26 - 1):
                alphabet_index_rotated = alphabet_index_rotated - 26
            if alphabet.isupper():
                secret_message += ASCII[alphabet_index_rotated].upper()
            else:
                secret_message += ASCII[alphabet_index_rotated]
        else:
            secret_message += alphabet
    return secret_message

print(rot13(message))
