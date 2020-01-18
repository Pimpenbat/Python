def invertKey(aleph_bet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inverted_cipher = ''
    for letter in range(26):
        inverted_letter_pos = aleph_bet.find(alphabet[letter])
        inverted_letter = alphabet[inverted_letter_pos]
        inverted_cipher += inverted_letter
    return inverted_cipher
