class Solution(object):
    def isValid(self, s):
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0
        