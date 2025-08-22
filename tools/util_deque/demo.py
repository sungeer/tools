"""限定容量最大10个元素
超过容量会自动丢弃另一侧的元素
append/extend 时丢左侧
appendleft/extendleft 时,在左侧加,丢右侧
"""

from collections import deque

recent = deque(maxlen=10)  # 最多存放 10 个元素

for i in range(15):
    recent.append(i)

print(list(recent))  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
