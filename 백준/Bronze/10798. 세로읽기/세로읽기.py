words = [input() for _ in range(5)]
result = []


max_length = max(len(word) for word in words)

for a in range(max_length):
    for i in range(5):
        if a < len(words[i]):
            print(words[i][a], end='')
