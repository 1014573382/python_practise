#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/07/02 17:40

# 作用域为同级及以下目录，即只对testcase生效

import os
import signal
import subprocess

import pytest

# autouse=True 自动对所有测试方法生效
@pytest.fixture(scope="class", autouse=True)
def record():
    # 测试过程录屏
    cmd = "scrcpy --record test.mp4"
    # subprocess 模块，Popen方法，参数表示使用shell执行命令，打印标准输出和错误输出
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    # 执行完命令之后通过对该命令的pid触发ctrl+c 信号 去停止录屏
    os.kill(p.pid, signal.CTRL_C_EVENT)