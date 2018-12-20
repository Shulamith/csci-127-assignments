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
print("orppgma","program",canMakeWord("orppgma","program"))

def withWild(letters,word):
    remaining_letters = [];
    for letter in letters:
        remaining_letters.append(letter);
    for letter in word:
        if letter not in remaining_letters and '?' not in remaining_letters:
            return False
        elif letter in remaining_letters:
            remaining_letters.remove(letter)
        else:
            remaining_letters.remove('?')
    return True

print("orppgma?","program",withWild("orppgma?","program"))
print("?????","hello",withWild("?????","hello"))
print("qwert?","teas",withWild("qwert?","teas"))