def find_perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        return True
    return False

Perfect_number = []
# 测试函数
for i in range(0, 100000):
    if find_perfect_number(i):
        Perfect_number.append(i)
    print(i)
number = open(mode='w', file='完全数.txt', encoding='utf8')
number.write(str(Perfect_number))
number.close()
