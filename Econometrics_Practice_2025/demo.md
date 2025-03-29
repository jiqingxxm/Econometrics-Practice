# 十五大损失函数汇总


## 1. 均方误差（Mean Squared Error, MSE）

- **解释**：常用于回归问题，计算预测值与真实值之间误差的平方平均值，对大误差更敏感。
- **公式**：$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true},i} - y_{\text{pred},i})^2$

```python
from sklearn.metrics import mean_squared_error
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]
mse = mean_squared_error(y_true, y_pred)
print("MSE:", mse)
```


## 2. 平均绝对误差（Mean Absolute Error, MAE）

- **解释**：预测值与真实值之间的绝对差的平均值，相较 MSE 更稳健。
- **公式**：$
  \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true},i} - y_{\text{pred},i}|$

```python
from sklearn.metrics import mean_absolute_error
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]
mae = mean_absolute_error(y_true, y_pred)
print("MAE:", mae)
```


## 3. 对数损失（Log Loss / Logistic Loss）

- **解释**：用于二分类，衡量预测概率与真实标签之间的差异。
- **公式**：$
  \text{LogLoss} = -\frac{1}{n} \sum_{i=1}^{n} \left[y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)\right]$

```python
from sklearn.metrics import log_loss
y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.1, 0.8, 0.7]
logloss = log_loss(y_true, y_pred)
print("Log Loss:", logloss)
```


## 4. 交叉熵损失（Cross-Entropy Loss）

- **解释**：适用于多分类问题，衡量真实分布与预测分布的差异，适合 softmax 输出。
- **公式**：$\text{CrossEntropy} = -\sum_{i=1}^{n} y_i \log(\hat{y}_i)$

```python
from sklearn.metrics import log_loss
y_true = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
y_pred = [[0.9, 0.05, 0.05], [0.05, 0.9, 0.05], [0.05, 0.05, 0.9]]
cross_entropy = log_loss(y_true, y_pred)
print("Cross-Entropy Loss:", cross_entropy)
```


## 5. SVM损失（Hinge Loss）

- **解释**：支持向量机常用损失函数，使支持向量远离决策边界。
- **公式**：$
  \text{SVM Loss} = \sum_{i=1}^{n} \max(0, 1 - y_i \hat{y}_i)
  $

```python
import numpy as np
from sklearn.svm import SVC
X = np.array([[3, 3], [4, 3], [1, 1], [2, 1]])
y = np.array([1, 1, -1, -1])
clf = SVC(kernel='linear')
clf.fit(X, y)
print("SVM support vectors:", clf.support_vectors_)
```


## 6. Huber损失（Huber Loss）

- **解释**：结合了 MSE 和 MAE 的优点，小误差用平方，大误差用绝对值，鲁棒性强。

```python
import numpy as np
def huber_loss(y_true, y_pred, delta=1.0):
    error = y_true - y_pred
    return np.where(np.abs(error) <= delta,
                    0.5 * error ** 2,
                    delta * (np.abs(error) - 0.5 * delta))

y_true = np.array([1.5, 2.5, 3.5])
y_pred = np.array([1.0, 2.0, 3.0])
loss = huber_loss(y_true, y_pred)
print("Huber Loss:", loss)
```


## 7. Focal Loss

- **解释**：用于类别不平衡时的分类任务，增强对难分样本的关注。
- **公式**：$
  \text{FocalLoss} = -\alpha (1 - \hat{y})^\gamma \log(\hat{y})
  $

```python
import tensorflow as tf
def focal_loss(y_true, y_pred, alpha=0.25, gamma=2.0):
    epsilon = tf.keras.backend.epsilon()
    y_pred = tf.clip_by_value(y_pred, epsilon, 1.0 - epsilon)
    cross_entropy = -y_true * tf.math.log(y_pred)
    weight = alpha * tf.pow(1 - y_pred, gamma)
    loss = weight * cross_entropy
    return tf.reduce_mean(loss)
```


## 8. KL散度（Kullback-Leibler Divergence）

- **解释**：衡量两个概率分布之间的距离。
- **公式**：$
  KL(P||Q) = \sum_i p(x_i) \log \left( \frac{p(x_i)}{q(x_i)} \right)
  $

```python
import numpy as np
def kl_divergence(p, q):
    return np.sum(p * np.log(p / q))

p = np.array([0.1, 0.4, 0.5])
q = np.array([0.2, 0.2, 0.6])
loss = kl_divergence(p, q)
print("KL Divergence:", loss)
```


## 9. 指数损失（Exponential Loss）

- **解释**：用于 Boosting，如 AdaBoost。
- **公式**：$
  \text{ExponentialLoss} = e^{-y_{\text{true}} \cdot y_{\text{pred}}}
  $

```python
import numpy as np
def exponential_loss(y_true, y_pred):
    return np.mean(np.exp(-y_true * y_pred))

y_true = np.array([1, -1, 1])
y_pred = np.array([0.9, -0.8, 0.7])
loss = exponential_loss(y_true, y_pred)
print("Exponential Loss:", loss)
```


## 10. 余弦相似度损失（Cosine Similarity Loss）

- **解释**：衡量两个向量之间夹角，广泛用于文本分类。
- **公式**：$
  \text{CosineSimilarity} = 1 - \frac{\sum y_i \hat{y}_i}{||y|| \cdot ||\hat{y}||}
  $

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
y_true = np.array([[1, 0, 0]])
y_pred = np.array([[0.9, 0.1, 0]])
loss = 1 - cosine_similarity(y_true, y_pred)
print("Cosine Similarity Loss:", loss)
```


## 11. 最大似然损失（Maximum Likelihood Loss）

- **解释**：用于概率建模，通过最大化似然估计模型参数。

```python
import numpy as np
def max_likelihood_loss(y_true, y_pred):
    return -np.sum(np.log(y_pred) * y_true)

y_true = np.array([1, 0])
y_pred = np.array([0.9, 0.8])
loss = max_likelihood_loss(y_true, y_pred)
print("Maximum Likelihood Loss:", loss)
```


## 12. 多任务损失（Multi-task Loss）

- **解释**：联合多个任务的损失函数。

```python
def multi_task_loss(losses, weights):
    return np.sum([w * l for w, l in zip(weights, losses)])

losses = [0.1, 0.2, 0.3]
weights = [0.5, 1.0, 1.5]
loss = multi_task_loss(losses, weights)
print("Multi-task Loss:", loss)
```


## 13. 汉明损失（Hamming Loss）

- **解释**：用于多标签分类，衡量标签错误率。
- **公式**：$
  \text{Hamming Loss} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}[y_i \neq \hat{y}_i]
  $

```python
from sklearn.metrics import hamming_loss
y_true = [0, 1, 0, 1]
y_pred = [0, 0, 0, 1]
loss = hamming_loss(y_true, y_pred)
print("Hamming Loss:", loss)
```


## 14. 马氏距离损失（Mahalanobis Distance Loss）

- **解释**：考虑特征间协方差关系的距离度量，常用于异常检测。
- **公式**：$
  D(x, \mu) = (x - \mu)^T \Sigma^{-1} (x - \mu)
  $

```python
import numpy as np
from scipy.spatial.distance import mahalanobis

x = np.array([1, 2, 3])
mu = np.array([1, 1, 1])
cov_matrix = np.cov(np.array([[1, 2, 3], [4, 5, 6]]), rowvar=False)
inv_cov_matrix = np.linalg.inv(cov_matrix)

distance = mahalanobis(x, mu, inv_cov_matrix)
print("Mahalanobis Distance:", distance)
```


## 15. 平方对数误差（Squared Logarithmic Error, SLE）

- **解释**：用于目标数值较大但对小误差更敏感的回归任务。
- **公式**：$
  \text{SLE} = \frac{1}{n} \sum_{i=1}^{n} \left[\log(y_i + 1) - \log(\hat{y}_i + 1)\right]^2
  $

```python
import numpy as np
def squared_log_error(y_true, y_pred):
    return np.mean((np.log(y_true + 1) - np.log(y_pred + 1)) ** 2)

y_true = np.array([1.0, 2.0, 3.0])
y_pred = np.array([0.9, 2.1, 3.1])
loss = squared_log_error(y_true, y_pred)
print("Squared Logarithmic Error:", loss)
```
