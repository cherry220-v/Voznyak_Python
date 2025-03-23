def f(s: str):
    end = []
    words = s.split()
    for word in words:
        if len(word) >= 5:
            end.append(word[::-1])
        else:
            end.append(word)
        
    return " ".join(end)

print(f("Hey fellow warriors"))
print(f("This is a test"))
print(f("This is rehtona test"))