# 📊 Python for Econometrics: Theory and Practice

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

- [📊 Python for Econometrics: Theory and Practice](#-python-for-econometrics-theory-and-practice)
  - [🧭 目录 / Table of Contents](#-目录--table-of-contents)
  - [中文](#中文)
    - [📌 项目概览](#-项目概览)
    - [🗂 项目结构](#-项目结构)
    - [🧰 技术栈](#-技术栈)
      - [核心工具](#核心工具)
      - [主要依赖库](#主要依赖库)
    - [⚙️ 环境配置](#️-环境配置)
    - [🚀 使用指南](#-使用指南)
    - [📌 注意事项](#-注意事项)
    - [📝 更新记录](#-更新记录)
      - [2025-03-21](#2025-03-21)
    - [📄 许可证](#-许可证)
  - [English](#english)
    - [📌 Project Overview](#-project-overview)
    - [🗂 Project Structure](#-project-structure)
    - [🧰 Tech Stack](#-tech-stack)
      - [Core Tools](#core-tools)
      - [Main Libraries](#main-libraries)
    - [⚙️ Environment Setup](#️-environment-setup)
    - [🚀 How to Use](#-how-to-use)
    - [📌 Notes](#-notes)
    - [📝 Changelog](#-changelog)
      - [2025-03-21](#2025-03-21-1)
    - [📄 License](#-license)

---

## 中文

### 📌 项目概览

本仓库系统性地实现了计量经济学的基础方法，包括 OLS、2SLS、GMM、GLS 等核心估计方法，并通过 Python 代码进行实现，适合教学与研究参考。

本项目系统性地实践了以下计量经济学方法：

- 普通最小二乘法（OLS）
- 两阶段最小二乘法（2SLS）
- 广义矩估计（GMM）
- 广义最小二乘法（GLS）
- 面板数据方法（预留拓展）

---

### 🗂 项目结构


```tree
Econometrics_Practice/
├── Econometrics_Practice_2025/  # 主要练习代码
│   ├── L1_test.py               # Python 基础测试
│   ├── L2_notebook.ipynb        # Jupyter 基础操作
│   ├── L3_ols.ipynb             # OLS 方法实现与应用
│   ├── L4_2sls.ipynb            # 2SLS 方法实现与应用
│   ├── L5_gmm.ipynb             # GMM 方法实现与应用
│   ├── L6_se.ipynb              # 标准误差估计
│   ├── L7_hw1.ipynb             # 作业1
│   ├── L8_gls.ipynb             # GLS 方法实现与应用
│   └── L9_hw1_answer.ipynb      # GLS 方法实现与应用
├── .gitignore                   # Git 忽略文件
├── LICENSE                      # 许可证文件
└── README.md                    # 项目说明
```
---

### 🧰 技术栈

#### 核心工具
- Python ≥ 3.8
- Jupyter Notebook / Jupyter Lab

#### 主要依赖库

| 库名 / Library      | 用途说明 / Description            |
|---------------------|-----------------------------------|
| pandas              | 数据处理 / Data manipulation      |
| numpy               | 数值计算 / Numerical computing    |
| statsmodels         | 计量经济建模 / Econometric models |
| scikit-learn        | 辅助建模 / ML utilities           |
| matplotlib & seaborn| 可视化 / Visualization            |

---


### ⚙️ 环境配置

建议使用 Conda 虚拟环境进行依赖管理：

```bash
conda create -n myenv_econ python=3.8
conda activate myenv_econ
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter
```

---

### 🚀 使用指南

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

### 📌 注意事项

- 推荐按照学习路径顺序完成练习；
- 作业部分请先独立完成，再查看答案；
- 数据集基于真实或模拟的能源经济情境。

---

### 📝 更新记录

#### 2025-03-25
- 增加项目结构说明
- 添加学习路径与各模块介绍
- 补充安装说明与使用建议

---

### 📄 许可证

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

| Course No.          | Files              | Topics                          |
|---------------------|--------------------|---------------------------------|
| L1 - Python Basics  | L1_test.py         | Python Syntax Testing           |
| L2 - Jupyter Basics | L2_notebook.ipynb  | Jupyter Notebook Operations     |
| L3 - OLS Method     | L3_ols.ipynb       | OLS Implementation              |
| L4 - IV Method      | L4_2sls.ipynb      | 2SLS Implementation             |
| L5 - GMM Method     | L5_gmm.ipynb       | GMM Implementation              |
| L6 - SE Estimation  | L6_se.ipynb        | Robust SE Derivation            |
| L7 - HW1            | L7_hw1.ipynb       | First Assignment                |
| L8 - GLS Method     | L8_gls.ipynb       | GLS Implementation              |
| L9 - HW1 Answer     | L9_hw1_answer.ipynb| First Assignment Answer         |

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

#### 2025-03-25
- Added project structure and learning path
- Improved installation instructions
- Added usage guidance

---

### 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
