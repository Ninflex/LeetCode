class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(" ","")
        x = "".join(ch for ch in s if ch.isalnum()).lower()

        reverse = x[::-1]
        print(reverse)
        print(x)
        if x == reverse:
            return True
        else:
            return False
        