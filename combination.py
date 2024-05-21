def combinations(text: list[str], length: int) -> list:
    combination = []
    if length > 0:
        for a,_ in enumerate(text):
            combinations(text, length - 1)
    return combination

result = combinations("ARVIND", 2)
print(result)
