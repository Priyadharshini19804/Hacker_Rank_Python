"""

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Input (stdin)
3
{[()]}
{[(])}
{{[[(())]]}}

Expected Output
YES
NO
YES

"""

def isBalanced(s):
    prev_length = -1
    while prev_length != len(s):
        prev_length = len(s)
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    
    if len(s) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    
    inputs = []
    for _ in range(t):
        inputs.append(input())  # Just take the string, no repeat prompt

    for s in inputs:
        result = isBalanced(s)
        print(result)
