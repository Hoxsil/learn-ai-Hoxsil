import matplotlib.pyplot as plt

# ========== 核心两行，放在所有绘图代码最前面 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']   # Windows：黑体；Mac用 ['Songti SC']
plt.rcParams['axes.unicode_minus'] = False     # 解决负号显示方框问题
# ======================================================

# fig, ax = plt.subplots(figsize=(6,3))
# ax.axis('off') # 关闭坐标轴，只保留表格

# 表格数据（包含中文）
cell_data = [
    ["张三", "95", "优秀"],
    ["李四", "82", "良好"],
    ["王五", "59", "不及格"]
]
col_labels = ["姓名", "分数", "评价"]

# # 创建表格
# table = ax.table(
#     cellText=cell_data,
#     colLabels=col_labels,
#     loc="center",
#     cellLoc="center"
# )
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1,1.5)

plt.title("学生成绩表")
plt.show()