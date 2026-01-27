import string
def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    words = sentence.split()
    word_count = len(words)
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return word_count, frequency
sentence = "This is a sample sentence, with a few repeated words. This sentence is a test."
count, freq = word_frequency(sentence)
print("Word Count:", count)
print("Word Frequency:", freq)
sentence2 = "One, two, three! One, two, three. Look at me."
count2, freq2 = word_frequency(sentence2)
print("\nWord Count:", count2)
print("Word Frequency:", freq2)
