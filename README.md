# Econometrics-Practice

这个仓库包含了计量经济学分析和实现的练习代码，主要关注计量经济学方法在能源经济领域的应用。

## 项目概述

本项目系统性地实践了计量经济学的各种方法，包括：

- OLS（普通最小二乘法）
- 2SLS（两阶段最小二乘法）
- GMM（广义矩估计）
- GLS（广义最小二乘法）
- 空间计量经济学方法

## 项目结构

```tree
Econ_Projects/
├── 能源数据分析实践_2025/    # 主要练习代码
│   ├── L1_test.py           # Python 基础测试
│   ├── L2_notebook.ipynb    # Jupyter 基础操作
│   ├── L3a_ols.ipynb       # OLS 方法实现
│   ├── L3b_ols.ipynb       # OLS 方法应用
│   ├── L4a_2sls.ipynb      # 2SLS 方法实现
│   ├── L4b_2sls.ipynb      # 2SLS 方法应用
│   ├── L5a_gmm.ipynb       # GMM 方法实现
│   ├── L5b_gmm.ipynb       # GMM 方法应用
│   ├── L7a_se.ipynb        # 标准误差估计
│   ├── L7b_hw1.ipynb       # 作业1
│   ├── L8a_gls.ipynb       # GLS 方法
│   └── L9_hw1_answer.ipynb # 作业1答案
├── .vscode/                # VS Code 配置
├── .gitignore             # Git 忽略文件
├── LICENSE                # 许可证文件
└── README.md              # 项目说明
```

## 技术栈

### 核心工具
- Python 3.8+
- Jupyter Notebook/Lab

### 主要库
- pandas: 数据处理和分析
- numpy: 数值计算
- statsmodels: 计量经济模型
- scikit-learn: 机器学习工具
- matplotlib/seaborn: 数据可视化

## 学习路径

1. Python 基础 (L1, L2)
2. 线性回归基础 (L3)
3. 工具变量方法 (L4)
4. 广义矩估计 (L5)
5. 标准误差估计 (L7)
6. 广义最小二乘法 (L8)
7. 实践作业 (L7b, L9)

## 使用指南

### 环境配置
```bash
# 创建虚拟环境
conda create -n myenv_econ python=3.8

# 激活环境
conda activate myenv_econ

# 安装依赖
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter

### 运行项目
1. 克隆仓库
```bash
git clone git@github.com:jiqingxxm/Econometrics-Practice.git
 ```
```

2. 进入项目目录
```bash
cd Econometrics-Practice
 ```

3. 按照学习路径顺序运行 notebooks
## 注意事项
- 建议按照学习路径顺序学习
- 确保完成每个部分的练习
- 参考答案前先独立完成作业
## 更新记录
### 2024-01-xx
- 更新了项目结构说明
- 添加了清晰的学习路径
- 详细说明了每个文件的用途
- 优化了环境配置说明
- 添加了学习建议
## 许可证
本项目采用 MIT 许可证。详见 LICENSE 文件。