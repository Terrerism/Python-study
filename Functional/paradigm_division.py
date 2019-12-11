"""
수의 시퀸스에서, 3으로도 5로도 나누어 떨어지지 않는 수들의 합을 구하는 프로그램
"""

# 1. 절차형
# 1.1. 엄격한 절차형
result = 0
for n in range(1, 10):
    if n % 5 == 0\
    or n % 7 == 0:
        result += n
print(result)

# 1.2. 파이썬의 OOP를 활용
result = list()
for n in range(1, 10):
    if n % 5 == 0\
    or n % 7 == 0:
        result.append(n)
print(sum(result))


# 1.3. 조금 더 그럴듯하게
class SummableList(list):
    def sum(self):
        result = 0
        for value in self.__iter__():
            result += value
        return result


result = SummableList()
for n in range(1, 10):
    if n % 5 == 0\
    or n % 7 == 0:
        result.append(n)
print(result.sum())
