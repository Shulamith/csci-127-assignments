def encode(string):
    x = 0;
    y =1;
    count = 1;
    encode = []
    while y <len(string):
        if string[x] == string[y]:
            count+=1;
            x+=1;
            y+=1;
        else:
            encode.append([string[x], count]);
            count =1;
            x+=1;
            y+=1;
    encode.append([string[x], count]);
##    if string[len(string) -1] != string[len(string)-2]:
##        encode.append([string[len(string) -1], count]);
    return encode
##        if string[letter] != string [letter+x]:
##            encode.append([string[letter], count]);

print(encode("abbacd"))
print(encode("abcd"))
print(encode("abcdd"))
print(encode("aabbccdd"))
print(encode("aaabbbcccddd"))
print(encode("aaabccd"))
print(encode("abbcd"))
print(encode("abbaaacddaaa"))
print(encode("cbbbbbdee"))
print(encode("abababababcab"))