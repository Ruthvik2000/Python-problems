class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left={'(','[','{'}
        stack=[]
        for i in s:
            if i in left:
                stack.append(i)
            elif i==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False 
            elif i==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False 
        if len(stack)==0:
            return True
        else:
            return False
            
"""
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
