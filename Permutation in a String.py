def find_permutation(str, pattern):
    counts = {}
    for item in pattern:
        times = counts.get(item, 0)
        counts[item] = times + 1
    left, match = 0, 0
    for i in range(0, len(str)):
        if str[i] in counts:
            counts[str[i]] -= 1
            if counts[str[i]] == 0:
                match += 1
                if match == len(counts):
                    return True
        if i - left + 1 == len(pattern):
            if str[left] in counts:
                counts[str[left]] += 1
                if counts[str[left]] == 1:
                    match -= 1
            left += 1

    return False
