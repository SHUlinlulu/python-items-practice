"""
某学员3门成绩如下：
    课程      分数
    Python    95
    English   92
    C语言      89
要求：1)计算python和C语言课程成绩之差
     2)3门课程的平均分
"""
# 解决方案：二维表格-->字典(dict)存储
stu_score_table = {"Python": 95, "English": 92, "C语言": 89}  # type:dict[str:int]

# 求解问题1
subtraction_python_C = stu_score_table["Python"] - stu_score_table["C语言"]
print(f"Python课程与C语言课程成绩的差值为：{subtraction_python_C}")

# 求解问题2
avg_score = float((stu_score_table["Python"]+stu_score_table["English"]+stu_score_table["C语言"]) / len(stu_score_table))
print(f"该学生3门课程成绩平均分为{avg_score}")
