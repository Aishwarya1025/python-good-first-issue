# Check if a string is a palindrome using the two-pointer approach

def pali(s):
  left,right=0,len(s)-1
  
  while left <= right:
    if s[left]!=s[right]:
      return False
    left+=1
    right-=1

  return True

print(pali("tenet"))   # True
print(pali("goat"))    # False
print(pali("madam"))   # True
print(pali("hello"))   # False
    
