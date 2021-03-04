def reverseInParentheses(s):
    chars = list(s)
    open_bracket_indexes = []
    for i, c in enumerate(chars):
        if c == '(':
            open_bracket_indexes.append(i)
        elif c == ')':
            j = open_bracket_indexes.pop()
            chars[j:i] = chars[i:j:-1]
    if open_bracket_indexes:
        raise ValueError('Unclosed parenthesis')
    return ''.join(c for c in chars if c not in '()')

print(reverseInParentheses("ad(bar(vi)adad)"))