'''
fork.py  进程演示
'''
import  os
from time import sleep
#创建子进程
pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid ==0:
    # 子进程执行部分
    sleep(3)
    print('The new process')
else:
    # 父进程执行部分
    sleep(4)
    print('The old process')
# 父子进程都执行
print('Fork test over')
