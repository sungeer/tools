"""密码相关
"""
import secrets


# 随机ID
def generate_random_id(byte_length: int = 16) -> str:
    return secrets.token_hex(byte_length)


if __name__ == '__main__':
    print(generate_random_id())  # 205a1442ff050b1496ae10cc923f4333
