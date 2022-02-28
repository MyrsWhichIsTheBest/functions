def starting_letter(word):
    if word[0] == "A" or "a":
        return True
    else:
        return False


get_word = str(input("What word?"))
print(starting_letter(get_word))
