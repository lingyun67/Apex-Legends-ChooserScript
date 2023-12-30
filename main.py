import subprocess
import random
import time

# 初始运行次数
run_count = 0

while True:
    # 每次运行增加计数
    run_count += 1

    # 定义艺术字标题
    title = """
    \033[1;36mApex Legends角色及武器双双抽取之随机数享受者\033[0m
         _                      _                              _     
        / \\   _ __   _____  __ | |    ___  __ _  ___ _ __   __| |___ 
       / _ \\ | '_ \\ / _ \\ \\/ / | |   / _ \\/ _` |/ _ \\ '_ \\ / _` | __|
      / ___ \\| |_) |  __/>  <  | |__|  __/ (_| |  __/ | | | (_| |\\__ \\
     /_/   \\_\\ .__/ \\___/_/\\_\\ |_____\\___|\\__, |\\___|_| |_|\\__,_|___/
             |_|                          |___/                      
    """
    if run_count == 1:
        print(title)

    # 生成包含两个随机数字（1或2）的数组
    random_numbers = [random.randint(1, 2) for _ in range(2)]
    #random_numbers = [1, 2]

    # 打印生成的数组
    print(f"第{run_count}次运行，生成的抽取规则的随机数数组：{random_numbers}")
    time.sleep(1)

    # 将数组的第一个数字作为参数传递给apex.py
    subprocess.run(["python", "apex.py", str(random_numbers[0])])
    time.sleep(1)

    # 提供规则解释
    print(f"\033[1;37m抽取武器将使用规则{random_numbers[1]}\033[0m")
    if random_numbers[1] == 1:
        print("\033[1;37m使用抽取规则1：抽取1种武器类别。\033[0m")
    if random_numbers[1] == 2:
        print("\033[1;37m使用抽取规则2：在所有武器中抽取3-5个武器。\033[0m")
    input("\033[1;37m按下回车以继续抽取武器 \033[0m")

    for player in range(3):
        print(f"\033[1;32m正在抽取玩家{player+1}的武器\033[0m")
        time.sleep(1)
        # 将数组的第二个数字作为参数传递给gun.py
        subprocess.run(["python", "gun.py", str(random_numbers[1])])

    user_input = input("\033[1;37m按下回车以继续下一次抽选，退出输入exit \033[0m")

    if user_input.lower() == 'exit':
        break

    # 在每次运行结束后添加空行，以便在输出中更清晰地分隔每次运行
    print("\n")
