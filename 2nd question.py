def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    words = sentence.lower().split()
    # Create a dictionary to hold word counts
    frequency = {}
    
    for word in words:
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        # Count the frequency of each word
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

