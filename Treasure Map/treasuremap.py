line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter an entry. (f.e. A3")

index1 = position[0].lower()
liste = ["a","b","c"]
realindex = liste.index(index1)

index2 = int(position[1]) - 1

map[index2][realindex] = "X"

print(f"{line1}\n{line2}\n{line3}")