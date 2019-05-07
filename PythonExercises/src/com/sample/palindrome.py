def isPalindrome(string):
    s1 = string
    s2 = string[::-1]
    #print(s1)
    #print(s2)
    print(s1.lower() == s2.lower()) 


isPalindrome('TEST')
isPalindrome('Dad')
