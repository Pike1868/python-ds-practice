def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []
    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0  or stack.pop() != '(':
                return False
    return len(stack) == 0
  
    
    
    
print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print( valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))