# 🎯 Topological Anomaly Detection in Retail Sales

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TDA](https://img.shields.io/badge/Topological%20Data%20Analysis-Ripser%2FGiotto--TDA-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview
This project applies **Topological Data Analysis (TDA)** to detect anomalous coordination patterns in Walmart retail sales data. Unlike traditional methods that focus on point outliers, TDA identifies systemic changes in store behavior relationships.

## 🎯 Key Finding: **No Systemic Coordination Anomalies Detected**

### Traditional vs Topological Analysis
| Method | Anomalies Found | Interpretation |
|--------|-----------------|----------------|
| **Z-Score** | 4 weeks | Point outliers in total sales volume |
| **Topological Data Analysis** | 0 weeks | **No evidence of coordinated behavioral shifts** |

### 🔍 The Real Insight
While traditional methods flagged 4 weeks with extreme total sales, topological analysis revealed **no persistent holes or unusual connectivity patterns** in week-to-week sales behavior.

**This means:** The anomalies were isolated volume spikes/drops rather than systemic changes in how stores coordinate with each other.

### ⚠️ disclaimer
to speak the truth, this project's code was written mostly(around 70%) by AI tools, while i understand(and still learning) the core  concepts of **TDA** i can't possibly fully produce such project as a first intiative without any external help,that been said, it was very educative and insightful to walk through the process
## 🛠️ Installation
```bash
git clone https://github.com/kelmnberg/topological-anomaly-detection.git
cd topological-anomaly-detection
pip install -r requirements.txt
