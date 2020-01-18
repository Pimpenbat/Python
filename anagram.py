from english import ENGLISH_WORDS

def listAnagrams(s):
    s = split(s)
    for word in ENGLISH_WORDS:
        s_new = word
        s_new = split(s_new)
        s_new.sort()
        s.sort()
        if s_new == s:
            print (word)

def split(word): 
    return [char for char in word] 



