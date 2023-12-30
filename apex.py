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

import random
import time

# 所有游戏角色及其分类
characters = {
    '进攻': ['进攻-班加罗尔', '进攻-暴雷', '进攻-艾许', '进攻-疯玛吉', '进攻-弹道'],
    '游击': ['游击-恶灵', '游击-动力小子', '游击-地平线', '游击-探路者', '游击-瓦尔基里', '游击-亡灵'],
    '侦察': ['侦察-寻血猎犬', '侦察-密客', '侦察-希尔', '侦察-万蒂奇'],
    '支援': ['支援-直布罗陀', '支援-命脉', '支援-纽卡斯尔', '支援-罗芭', '支援-幻象', '支援-导线管'],
    '控制': ['控制-侵蚀', '控制-沃特森', '控制-兰伯特', '控制-卡特莉丝']
}

# 抽取规则1：从某一类别中随机抽取3个角色
def rule1():
    category = random.choice(list(characters.keys()))
    print(f"\033[1;33m已选用抽取规则1，正在抽取角色类别。\033[0m")
    time.sleep(1)
    print(f"\033[1;33m抽取到的角色类别：{category}\033[0m")
    time.sleep(1)
    #input("\033[1;37m按下回车以继续抽取角色\033[0m")
    print("\033[1;33m正在随机抽取角色；\033[0m")
    time.sleep(1)
    selected_characters = random.sample(characters[category], 3)
    random.shuffle(selected_characters)
    return category, selected_characters

# 抽取规则2：直接随机抽取3个角色
def rule2():
    print("\033[1;33m已选用抽取规则2，直接随机抽取三个角色；\033[0m")
    time.sleep(1)
    selected_characters = random.sample([char for chars in characters.values() for char in chars], 3)
    random.shuffle(selected_characters)
    return selected_characters

# 提供规则解释
print(f"\033[1;37m抽取传奇将使用规则{input_number}\033[0m")
if input_number == 1:
    print("\033[1;37m使用抽取规则1：从某一类别中随机抽取3个角色。\033[0m")
if input_number == 2:
    print("\033[1;37m使用抽取规则2：直接随机抽取3个角色。\033[0m")

time.sleep(1)

# 使用哪种规则
rule_type = input_number

# 根据用户选择执行相应规则
if rule_type == 1:
    category, selected_characters = rule1()
    print("\033[1;37m抽取结果：\033[0m")
    for i, player in enumerate(['玩家1', '玩家2', '玩家3']):
        time.sleep(1)
        print(f"\033[1;34m{player}：{selected_characters[i]}\033[0m")
elif rule_type == 2:
    selected_characters = rule2()
    print("\033[1;37m抽取结果：\033[0m")
    for i, player in enumerate(['玩家1', '玩家2', '玩家3']):
        time.sleep(1)
        print(f"\033[1;34m{player}：{selected_characters[i]}\033[0m")
else:
    print("\033[1;31m无效的选择，请输入 1'或 2.\033[0m")

time.sleep(1)
#input("\033[1;37m按下回车以继续，或输入 'exit' 退出程序：\033[0m")

print("\033[1;32m传奇抽取结束。\033[0m")
