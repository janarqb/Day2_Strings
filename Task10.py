sentence = "If I don't get it this time I quit"
space_count = 0 
for character in sentence:
    if character == " ":
        space_count = space_count + 1
number_of_words = space_count + 1
print(number_of_words)