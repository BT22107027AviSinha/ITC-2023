def sort_hyphen_sequence(sequence):
    words = sequence.split('-')  # Split the sequence into individual words
    sorted_words = sorted(words)  # Sort the words alphabetically
    sorted_sequence = '-'.join(sorted_words)  # Join the sorted words with hyphens
    return sorted_sequence

# Example usage
sequence = "green-red-yellow-black-white"
sorted_sequence = sort_hyphen_sequence(sequence)
print("Sorted sequence:", sorted_sequence)
