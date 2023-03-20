"""
根据父母的身高，预测儿子的身高，其计算公式为：
    儿子身高 = （父亲身高 + 母亲身高） * 0.54
"""
print(" "*15+"身高预测（单位:m）")
f_height = float(input("请输入父亲身高："))
m_height = float(input("请输入母亲身高："))

pre_s_height = (f_height + m_height) * 0.54
print(f"预测儿子的身高为：{pre_s_height}")
