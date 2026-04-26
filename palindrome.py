def is_palindrome(s: str) -> bool:
    normalized = s.replace(' ', '').casefold()
    return normalized == normalized[::-1]
