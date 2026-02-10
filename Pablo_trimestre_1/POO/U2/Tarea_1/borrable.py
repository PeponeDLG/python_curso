def duplicate_count(text):
    count = len(text) * -1
    for i in text.lower():
        for j in text.lower():
            if j == i:
                count += 1
                
    return count

print(duplicate_count("abca"))
