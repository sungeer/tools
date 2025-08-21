"""any(iterable)
用来判断某个可迭代对象里是否至少有一个元素为真
只要遇到第一个真值就立刻返回 True，否则返回 False
空的可迭代对象直接返回 False
"""

##
# 判断字符串 "ac" 是否出现在 列表 任意元素的"子串"中
lst = ["foo", "bar", "abc", "xyz"]
target = "ac"

exists = any(target in s for s in lst)
print(exists)  # False 因为没有元素包含 "ac"

##
# 忽略大小写
exists_ci = any(target.lower() in s.lower() for s in lst)

##
# 先过滤
lst = ["foo", None, 123, "bacon"]
target = "ac"

exists = any(target in str(s) for s in lst if s is not None)
print(exists)  # True（"bacon" 包含 "ac"）
