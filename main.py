import time
import psutil

i = 0   # 初始
end = 60    # 结束时间

while i < end:
    t = time.localtime()
    cpu_time = '%d:%d:%d' %(t.tm_hour,t.tm_min,t.tm_sec)
    cpu_res = psutil.cpu_percent()
    print(cpu_time,cpu_res)

    with open('cpu.txt','a+') as f:
        f.write('%s, %s \n'%(cpu_time,cpu_res))
    time.sleep(1)
    i += 1