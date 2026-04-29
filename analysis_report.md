# Sales Data Analysis Report

**Internship Week 3 Project | Python Data Analysis**
**Submitted by:** Mariya Patel
**Date:** 29 April 2026

---

## Project Overview

This project analyzes a sales dataset containing 100 transactions across 4 months (January–April 2024). The goal was to load real data using the pandas library, clean it, and extract meaningful business insights including total revenue, best-selling products, and regional performance.

---

## Dataset Description

| Property | Value |
|----------|-------|
| File | sales_data.csv |
| Total Rows | 100 |
| Total Columns | 7 |
| Date Range | Jan 2024 – Apr 2024 |
| Missing Values | None |

**Columns:** Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales

---

## Setup Instructions

### Requirements
- Python 3.x
- pandas library

### Installation

```bash
pip install -r requirements.txt
```

### Running the Program

```bash
python sales_analysis.py
```

---

## Project File Structure

```
sales_project/
├── sales_analysis.py    ← Main Python analysis script
├── sales_data.csv       ← Dataset (100 rows)
├── requirements.txt     ← Python dependencies
└── analysis_report.md  ← This report
```

---

## Analysis Steps

### Step 1: Load Data
The dataset is loaded using `pd.read_csv()`. After loading, the shape and first few rows are displayed to confirm it loaded correctly.

### Step 2: Explore Data
Column data types are checked using `df.dtypes`. The Date column is converted from string to datetime using `pd.to_datetime()` for accurate time-based analysis.

### Step 3: Clean Data
Missing values are checked with `df.isnull().sum()`. Duplicate rows are removed using `df.drop_duplicates()`. The dataset had 0 missing values and 0 duplicates — it was already clean.

### Step 4: Analyze Sales
Five key metrics are calculated:
- Total revenue (sum of all Total_Sales)
- Average order value (mean of Total_Sales)
- Total units sold (sum of Quantity)
- Highest and lowest single transaction

Products and regions are grouped using `df.groupby()` to find top performers.

### Step 5: Generate Report
All findings are formatted and printed as a structured report in the terminal.

---

## Key Findings

### Overall Metrics

| Metric | Value |
|--------|-------|
| Total Revenue | Rs.1,23,65,048.00 |
| Average Order Value | Rs.1,23,650.48 |
| Total Units Sold | 478 |
| Highest Single Sale | Rs.3,73,932.00 |
| Lowest Single Sale | Rs.6,540.00 |

### Revenue by Product

| Product | Total Revenue | Rank |
|---------|--------------|------|
| Laptop | Rs.38,89,210 | 1st |
| Tablet | Rs.28,84,340 | 2nd |
| Phone | Rs.28,59,394 | 3rd |
| Headphones | Rs.13,84,033 | 4th |
| Monitor | Rs.13,48,071 | 5th |

**Best Selling Product: Laptop** — contributing 31.4% of total revenue.

### Revenue by Region

| Region | Total Revenue | Rank |
|--------|--------------|------|
| North | Rs.39,83,635 | 1st |
| South | Rs.37,37,852 | 2nd |
| East | Rs.25,19,639 | 3rd |
| West | Rs.21,23,922 | 4th |

**Top Performing Region: North**

---

## Code Structure & Functions Explained

### `pd.read_csv()`
Loads the CSV file into a DataFrame — a table-like structure similar to an Excel sheet. Each column becomes a pandas Series.

### `df.isnull().sum()`
Checks each column for missing (NaN) values. Returns a count per column so we know exactly where gaps exist.

### `df.groupby("Product")["Total_Sales"].sum()`
Groups all rows by product name and sums up the Total_Sales for each group. This gives us total revenue per product in one line.

### `pd.to_datetime(df["Date"])`
Converts the Date column from plain text ("2024-01-01") to a proper datetime object, enabling month/year extraction for time-based analysis.

### `.sort_values(ascending=False)`
Sorts the grouped results from highest to lowest, making it easy to identify top performers.

---

## Screenshots

> Screenshot is available as `screenshot.png` in the GitHub repository showing the terminal output of the full analysis report.

---

## Testing Evidence

| Test | What was Checked | Result |
|------|-----------------|--------|
| Data load | CSV loads with correct shape (100 rows, 7 cols) | ✅ PASS |
| Missing values | `isnull().sum()` returns 0 for all columns | ✅ PASS |
| Total revenue | Sum of Total_Sales column = 1,23,65,048 | ✅ PASS |
| Best product | Laptop has highest grouped revenue | ✅ PASS |
| Best region | North has highest grouped revenue | ✅ PASS |
| Date parsing | Date column converts to datetime without errors | ✅ PASS |
| Monthly breakdown | 4 months (Jan–Apr) correctly extracted | ✅ PASS |

---

## What I Learned

- How to load and inspect real CSV data using pandas
- Cleaning data by checking for missing values and duplicates
- Using `groupby()` to aggregate data by category
- Converting date strings to datetime for time-based analysis
- Formatting and presenting analysis findings as a structured report

---

*Project submitted as part of Python Internship — Week 3 Assignment*
