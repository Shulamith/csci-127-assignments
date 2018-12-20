def countPlurals(line):
    count =0;
    words = line.split()
    for word in words:
        if word[len(word)-1] == 's':
            count+=1;
    return count

def notPossesive(line):
    count =0;
    words = line.split()
    for word in words:
        if word[len(word)-1] == 's' and word[len(word)-2] != "'":
            count+=1;
    return count
    


print("monkeys love to eat bananas",countPlurals("monkeys love to eat bananas"))
print("shoes and hats",countPlurals("shoes and hats"))
print("tvs",countPlurals("tvs"))
print("not a plural",countPlurals("not a plural"))
print("Twenty oranges",countPlurals("Twenty oranges"))
print("Mike's and looks look like plurals to prgrm",countPlurals("Mike's and looks look like plurals to prgrm"))

print("\nPosessives:")
print("gorillas gorilla's cats",notPossesive("gorillas gorilla's cats"))
print("monkeys love to eat bananas",notPossesive("monkeys love to eat bananas"))
