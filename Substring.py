s = 'abcdefghiabcd'
sb = 'abcd'
results = 0
sub_len = len(sb)

for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print("The count is", results)