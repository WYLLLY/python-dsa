"""Valid Parentheses. See problems/stack/valid_parentheses.md."""


def valid_parentheses(text: str) -> bool:
    """Recognize properly nested (), [] and {}; reject other characters."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char not in pairs or not stack or stack.pop() != pairs[char]:
            return False
    return not stack
