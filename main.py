import time
import psutil
from datetime import datetime

duration = 30  # 总运行时间（秒）
interval = 0.1  # 采样间隔（秒，即100毫秒）

end_time = time.time() + duration

# 初始化CPU使用率计算
psutil.cpu_percent(interval=0.0)

while time.time() < end_time:
    # 获取CPU使用率（会阻塞interval秒）
    cpu_usage = psutil.cpu_percent(interval=interval)
    # 获取内存使用率（GB）
    mem_usage = psutil.virtual_memory().used / (1024 ** 3)

    # 获取带毫秒的当前时间
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    # 写入CPU记录
    with open('cpu.txt', 'a') as f:
        f.write(f'{current_time}, {cpu_usage}\n')

    # 写入内存记录
    with open('mem.txt', 'a') as f:
        f.write(f'{current_time}, {mem_usage}\n')
    print(f'{current_time}, CPU: {cpu_usage}%, MEM: {mem_usage}G')