"""Valid Palindrome. See problems/two_pointers/valid_palindrome.md."""


def valid_palindrome(text: str) -> bool:
    """Ignore non-alphanumeric code points and compare with str.lower."""
    left, right = 0, len(text) - 1
    while left < right:
        if not text[left].isalnum():
            left += 1
        elif not text[right].isalnum():
            right -= 1
        elif text[left].lower() != text[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
