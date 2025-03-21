# 📊 Python for Econometrics: A Step-by-Step Guide

> A practical tutorial on econometric methods using Python, with step-by-step code and explanations.

> 基于 Python 的计量经济学实战教程，涵盖方法讲解与完整代码演示。

<p align="center">
    <a href="#中文">中文</a> | <a href="#english">English</a>
</p>

<p align="center">
    作者 / Author: 吉庆 (Qing Ji)
</p>

---

## 🧭 目录 / Table of Contents

- [📌 项目概览 / Project Overview](#项目概览--project-overview)
- [🗂 项目结构 / Project Structure](#项目结构--project-structure)
- [🧰 技术栈 / Tech Stack](#技术栈--tech-stack)
- [⚙️ 环境配置 / Environment Setup](#环境配置--environment-setup)
- [🚀 使用指南 / How to Use](#使用指南--how-to-use)
- [📌 注意事项 / Notes](#注意事项--notes)
- [📝 更新记录 / Changelog](#更新记录--changelog)
- [📄 许可证 / License](#许可证--license)

---

## 中文

### 📌 项目概览 / Project Overview

本仓库系统性地实现了计量经济学的基础方法，包括 OLS、2SLS、GMM、GLS 等核心估计方法，并通过 Python 代码进行实现，适合教学与研究参考。

本项目系统性地实践了以下计量经济学方法：

- 普通最小二乘法（OLS）  
- 两阶段最小二乘法（2SLS）  
- 广义矩估计（GMM）  
- 广义最小二乘法（GLS）  
- 面板数据方法（预留拓展）

---

### 🗂 项目结构 / Project Structure


```tree
Econometrics_Practice/
├── Econometrics_Practice_2025/  # 主要练习代码
│   ├── L1_test.py              # Python 基础测试
│   ├── L2_notebook.ipynb       # Jupyter 基础操作
│   ├── L3_ols.ipynb          # OLS 方法实现与应用
│   ├── L4_2sls.ipynb         # 2SLS 方法实现与应用
│   ├── L5_gmm.ipynb          # GMM 方法实现与应用
│   ├── L6_se.ipynb           # 标准误差估计
│   ├── L7_hw1.ipynb          # 作业1
│   └── L8_gls.ipynb          # GLS 方法实现与应用
├── .gitignore                 # Git 忽略文件
├── LICENSE                    # 许可证文件
└── README.md                  # 项目说明
```
---

### 🧰 技术栈 / Tech Stack

#### 核心工具 Core Tools
- Python ≥ 3.8
- Jupyter Notebook / Jupyter Lab

#### 主要依赖库 Main Libraries

| 库名 / Library      | 用途说明 / Description            |
|---------------------|-----------------------------------|
| pandas              | 数据处理 / Data manipulation      |
| numpy               | 数值计算 / Numerical computing    |
| statsmodels         | 计量经济建模 / Econometric models |
| scikit-learn        | 辅助建模 / ML utilities           |
| matplotlib & seaborn| 可视化 / Visualization            |

---


### ⚙️ 环境配置 / Environment Setup

建议使用 Conda 虚拟环境进行依赖管理：

```bash
conda create -n myenv_econ python=3.8
conda activate myenv_econ
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter
```

---

### 🚀 使用指南 / How to Use

```bash
# 克隆仓库 / Clone the repository
git clone git@github.com:jiqingxxm/Econometrics-Practice.git

# 进入目录 / Enter the project folder
cd Econometrics-Practice

# 创建并激活 conda 环境 / Create and activate conda environment
conda create -n myenv_econ python=3.8
conda activate myenv_econ

# 安装依赖 / Install dependencies
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter

# 启动 Jupyter / Launch Jupyter
jupyter notebook
```

---

### 📌 注意事项 / Notes

- 推荐按照学习路径顺序完成练习；
- 作业部分请先独立完成，再查看答案；
- 数据集基于真实或模拟的能源经济情境。

---

### 📝 更新记录 / Changelog

#### 2025-03-21
- 增加项目结构说明  
- 添加学习路径与各模块介绍  
- 补充安装说明与使用建议

---

### 📄 许可证 / License

本项目采用 MIT 开源许可证。详见 `LICENSE` 文件。  

---

## English

### 📌 Project Overview

This repository provides systematic implementations of fundamental econometric methods, including OLS, 2SLS, GMM, GLS, and other core estimation techniques. All implementations are in Python, making it suitable for teaching and research reference.

The project systematically implements the following econometric methods:

- Ordinary Least Squares (OLS)  
- Two-Stage Least Squares (2SLS)  
- Generalized Method of Moments (GMM)  
- Generalized Least Squares (GLS)  
- Panel Data Methods (future)

---

### 🗂 Project Structure

| Course No.           | Files              | Topics                           |
|---------------------|--------------------|---------------------------------|
| L1 - Python Basics  | L1_test.py        | Python Syntax Testing           |
| L2 - Jupyter Basics | L2_notebook.ipynb | Jupyter Notebook Operations     |
| L3 - OLS Method     | L3a_ols.ipynb     | OLS Implementation & Derivation |
|                     | L3b_ols.ipynb     | OLS Empirical Applications     |
| L4 - IV Method      | L4a_2sls.ipynb    | 2SLS Implementation            |
|                     | L4b_2sls.ipynb    | 2SLS Applications             |
| L5 - GMM Method     | L5a_gmm.ipynb     | GMM Implementation             |
|                     | L5b_gmm.ipynb     | GMM Applications              |
| L7 - SE Estimation  | L7a_se.ipynb      | Robust SE Derivation           |
|                     | L7b_hw1.ipynb     | First Assignment              |
| L8 - GLS Method     | L8a_gls.ipynb     | GLS Implementation & Apps      |

---

### 🧰 Tech Stack

#### Core Tools
- Python ≥ 3.8
- Jupyter Notebook / Jupyter Lab

#### Main Libraries

| Library            | Description                    |
|-------------------|--------------------------------|
| pandas            | Data manipulation              |
| numpy             | Numerical computing            |
| statsmodels       | Econometric models            |
| scikit-learn      | ML utilities                  |
| matplotlib/seaborn| Visualization                  |

---

### ⚙️ Environment Setup

We recommend using Conda virtual environment:

```bash
conda create -n myenv_econ python=3.8
conda activate myenv_econ
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter
```

---

### 🚀 How to Use

```bash
# Clone the repository
git clone git@github.com:jiqingxxm/Econometrics-Practice.git

# Enter the project folder
cd Econometrics-Practice

# Create and activate conda environment
conda create -n myenv_econ python=3.8
conda activate myenv_econ

# Install dependencies
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter

# Launch Jupyter
jupyter notebook
```
---

### 📌 Notes

- Follow the suggested learning path for best results  
- Try solving the exercises independently before checking the solutions  
- All data is based on real or simulated energy economics scenarios

---

### 📝 Changelog

#### 2025-03-21
- Added project structure and learning path  
- Improved installation instructions  
- Added usage guidance

---

### 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.