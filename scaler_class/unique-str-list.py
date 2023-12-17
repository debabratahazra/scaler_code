def unique_chars(list_of_words):
    # YOUR CODE GOES HERE
    pass
    ans = []
    for word in list_of_words:
        set_ch = set(word)
        if len(set_ch) == len(word):
            ans.append(word)
    return ans


list_of_words = ['hello', 'world', 'python', 'programming']
ret = unique_chars(list_of_words)
print(ret)
