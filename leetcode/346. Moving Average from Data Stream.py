from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.cur_sum=0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.cur_sum-=self.queue.popleft()
        self.queue.append(val)
        self.cur_sum+=val
        return self.cur_sum / len(self.queue)



# bad solution
# class MovingAverage:
#
#     def __init__(self, size: int):
#         self.size = size
#         self.checked = []
#         self.cur_sum = 0
#
#     def next(self, val: int) -> float:
#
#         if len(self.checked) >= self.size:
#             if self.checked[-self.size] < 0:
#                 self.cur_sum += abs(self.checked[-self.size])
#             else:
#                 self.cur_sum -= self.checked[-self.size]
#         self.cur_sum += val
#         self.checked.append(val)
#
#         if len(self.checked) >= self.size:
#             res = self.cur_sum / self.size
#         else:
#             res = self.cur_sum / len(self.checked)
#
#         return res


check = MovingAverage(2)
assert check.next(-50) == -50.00000
assert check.next(100) == 25.00000
assert check.next(50) == 75.00000


check = MovingAverage(5)
assert check.next(12009) == 12009.00000
assert check.next(1965) == 6987.00000
assert check.next(-940) == 4344.666666666667
assert check.next(-8516) == 1129.50000
assert check.next(-16446) == -2385.60000
assert check.next(7870) == -3213.40000
assert check.next(25545) == 1502.60000
assert check.next(-21028) == -2515.00000
assert check.next(18430) == 2874.20000
assert check.next(-23464) == 1470.60000
