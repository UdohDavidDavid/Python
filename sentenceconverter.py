# This program takes in input that contains only letters and reverses the words that are more than five letters long
wq
# This is where the action happenns
def spin_words(sentence):
    words = sentence.split(" ")  # Splits the words and puts them into a list
    # Turns the list of words into a sting so it can be checked later on
    wordstr = "".join(words)
    if wordstr.isalpha():  # Checks if it contains only alphabets
        for word in words:
            # checks if length is hight than five
            if len(word) >= 5:
                words[words.index(word)] = word [::-1] # This bit gets the index of the word and reverses it
        for word in words:
            print(f"{word}", end = " ")  # This turns the words from a list back into a sentence
        #print() # New line to avoid bugs in the terminal
    else:
        # If its not an alphabet prints this message
        print("Type in only letters")

# Call the function
spin_words(input("Type in a sentence\nThis program will reverse any word\nthat is longer than 5 words: "))
