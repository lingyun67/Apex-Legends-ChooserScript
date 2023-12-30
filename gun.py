import random
import time

# 定义艺术字标题
title = """
\033[1;36m如果你抽到结果为空投枪和制造器枪，请坚定你的结果\033[0m
     _                     __        __                           
    / \\   _ __   _____  __ \\ \\      / /__  __ _ _ __   ___  _ __  
   / _ \\ | '_ \\ / _ \\ \\/ /  \\ \\ /\\ / / _ \\/ _` | '_ \\ / _ \\| '_ \\ 
  / ___ \\| |_) |  __/>  <    \\ V  V /  __/ (_| | |_) | (_) | | | |
 /_/   \\_\\ .__/ \\___/_/\\_\\    \\_/\\_/ \\___|\\__,_| .__/ \\___/|_| |_|
         |_|                                   |_|                  
"""
print(title)

# 所有游戏武器及其分类
weapons = {
    '突击步枪': ['VK-47平行步枪', '赫姆洛克步枪', 'R-301卡宾枪', '哈沃克步枪', '复仇女神连发突击步枪'],
    '冲锋枪': ['转换者冲锋枪', '猎兽冲锋枪', 'R-99冲锋枪', '电能冲锋枪', 'C.A.R冲锋枪'],
    '轻机枪': ['专注轻机枪', '喷火轻机枪', 'L-star轻机枪', '暴走轻机枪'],
    '神射手': ['G7侦查枪', '30-30杠杆步枪', '三重式狙击枪', '波塞克复合弓'],
    '狙击枪': ['长弓狙击步枪', '充能步枪', '哨兵狙击步枪', '克莱伯（克雷贝尔）狙击枪'],
    '霰弹枪': ['EVA-8霰弹枪', '獒犬霰弹枪', '莫桑比克霰弹枪', '和平捍卫者霰弹枪'],
    '手枪': ['RE-45', 'P2020', '小帮手（辅助手枪）']
}

# 抽取规则1：抽取1种枪械类别，然后直接展示该类别给用户
def rule1():
    category = random.choice(list(weapons.keys()))
    print(f"\033[1;33m已选用抽取规则1，正在抽取武器类别。\033[0m")
    time.sleep(1)
    print(f"\033[1;33m抽取到的武器类别：\033[0m", end="", flush=True)  # end="" prevents a newline, flush=True forces printing
    time.sleep(1)
    print(f"\033[1;33m{category}\033[0m")
    time.sleep(1)
    return category, weapons[category]


# 抽取规则2：在所有武器中抽取3-5个武器展示给用户，要求输出武器是什么种类的
def rule2():
    print("\033[1;33m已选用抽取规则2，直接随机抽取三到五个武器；\033[0m")
    time.sleep(1)
    num_selected = random.randint(3, 5)
    selected_weapons = random.sample([weapon for weapons_list in weapons.values() for weapon in weapons_list], num_selected)
    random.shuffle(selected_weapons)
    return selected_weapons

# 初始化抽取次数计数器
draw_count = 1

while True:
    # 提供规则解释
    if draw_count == 1:
        print("\033[1;37m抽取规则1：抽取1种武器类别，然后直接展示该类别给用户。\033[0m")
        print("\033[1;37m抽取规则2：在所有武器中抽取3-5个武器展示给用户，要求输出武器是什么种类的。\033[0m")

    if draw_count != 1:
        print(f"\033[1;37m当前是第{draw_count}次抽取\033[0m")
    # 更新抽取次数计数器
    draw_count += 1

    # 询问用户使用哪种规则
    rule_type = input("\033[1;37m请选择抽取规则 (1 或 2)，或输入 'exit' 退出程序：\033[0m")

    if rule_type.lower() == 'exit':
        break  # 用户输入 'exit' 时退出循环

    # 根据用户选择执行相应规则
    if rule_type == '1':
        category, selected_weapons = rule1()
        print("\033[1;37m抽取结果：\033[0m")
        for i, weapon in enumerate(selected_weapons):
            print(f"\033[1;34m武器{i + 1}：{weapon}\033[0m")
        time.sleep(1)
    elif rule_type == '2':
        selected_weapons = rule2()
        num_selected = len(selected_weapons)
        print("\033[1;37m抽取结果：\033[0m")
        time.sleep(1)
        print(f"你可以选用的武器有{num_selected}把！")
        time.sleep(1)
        for i, weapon in enumerate(selected_weapons):
            # 根据武器找到对应的类别
            weapon_category = next((category for category, weapons_list in weapons.items() if weapon in weapons_list), None)
            print(f"\033[1;34m武器{i + 1}（{weapon_category}类）：{weapon}\033[0m")
            time.sleep(1)
    else:
        print("\033[1;31m无效的选择，请输入 '1' 或 '2'.\033[0m")

print("\033[1;32m程序结束。\033[0m")
