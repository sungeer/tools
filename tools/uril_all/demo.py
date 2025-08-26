"""all(iterable)
用来判断一个可迭代对象中的所有元素是否都为真
只要有一个元素为假，就返回 False
如果所有元素都为真，返回 True
若可迭代对象为空，all([]) 返回 True（"空的全称量化"为真）
"""

##
# 全为真
all([1, "a", [0]])  # True

# 含有假
all([1, 0, 2])  # False（0 为假）
all(["hello", ""])  # False（空字符串为假）

# 空可迭代
all([])  # True


##
# 检查列表是否没有假值
data = [x is not None for x in items]
if all(data):
    ...

# 组合条件判断
rules = [
    lambda s: len(s) >= 8,
    lambda s: any(c.isdigit() for c in s),
    lambda s: any(c.isupper() for c in s),
]
password_ok = all(rule(pwd) for rule in rules)

# 与生成器表达式配合（惰性、短路）
all(x > 0 for x in numbers)  # 一旦遇到非正数就停止

# 校验子串存在于所有元素中
target = "ac"
ok = all(target in s for s in lst)  # 只有当每个元素都包含 "ac" 才 True

