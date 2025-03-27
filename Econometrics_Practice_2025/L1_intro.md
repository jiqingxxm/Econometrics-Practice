# Python 系统环境检查工具


## 1. Python 版本和环境路径

- **解释**：显示当前 Python 版本和可执行文件路径。
- **代码**：

```python
import sys
print(f"Python 版本信息: {sys.version}")
print(f"Python 环境路径: {sys.executable}")
```


## 2. 操作系统信息

- **解释**：获取当前操作系统的详细信息。
- **代码**：

```python
import platform
print(f"操作系统信息: {platform.platform()}")
```


## 3. Python 实现方式

- **解释**：显示当前 Python 的实现方式（如 CPython）。
- **代码**：

```python
import platform
print(f"Python 实现方式: {platform.python_implementation()}")
```


## 4. CPU 架构和处理器信息

- **解释**：获取 CPU 架构和处理器的详细信息。
- **代码**：

```python
import platform
print(f"CPU 架构: {platform.machine()}")
print(f"处理器信息: {platform.processor()}")
```

## 5. 当前工作目录

- **解释**：显示当前的工作目录路径。
- **代码**：

```python
import os
print(f"当前工作目录: {os.getcwd()}")
```


## 6. 完整代码

- **代码**：

```python
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
print(f"当前工作目录: {os.getcwd()}")
print("-" * 50)
```
