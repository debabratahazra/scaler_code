''' The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **

ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.'''


def getZigZagString(str, n):
    # if line n is <=1 then return original string
    if n <= 1:
        return str

    # create a str array based on line n size
    zigZagArr = ["" for _ in range(n)]

    row = 0
    down = True

    for i in range(0, len(str)):
        # add ch based on row number
        zigZagArr[row] += str[i]

        # if row number going to end of line, down False
        if row == n - 1:
            down = False
        elif row == 0:
            # if row number going to begin of line, down True
            down = True

        if down:
            # down direction
            row += 1
        else:
            # up direction
            row -= 1

    zigZagStr = ""
    for zStr in zigZagArr:
        zigZagStr += zStr

    # return each row str concat value
    return zigZagStr


sampleStr = "PAYPALISHIRING"
n = 3
print(getZigZagString(sampleStr, n))
