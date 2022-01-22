def longestCommonPrefix(strs):
    for i, letter_group in enumerate(zip(*strs)):
        print(set(letter_group))
        print(len(set(letter_group)))
        if len(set(letter_group)) >1:
            return strs[0][:i]
        else:
            print("here")
            return min(strs)


print(longestCommonPrefix(["flower","flower","flowe"]))