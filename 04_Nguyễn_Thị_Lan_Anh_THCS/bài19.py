d = {'An': 8, 'Bình': 9, 'Chi': 8}
result = {}

for name in d:
    score = d[name]
    if score not in result:
        result[score] = [name]
    else:
        result[score].append(name)

print(result)