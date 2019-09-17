'''
二级子进程处理僵尸
'''
import os
from time import sleep
pid1 = os.fork()

if pid1<0:
    print('Error')
elif pid1==0:

    pid2 = os.fork()
    if pid2 <0:
        print('Error')
    elif pid2 ==0:

        print('Child process:',os.getpid())
    else:
        os._exit(0)

else:
    pid1,status = os.wait()#阻塞等待回收子进程
    print('pid:',pid1)
    print('status:',status)
    while True:#让父进程不退出
        pass