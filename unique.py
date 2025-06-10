def first_unique_char(s: str) -> str:
    from collections import Counter
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char

s = "swiss"
print(first_unique_char(s))