# Given two numbers nn and mm. Create a two-dimensional array of size (n×m)(n×m) and populate it with the characters
# "." and "*" in a checkerboard pattern. The top left corner should have the character "."
# AS60

nn = int(input("Input number"))
mm = int(input("Input another number"))
c = 0
array = [0] * mm * nn
for i in range(0, mm * nn):
    array[i] = [0] * mm * nn

for y in range(0, len(array)):
    for x in range(0, len(array[y])):
        if x % 2 == 0 and y % 2 == 0:
            array[y][x] = "."
        elif x % 2 != 0 and y % 2 != 0:
            array[y][x] = "."
        else:
            array[y][x] = "*"
    c = c + 1

for a in range(0, len(array)):
    print(array[a])
