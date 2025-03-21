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

| 阶段 / Stage          | 文件 / Files             | 内容 / Topics                             |
|------------------------|--------------------------|--------------------------------------------|
| Python 基础            | L1, L2                   | Python 语法与 Notebook 基础                 |
| OLS 方法               | L3a, L3b                 | OLS 理论与实证实现                         |
| 工具变量 / 2SLS        | L4a, L4b                 | 工具变量法与两阶段最小二乘                 |
| GMM 方法               | L5a, L5b                 | 广义矩估计理论与应用                       |
| 标准误差估计           | L7a                      | 鲁棒标准误差推导                           |
| GLS 方法               | L8a                      | 广义最小二乘法建模                         |
| 综合练习               | L7b, L9                  | 作业与参考答案                             |

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
git clone https://github.com/yourusername/Econometrics-Practice.git

# 进入目录 / Enter the project folder
cd Econometrics-Practice

# 启动 Jupyter Notebook / Launch Jupyter
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