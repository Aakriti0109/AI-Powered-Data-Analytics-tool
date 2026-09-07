# 🤖 AI-Powered Data Analytics Platform

An **AI-powered data analytics platform** that allows users to upload CSV datasets, automatically clean and analyze data, assess data quality, generate statistical insights, and interact with the results through a web-based interface.

## 🚀 Key Features

* 📂 **CSV Upload** — Upload and process CSV datasets.
* 🧹 **Automated Data Cleaning** — Handle missing values, duplicates, incorrect data types, and inconsistent data.
* 📊 **Data Quality Assessment** — Identify missing values, duplicates, outliers, and data inconsistencies.
* 🔎 **Dataset Profiling** — Generate dataset summaries, column information, distributions, and descriptive statistics.
* 💡 **Automated Insights** — Discover trends, correlations, patterns, and important findings.
* 🤖 **AI-Assisted Analysis** — Use AI to interpret analytical results in simple language.
* 📈 **Interactive Visualizations** — Explore datasets using charts and graphs.
* 📥 **Cleaned Dataset Download** — Download the processed dataset as a CSV file.
* 🌐 **Web Interface** — Perform the complete analysis through an easy-to-use interface.

## 🛠️ Tech Stack

**Frontend / Interface**

* Streamlit

**Data Analysis**

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

**AI / Machine Learning**

* Generative AI / LLM API
* Scikit-learn

**Data Quality & Profiling**

* Pandas Profiling / YData Profiling
* Custom data-quality checks

## 📁 Project Structure

```text
AI-Data-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── modules/
│   ├── data_cleaning.py
│   ├── data_quality.py
│   ├── profiling.py
│   ├── visualization.py
│   └── ai_insights.py
│
└── assets/
    └── screenshots/
```

## ⚙️ How It Works

```text
Upload CSV
    ↓
Data Validation
    ↓
Data Cleaning & Preprocessing
    ↓
Data Quality Assessment
    ↓
Dataset Profiling
    ↓
Statistical Analysis
    ↓
Visualizations
    ↓
AI-Generated Insights
    ↓
Download Cleaned Dataset
```

## ▶️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Data-Analytics.git
cd AI-Data-Analytics
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

If the project uses an AI API, add your API key through environment variables rather than directly inside the source code.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Example Analysis

The platform can analyse datasets and provide:

* Number of rows and columns
* Missing-value percentage
* Duplicate records
* Numerical and categorical column summaries
* Mean, median, standard deviation, minimum, and maximum
* Outlier detection
* Correlation analysis
* Distribution analysis
* Important trends and patterns
* AI-generated natural-language explanations

## 🎯 Project Goals

The main goal of this project is to make **data analytics faster and accessible to users without requiring extensive programming or statistical knowledge**.

Instead of manually performing every pre-processing and analysis step, users can upload a dataset and receive a complete analytical overview with AI-assisted explanations.

## 🔮 Future Enhancements

* Support for Excel and JSON files
* Natural-language querying of datasets
* Automated machine-learning models
* Predictive analytics
* Automated dashboard generation
* Advanced anomaly detection
* PDF analytical reports
* User authentication
* Cloud deployment
* Multiple AI model support

## 👩‍💻 Author

**Aakriti Singh**

B.Tech. CSE | Data Analytics | AI | Python | SQL

---

⭐ If you find this project useful, consider giving the repository a star!
