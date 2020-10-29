ht = {}
clean_arr = []

def word_count(s):
    # Your code here
    lower_s = s.lower()
    chars = set('":;,.-+=/\|[]{}()*^&')
    s_arr = lower_s.split()
    for word in s_arr:
        #print("word: ", word)
        result = ""
        for char in word:
            #print("char: ", char)            
            if char not in chars:
                result += char
        #print("result: ", result)
        clean_arr.append(result)
    
    for word in clean_arr:
        if word not in ht:
            ht[word] = 0
        ht[word] += 1

    return ht




if __name__ == "__main__":
    #print(word_count(""))
    #print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    #print(word_count('This is a test of the emergency broadcast network. This is only a test.'))