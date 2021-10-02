'''Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"'''


#')((()))'
def longestValidParentheses( s: str) -> int:
    print('s ',s)
    stack = []
    stack.append(-1)
    maxlen = 0

    for i in range(0,len(s)):
        print('--current stack',stack)
        print('char = ',s[i])
        print('i = ',i)
        if s[i] == '(':
            stack.append(i)
            print('stack.append(i)',stack)
        else:
            stack.pop()
            print('stack.pop()',stack)
            if not stack:
                stack.append(i)
                print('stack.append(i) empty',stack)
            else:
                peek = getpeek(stack)
                print('i - peek',i - peek)
                print('currcent maxlen', maxlen)
                maxlen = max(maxlen,i - peek)
        print('stack',stack)                
        print('maxlen',maxlen)
    return maxlen

def getpeek(stack):
    if stack:
        peek = stack[-1]
    else:
        peek = None
    print('peek',peek)
    
    return peek

correctinput = ")))(((()()(((())()))"
fncoutput =longestValidParentheses(correctinput)

exit()
correctinput = "(()"
fncoutput =longestValidParentheses(correctinput)
print('fncoutput',fncoutput)
correctoutput = 2
print('correctoutput',correctoutput)
correctinput = ")()())"
fncoutput =longestValidParentheses(correctinput)
print('fncoutput',fncoutput)
correctoutput = 4
print('correctoutput',correctoutput)
