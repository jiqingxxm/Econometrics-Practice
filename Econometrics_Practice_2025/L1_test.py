import sys
import platform

print("-" * 50)
print(f"Python 版本信息: {sys.version}")
print(f"Python 环境路径: {sys.executable}")
print(f"操作系统信息: {platform.platform()}")
print(f"Python 实现方式: {platform.python_implementation()}")
print("-" * 50)
