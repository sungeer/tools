import pandas as pd
import pandera as pa

# 定义 schema
schema = pa.DataFrameSchema({
    "age": pa.Column(pa.Int, pa.Check(lambda x: (x > 0) & (x < 120))),
    "email": pa.Column(pa.String, pa.Check.str_matches(r"[^@]+@[^@]+\.[^@]+"))
})

# 读取 Excel 文件
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 示例数据
df = pd.DataFrame({
    "age": [25, 150, -5, 29],
    "email": ["test@example.com", "bademail", "foo@bar.com", "test2@demo.com"]
})

try:
    schema.validate(df, lazy=True)
except pa.errors.SchemaErrors as err:
    # 获取所有出错的行索引
    failed_indices = err.failure_cases["index"].unique()
    # 只要有一列不合格，整行都提取出来
    failed_rows = df.loc[failed_indices]
    print("不合格的整行数据：")
    print(failed_rows)
