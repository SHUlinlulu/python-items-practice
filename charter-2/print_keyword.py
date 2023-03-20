"""
使用keyword module，列举出Python中的所有保留字(Reserved words)
"""
import keyword
print(f"Python中所有保留字:{keyword.kwlist}")
print(f"whether as is or not a reserved word:{keyword.iskeyword('as')}")

