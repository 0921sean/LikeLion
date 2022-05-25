sentence = input("Enter a sentence: ")
count = sentence.count('A') + sentence.count('a') + sentence.count('E') + sentence.count('e') + sentence.count('I') + sentence.count('i') + sentence.count('O') + sentence.count('o') + sentence.count('U') + sentence.count('u')
if (count == 1):
    print("Your sentence contains " + str(count) + " vowel.")
else:
    print("Your sentence contains " + str(count) + " vowels.")