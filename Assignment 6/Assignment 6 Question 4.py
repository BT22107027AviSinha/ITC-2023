import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)

    # Convert the sentence to lowercase and remove any punctuation
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    # Check if every letter of the alphabet is present in the sentence
    for letter in alphabet:
        if letter not in sentence:
            return False

    return True

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
