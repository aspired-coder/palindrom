def rev_words(s):
        word=s.split()
        rev=' '.join(reversed(word))
        return rev
s='hello world!'
print(rev_words(s))
