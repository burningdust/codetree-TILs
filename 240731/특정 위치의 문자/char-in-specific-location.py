word = ["L", "E", "B", "R", "O", "S"]
letter = input()

if letter in word:
    print(word.index(letter))
else:
    print("None")