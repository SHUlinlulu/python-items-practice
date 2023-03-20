"""
假设某超市因为找零钱麻烦，特设抹零行为。请设计一段Python代码，实现该功能。
"""
# 思路：累加所有商品金额-->输出应收金额-->通过int(x)实现抹零-->最后给出真正实收金额
cart_changes = {25.59, 14.99, 28.88, 19.90, 6.49, 9.99}  # 购物车中各商品标价金额
all_changes = 0
for change in cart_changes:
    all_changes += change

print(f"商品总金额：{all_changes}")
real_changes = int(all_changes)  # 实现“抹零”操作
print(f"购物实收金额：{real_changes}")

