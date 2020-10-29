ht = {}
clean_arr = []

def word_count(s):
    # Your code here
    chars = set('":;,.-+=/\|[]{}()*^&')
    word = "a*b^c"
    s_arr = s.split()
    for word in s_arr:
        #print("word: ", word)
        result = ""
        for char in word:
            #print("char: ", char)            
            if char not in chars:
                result += char
        #print("result: ", result)
        clean_arr.append(result)
    return clean_arr




if __name__ == "__main__":
    #print(word_count(""))
    #print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    #print(word_count('This is a test of the emergency broadcast network. This is only a test.'))