sentence = input("Enter a sentence: ")
words = sentence.split()

longest_word = ""
longest_length = 0

for word in words:
    if len(word) > longest_length:
        longest_word = word
        longest_length = len(word)

print("Longest word:", longest_word)
print("Length of the longest word:", longest_length)
