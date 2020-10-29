

def no_dups(s):
    lookup_table = {}
    s_arr = s.split()
    #print("s_arr: ", s_arr)
    for word in s_arr:
        if word not in lookup_table:
            lookup_table[word] = word
    #print("--------> ", " ".join(lookup_table.keys()))
    return " ".join(lookup_table.keys())
    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))