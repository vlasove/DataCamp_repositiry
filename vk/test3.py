def sentencePalindrome(s): 
    l, h = 0, len(s) - 1
    
    # Lowercase string 
    s = s.lower() 
    
    # Compares character until they are equal 
    while (l <= h): 
    
        # If there is another symbol in left 
        # of sentence 
        if (not(s[l] >= 'а' and s[l] <= 'я') or not(s[l] >= 'a' and s[l] <= 'z') or (s[l] >= 'a' and s[l] <= 'z') or not(s[l] >= '0' and s[l] <= '9') ): 
            l += 1
    
        # If there is another symbol in right  
        # of sentence 
        elif (not(s[h] >= 'а' and s[h] <= 'я')or not(s[h] >= 'a' and s[h] <= 'z') or (s[h] >= 'a' and s[h] <= 'z') or not(s[h] >= '0' and s[h] <= '9') ): 
            h -= 1
    
        # If characters are equal 
        elif (s[l] == s[h]): 
            l += 1
            h -= 1
          
        # If characters are not equal then 
        # sentence is not palindrome 
        else: 
            return False
    # Returns true if sentence is palindrome 
    return True
    
# Driver program to test sentencePalindrome() 

num = int(input())

for i in range(num):
    line = input()
    if (sentencePalindrome(line)): 
        print ("yes")
    else: 
        print ("no")




  
