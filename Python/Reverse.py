def reverse (word):
    
    sign = ''
    for i in word:
        sign = i + sign
    return sign

def isPalindrome (word):
    return word == reverse(word)
    

sana = input("Hello! Insert word:")
print(reverse(sana))
print (isPalindrome(sana))