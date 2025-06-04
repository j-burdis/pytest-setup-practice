# exercise 1
# def say_hello(name):
#     return f"hello {name}"

# Intended output:
#
# > say_hello("kay")
# => "hello kay"

# exercise 2
def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    print(cipher)
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        # corrected this line from:
        # plain_char = cipher[65 - ord(i)]
        # which was returning a negative index
        # this line now reverses the ciphered_char generated in line 17
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    # corrected this line from
    # alphabet = [chr(i + 98) for i in range(1, 26)]
    # which was skipping out 'a' and 'b' from the alphabet list
    # due to the chr and range being slightly wrong
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

# use print statements a lot to show exactly what each line is doing
# printing through loops shows the result of each iteration
