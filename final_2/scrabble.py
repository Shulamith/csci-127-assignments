def canMakeWord(letters,word):
    remaining_letters = [];
    for letter in letters:
        remaining_letters.append(letter);
    for letter in word:
        if letter not in remaining_letters:
            return False
        else:
            remaining_letters.remove(letter)
    return True

print("ladilmy","daily",canMakeWord("ladilmy","daily"))
print("hellost","ham",canMakeWord("hellost","ham"))
print("orppgma","prorgram",canMakeWord("orppgma","prorgram"))