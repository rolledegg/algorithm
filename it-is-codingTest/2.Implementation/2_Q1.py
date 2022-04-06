# 왕실의 나이트 [시뮬레이션]
input_data = input()

row = ord(input_data[0]) - ord('a') + 1
column = int(input_data[1])
'''
alpha = "abcdefgh"
for i in range(8):
    if row == alpha[i]:
        row = i+1
'''
steps = [(2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(-1,2),(1,-2),(-1,-2)]

count = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
        continue
    count += 1

print(count)