"""
Python 系统环境检查工具

这个脚本用于检查和显示当前 Python 运行环境的关键信息，包括：
- Python 版本和环境路径
- 操作系统信息
- CPU 架构和处理器信息
- 当前工作目录

"""

import sys
import platform
import os

print("-" * 50)
print(f"Python 版本信息: {sys.version}")
print(f"Python 环境路径: {sys.executable}")
print(f"操作系统信息: {platform.platform()}")
print(f"Python 实现方式: {platform.python_implementation()}")
print(f"CPU 架构: {platform.machine()}")
print(f"处理器信息: {platform.processor()}")

# 获取当前工作目录
print(f"当前工作目录: {os.getcwd()}")
print("-" * 50)
