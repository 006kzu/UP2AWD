import re
hand = open('regex_sum_2147985.txt')
content = hand.read()
numlist = re.findall('[0-9]+', content)

total = 0
for num in numlist:
    total = total + int(num)

print(total)