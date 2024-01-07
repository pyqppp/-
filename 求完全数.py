def find_perfect_number(num):
    divisor_sum = 0
    end = int(num / 2) + 1
    for i in range(1, end):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        return True
    return False

Perfect_number = []
for i in range(2, 10000, 2):
    if find_perfect_number(i):
        Perfect_number.append(i)
    print(i)
with open(mode='w', file='完全数.txt', encoding='utf8') as number:
    number.write(str(Perfect_number))

