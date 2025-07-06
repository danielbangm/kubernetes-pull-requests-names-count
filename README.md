
# 🔍 Kubernetes PR Analyzer  
This is a Python automation project that retrieves and analyzes pull request (PR) activity from the Kubernetes GitHub repository in real-time.

## 🧠 Why This Project?
Tracking contributor activity on major open source repositories like Kubernetes can be time-consuming. This tool automates that process, providing quick insights into pull requests without manually browsing GitHub.

Perfect for:
- Open source enthusiasts
- DevOps engineers monitoring upstream activity
- Contribution dashboards

---

## ⚙️ Features

- Fetches real-time PRs from the Kubernetes repo
- Filters by PR state (`open`, `closed`, or `all`)
- Displays author, title, and PR number
- Ready for CLI or API expansion
- Clean and modular code structure

---

## 🚀 Quick Start

### 1. Clone Repository
- git clone "https://github.com/danielbangm/kubernetes-pull-requests-names-count.git"
- cd kubernetes-pull-requests-names-count.git

---

### 2. Install Dependencies
pip install requests

---

### 3. Set up GitHub API access
You can easily obtain that API by searching "GitHub api pull requests" on google.com (CHECK THE PYTHON CODE (pull.py) in my repository)

---

### 4. Run the script
python pull.py

