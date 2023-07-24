def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    test_case = int(input())
    vowels = "aeiou"
    str_val = []
    for i in range(0, test_case):
        s = input()
        str_val.append(s.lower())

    for j in str_val:
        vowel_count = 0
        consonant_count = 0
        for char in j:
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        print(vowel_count, end=' ')
        print(consonant_count)
    return 0


if __name__ == '__main__':
    main()
