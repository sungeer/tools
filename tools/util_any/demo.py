"""
will
"""

# 判断字符串 "ac" 是否出现在 列表 任意元素的"子串"中
lst = ["foo", "bar", "abc", "xyz"]
target = "ac"

exists = any(target in s for s in lst)
print(exists)  # False 因为没有元素包含 "ac"
