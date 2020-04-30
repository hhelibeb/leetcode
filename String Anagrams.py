def find_string_anagrams(str, pattern):
    result_indexes = []
    count = {}
    for char in pattern:
        count[char] = count.get(char, 0) + 1
    left, match = 0, 0
    for right in range(0, len(str)):
        right_char = str[right]
        if right_char in count:
            count[right_char] -= 1
            if count[right_char] == 0:
                match += 1
        if right - left + 1 == len(pattern):
            if match == len(count):
                result_indexes.append(left)
            left_char = str[left]
            if left_char in count:
                count[left_char] += 1
                if count[left_char] == 1:
                    match -= 1
            left += 1

    return result_indexes


print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))
