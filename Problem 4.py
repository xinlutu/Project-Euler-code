def isPalindrome (n):
    s = str(n)
    reverseString = ""
    for i in range (len(s) - 1, -1, -1):
        reverseString += s[i]
    return reverseString == s
def findLargestPalindrome():
        palindrome = -1
