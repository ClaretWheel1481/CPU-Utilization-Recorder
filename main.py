import time
import psutil
from datetime import datetime

duration = 60  # 总运行时间（秒）
interval = 0.1  # 采样间隔（秒，即100毫秒）

end_time = time.time() + duration

# 初始化CPU使用率计算
psutil.cpu_percent(interval=0.0)

while time.time() < end_time:
    # 获取CPU使用率（会阻塞interval秒）
    cpu_usage = psutil.cpu_percent(interval=interval)

    # 获取带毫秒的当前时间
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    # 写入文件
    with open('cpu.txt', 'a') as f:
        f.write(f'{current_time}, {cpu_usage}\n')