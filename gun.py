# -*- coding: utf-8 -*-
import colorama
colorama.init(autoreset=True)
import sys

# 检查是否有命令行参数传递
if len(sys.argv) < 2:
    print("\033[1;31m请提供一个数字作为参数，或正确从main.py打开文件！\033[0m")
    sys.exit(1)

# 从命令行参数中获取数字
input_number = int(sys.argv[1])

# 在这里使用 input_number 进行进一步的处理
# 例如，你可以将其用作程序的输入或进行其他操作
# print(f"从 main.py 接收到的数字：{input_number}")
# 该数字可能是 1 或是 2

import random
import time

# 所有游戏武器及其分类
weapons = {
    '突击步枪': ['VK-47平行步枪', '赫姆洛克步枪', 'R-301卡宾枪', '哈沃克步枪', '复仇女神连发突击步枪'],
    '冲锋枪': ['转换者冲锋枪', '猎兽冲锋枪', 'R-99冲锋枪', '电能冲锋枪', 'C.A.R冲锋枪'],
    '轻机枪': ['专注轻机枪', '喷火轻机枪', 'L-star轻机枪', '暴走轻机枪'],
    '神射手': ['G7侦查枪', '30-30杠杆步枪', '三重式狙击枪', '波塞克复合弓'],
    '狙击枪': ['长弓狙击步枪', '滋崩（充能步枪）', '哨兵狙击步枪', '克莱伯（克雷贝尔）狙击枪'],
    '霰弹枪': ['EVA-8霰弹枪', '獒犬霰弹枪', '莫桑比克霰弹枪', '和平捍卫者霰弹枪'],
    '手枪': ['RE-45', 'P2020', '小帮手（辅助手枪）']
}

# 抽取规则1：抽取1种枪械类别，然后直接展示该类别给用户
def rule1():
    category = random.choice(list(weapons.keys()))
    print(f"\033[1;33m抽取到的武器类别：\033[0m", end="", flush=True)  # end="" prevents a newline, flush=True forces printing
    time.sleep(1)
    print(f"\033[1;33m{category}\033[0m")
    time.sleep(1)
    return category, weapons[category]


# 抽取规则2：在所有武器中抽取1-5个武器展示给用户，要求输出武器是什么种类的
def rule2():
    num_selected = random.randint(1, 5)
    selected_weapons = random.sample([weapon for weapons_list in weapons.values() for weapon in weapons_list], num_selected)
    random.shuffle(selected_weapons)
    return selected_weapons

# 询问用户使用哪种规则
rule_type = input_number

# 根据用户选择执行相应规则
if rule_type == 1:
    category, selected_weapons = rule1()
    print("\033[1;37m抽取结果：\033[0m")
    for i, weapon in enumerate(selected_weapons):
        print(f"\033[1;34m武器{i + 1}：{weapon}\033[0m")
    time.sleep(1)
elif rule_type == 2:
    selected_weapons = rule2()
    num_selected = len(selected_weapons)
    print("\033[1;37m抽取结果：\033[0m")
    time.sleep(1)
    print(f"恭喜！你可以选用的武器有{num_selected}把！")
    time.sleep(1)
    for i, weapon in enumerate(selected_weapons):
        # 根据武器找到对应的类别
        weapon_category = next((category for category, weapons_list in weapons.items() if weapon in weapons_list), None)
        print(f"\033[1;34m武器{i + 1}（{weapon_category}类）：{weapon}\033[0m")
        time.sleep(1)
else:
    print("\033[1;31m无效的选择，请输入 1 或 2.\033[0m")

#print("\033[1;32m该玩家武器抽取程序结束。\033[0m")
