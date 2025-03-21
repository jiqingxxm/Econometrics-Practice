+++markdown

📊 Econometrics-Practice

本仓库收录了计量经济学方法在能源经济领域中的应用实践，涵盖 OLS、2SLS、GMM、GLS 及空间计量等主流方法，并通过 Python 代码系统实现，适用于教学与科研参考。

⸻

📌 项目概览

本项目系统性地实践了以下计量方法，旨在帮助学习者理解模型背后的数学逻辑及其在能源经济数据中的实际应用：
	•	OLS：普通最小二乘法
	•	2SLS：两阶段最小二乘法
	•	GMM：广义矩估计
	•	GLS：广义最小二乘法
	•	空间计量方法：预留拓展

⸻

🗂 项目结构

Econ_Projects/
├── 能源数据分析实践_2025/       # 主要练习代码
│   ├── L1_test.py              # Python 基础测试
│   ├── L2_notebook.ipynb       # Jupyter Notebook 入门
│   ├── L3a_ols.ipynb           # OLS 理论推导与实现
│   ├── L3b_ols.ipynb           # OLS 实证应用
│   ├── L4a_2sls.ipynb          # 2SLS 理论与实现
│   ├── L4b_2sls.ipynb          # 2SLS 实证应用
│   ├── L5a_gmm.ipynb           # GMM 方法实现
│   ├── L5b_gmm.ipynb           # GMM 应用案例
│   ├── L7a_se.ipynb            # 标准误估计与鲁棒处理
│   ├── L7b_hw1.ipynb           # 综合练习：作业1
│   ├── L8a_gls.ipynb           # GLS 方法实现
│   └── L9_hw1_answer.ipynb     # 作业1参考答案
├── .vscode/                    # VS Code 配置
├── .gitignore                 # Git 忽略配置
├── LICENSE                    # 许可证文件
└── README.md                  # 项目说明文档



⸻

🧰 技术栈

🔧 核心工具
	•	Python ≥ 3.8
	•	Jupyter Notebook / Jupyter Lab

📦 主要依赖库

库名	用途说明
pandas	数据处理与分析
numpy	数值计算
statsmodels	计量经济建模与推断
scikit-learn	辅助建模与评估工具
matplotlib	数据可视化
seaborn	高级统计图形绘制



⸻

📚 学习路径推荐

阶段	对应文件	学习内容
🧩 Python 基础	L1_test.py, L2_notebook.ipynb	Python 语言及 Notebook 基础操作
📈 回归分析基础	L3a_ols.ipynb, L3b_ols.ipynb	OLS 理论与实证实践
🔁 工具变量方法	L4a_2sls.ipynb, L4b_2sls.ipynb	2SLS 模型及工具变量法
⚙️ GMM 方法	L5a_gmm.ipynb, L5b_gmm.ipynb	GMM 推导与案例分析
🧮 标准误估计	L7a_se.ipynb	鲁棒标准误估计与异方差处理
📉 GLS 方法	L8a_gls.ipynb	广义最小二乘法实现
📝 综合练习	L7b_hw1.ipynb, L9_hw1_answer.ipynb	综合作业与参考答案



⸻

⚙️ 环境配置指南

建议使用 Conda 创建独立环境，确保依赖一致性：

# 创建虚拟环境
conda create -n econ_env python=3.8

# 激活环境
conda activate econ_env

# 安装主要依赖
conda install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter



⸻

🚀 运行项目指南

# 1. 克隆项目仓库
git clone git@github.com:jiqingxxm/Econometrics-Practice.git

# 2. 进入项目目录
cd Econometrics-Practice

# 3. 启动 Jupyter Notebook/Lab，开始学习
jupyter notebook

📌 建议顺序学习，并在动手过程中深入理解模型与数据背后的逻辑。

⸻

✅ 注意事项
	•	按照推荐顺序逐步学习，循序渐进；
	•	强烈建议先独立完成作业，再查看参考答案；
	•	所有代码基于 Python 3.8 及主流数据科学库，确保环境一致性；
	•	空间计量方法后续版本将逐步添加，敬请关注。

⸻

📅 更新记录

2024-01-xx
	•	优化项目结构与命名
	•	添加模块化学习路径推荐
	•	增补依赖说明与运行方式
	•	丰富练习与作业参考

⸻

📄 许可证

本项目采用 MIT License 开源协议，详见 LICENSE 文件。

⸻

如果你在使用过程中有任何建议或反馈，欢迎提交 Issue 或 PR！
+++