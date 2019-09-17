
import  os
import signal
#信号处理僵尸
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#创建子进程
pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid ==0:
    # 子进程执行部分

    print('Child process:',os.getpid())
else:
    # 父进程执行部分

    print('Get process',pid)
# 父子进程都执行
print('Fork test over')
