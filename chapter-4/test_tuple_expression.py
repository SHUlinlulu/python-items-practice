"""
测试tuple的Expression,即：元组推导式
"""
import random
old_tuple = ("itheima", "itcast", "baidu", "sina", "shu.edu.cn")
#
generator_1 = (random.randint(10, 100) for i in range(10))
print(f"generator_1 = {generator_1}\ntype of generator_1 is {type(generator_1)}")

# 转化为tuple
tuple_1 = tuple(generator_1)
print(f"生成器转化为元组后:\ntuple_1 = {tuple_1}\ntype of tuple_1 is {type(tuple_1)}")

# 转化为tuple
list_1 = list(generator_1)
print(f"生成器转化为列表后:\nlist_1 = {list_1}\ntype of list_1 is {type(list_1)}")
# -->list_1 = []    type of list_1 is <class 'list'>
# 表明11行generator_1---->tuple_1后，对象已经不存在了----即：生成器对象只能被使用一次，再想使用，必须重新创建
