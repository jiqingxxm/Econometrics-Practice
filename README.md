# 📊 Econometrics-Practice

> A practical econometrics project focusing on applications in energy economics.  
> 一个聚焦能源经济领域应用的计量经济学实战项目。

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

本仓库收录了计量经济学方法在能源经济领域中的应用实践，涵盖 OLS、2SLS、GMM、GLS 及空间计量等主流方法，并通过 Python 代码系统实现，适合教学与研究参考。

本项目系统性地实践了以下计量经济学方法：

- 普通最小二乘法（OLS）  
- 两阶段最小二乘法（2SLS）  
- 广义矩估计（GMM）  
- 广义最小二乘法（GLS）  
- 空间计量方法（预留拓展）

---

### 🗂 项目结构 / Project Structure

```tree
Econ_Projects/
├── 能源数据分析实践_2025/    # 主要练习代码
│   ├── public/             # 公开发布的内容
│   │   ├── notebooks/     # 练习题目
│   │   └── data/         # 数据集
│   ├── private/           # 私人文件夹（不同步到GitHub）
│   └── [课程文件]          # 按课程编号排序的实践文件
├── .vscode/               # VS Code 配置
├── .gitignore            # Git 忽略文件
├── LICENSE               # 许可证文件
└── README.md             # 项目说明
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

#### 2024-01-xx
- 增加项目结构说明  
- 添加学习路径与各模块介绍  
- 补充安装说明与使用建议

---

### 📄 许可证 / License

本项目采用 MIT 开源许可证。详见 `LICENSE` 文件。  
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## English

### 📌 Project Overview

This repository provides practical implementations of econometric methods with real or simulated energy economics data. It covers:

- Ordinary Least Squares (OLS)  
- Two-Stage Least Squares (2SLS)  
- Generalized Method of Moments (GMM)  
- Generalized Least Squares (GLS)  
- Spatial econometrics (future)

---

### 🗂 Project Structure

(See structure above)

---

### 🧰 Tech Stack

(See table above)

---


### ⚙️ Environment Setup

(See steps above)

---

### 🚀 How to Use

(See instructions above)

---

### 📌 Notes

- Follow the suggested learning path for best results  
- Try solving the exercises independently before checking the solutions  
- All data is based on real or simulated energy economics scenarios

---

### 📝 Changelog

#### 2024-01-xx
- Added project structure and learning path  
- Improved installation instructions  
- Added usage guidance

---

### 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.