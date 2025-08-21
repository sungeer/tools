"""
will
"""

# 判断字符串 "ac" 是否出现在 列表 任意元素的"子串"中
lst = ["foo", "bar", "abc", "xyz"]
target = "ac"

exists = any(target in s for s in lst)
print(exists)  # False 因为没有元素包含 "ac"

# 忽略大小写
exists_ci = any(target.lower() in s.lower() for s in lst)

