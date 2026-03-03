# 🔍 Job Listing Scraper

A Python tool that automatically scrapes and filters remote tech job listings from the web, and exports the results to a CSV file for easy viewing.

---

## 📌 Features

- Fetches live job listings using the Remotive public API
- Filters jobs by customizable keywords (e.g. "intern", "junior", "entry level")
- Searches across multiple job categories (e.g. software development, data)
- Removes duplicate listings automatically
- Exports results to a clean `jobs.csv` file
- Prints a formatted summary directly in the terminal

---

## 🛠️ Tech Stack

- **Python 3**
- **Requests** — HTTP calls to the Remotive API
- **CSV** — built-in Python module for exporting data

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/fatasduckling/job-listing-scraper.git
cd job-listing-scraper
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the scraper
```bash
python job_scraper.py
```

---

## ⚙️ Configuration

Edit the config block at the top of `job_scraper.py` to customize your search:

```python
KEYWORDS   = ["intern", "junior", "entry level"]  # job title keywords to filter by
CATEGORIES = ["software-dev", "data"]             # job categories to search
OUTPUT_CSV = "jobs.csv"                           # output file name
```

### Available Categories
`software-dev` · `data` · `devops` · `design` · `product` · `finance` · `marketing` · `writing`

---

## 📄 Example Output

```
============================================================
  🎯 12 matching jobs found
============================================================

📌 Software Engineering Intern
   🏢 Acme Corp
   📍 Worldwide
   📅 2026-02-28
   🔗 https://remotive.com/remote-jobs/...
```

Results are also saved to `jobs.csv`, which can be opened in Excel or Google Sheets.

---

## 📁 Project Structure

```
job-listing-scraper/
├── job_scraper.py   # main scraper script
├── jobs.csv         # output file (auto-generated)
└── README.md        # project documentation
```

---

## 👤 Author

**Kevin Dong**  
Computer Science @ University of Toronto  
[LinkedIn](https://www.linkedin.com/in/kevindong668/) · [GitHub](https://github.com/fatasduckling)
