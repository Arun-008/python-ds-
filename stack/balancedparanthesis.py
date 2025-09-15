"""s=input().strip()
while ("{}" in s) or ("[]" in s) or ("()" in s):
    s=s.replace("{}","")
    s=s.replace("[]","")
    s=s.replace("()","")
print(len(s)==0)
"""

#another method
"""def is_balanced(expression):
    stack = []
    # Mapping of closing to opening brackets
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)  # push
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()  # pop if matched

    return len(stack) == 0  """# True if no unmatched brackets left


# Test cases
#print(is_balanced("({[]})"))   # ✅ True
#print(is_balanced("((())"))    # ❌ False
#print(is_balanced("{[()]}"))   # ✅ True
#print(is_balanced("(){}{}[]"))   # ❌ False

#USING LINKED LIST
class Node:
    def __init__(self,top):
        self.top=top
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,val):
        newnode=Node(val)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top is None:
            return None
        poped=self.top.top
        self.top=self.top.next
        return poped
    def peek(self):
        return None if self.top is None else self.top.data
    def isempty(self):
        return self.top is None
    
def balancedparanthesis(exp):
    stack=Stack()
    pair={')':'(','}':'{',']':'['}
    for char in exp:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.isempty() or stack.pop()!=pair[char]:
                return False
    return stack.isempty()
exp="({[]})"
print(balancedparanthesis(exp))
