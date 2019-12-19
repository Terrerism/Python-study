"""
수의 시퀸스에서, 3으로도 5로도 나누어 떨어지지 않는 수들의 합을 구하는 프로그램
"""

# 1. 절차형
# 1.1. 엄격한 절차형
result = 0
for n in range(1, 20):
    if n % 5 == 0\
    or n % 7 == 0:
        result += n
print(result)

# 1.2. 파이썬의 OOP를 활용
result = list()
for n in range(1, 20):
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
for n in range(1, 20):
    if n % 5 == 0\
    or n % 7 == 0:
        result.append(n)
print(result.sum())


# 2. 함수형 패러다임

# 2.1. 재귀적 정의
# 마치 점화식과 비슷하다!
def sum_(seq):
    if len(seq) == 0:
        return 0 # 끝나는 조건
    return seq[0] + sum_(seq[1:]) # 재귀 조건


def until(n, filter_func, v):
    if v == n:
        return [] # 끝나는 조건
    if filter_func(v):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n, filter_func, v+1)


print(until(20, lambda  x: x%5 == 0 or x%7 == 0, 0))


# 2.2. 함수형 하이브리드
print(sum(n for n in range(1, 20) if n%5 == 0 or n%7==0))


# 2.3. 함수형 프로그래밍 예
# 제곱근 구하기, Newton-Raphson 알고리즘 이용..
def next_(n, x):
    return (x + n/x) / 2


# 실행할때마다 한단계씩 진행되는 무한함수
def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v


# 오차 이하까지 계산하는 함수
def within(e, iterable):
    def head_tail(e, a, iterable):
        b = next(iterable)
        if abs(a-b) <= e:
            return b
        return head_tail(e, b, iterable)수
    return head_tail(e, next(iterable), iterable)


# 실제 sqrt를 구하는 함
def sqrt(a0, e, n):
    return within(e, repeat(lambda x: next_(n, x), a0))

