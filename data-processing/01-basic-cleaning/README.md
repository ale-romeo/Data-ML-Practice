# Basic Data Cleaning Project

**Difficulty:** Beginner  
**Estimated Time:** 2-3 hours  
**Skills Practiced:** pandas, data cleaning, exploratory data analysis

## 📚 Learning Objectives

By completing this project, you will learn to:
- Handle missing values in datasets
- Detect and remove duplicate records
- Clean and standardize text data
- Validate data types and formats
- Create data quality reports
- Implement data cleaning pipelines

## 📋 Project Description

In this project, you'll clean a messy customer dataset containing various data quality issues typical in real-world scenarios. The dataset includes missing values, duplicates, inconsistent formatting, and invalid entries.

## 🎯 Tasks

### Task 1: Data Exploration
- [ ] Load the raw dataset and examine its structure
- [ ] Identify missing values, duplicates, and data type issues
- [ ] Create a data quality assessment report

### Task 2: Missing Data Handling
- [ ] Analyze missing data patterns
- [ ] Implement different imputation strategies
- [ ] Compare results of different approaches

### Task 3: Duplicate Detection
- [ ] Identify exact and fuzzy duplicates
- [ ] Implement deduplication logic
- [ ] Validate duplicate removal results

### Task 4: Data Standardization
- [ ] Clean and standardize text fields
- [ ] Normalize phone numbers and email addresses
- [ ] Standardize date formats

### Task 5: Validation and Quality Checks
- [ ] Implement data validation rules
- [ ] Create data quality metrics
- [ ] Generate final data quality report

## 📁 Files Structure

```
01-basic-cleaning/
├── data/
│   ├── raw/
│   │   └── customers_messy.csv     # Raw messy dataset
│   └── processed/
│       └── customers_clean.csv     # Cleaned dataset
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_missing_data_analysis.ipynb
│   ├── 03_duplicate_detection.ipynb
│   └── 04_data_standardization.ipynb
├── src/
│   ├── data_cleaner.py            # Main cleaning functions
│   ├── quality_checker.py         # Data quality assessment
│   └── utils.py                   # Helper functions
├── requirements.txt
└── README.md                      # This file
```

## 🛠 Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

2. **Generate sample data:**
   ```bash
   python src/generate_sample_data.py
   ```

3. **Start Jupyter notebook:**
   ```bash
   jupyter notebook notebooks/
   ```

## 📊 Sample Data Description

The `customers_messy.csv` dataset contains:
- **customer_id**: Unique identifier (some missing)
- **first_name**: First name (inconsistent capitalization)
- **last_name**: Last name (some missing, mixed case)
- **email**: Email address (some invalid formats)
- **phone**: Phone number (various formats)
- **address**: Street address (inconsistent formatting)
- **city**: City name (spelling variations)
- **state**: State code (mixed abbreviations/full names)
- **zip_code**: ZIP code (various formats, some invalid)
- **registration_date**: Account creation date (multiple formats)
- **last_login**: Last login timestamp (some missing)
- **status**: Account status (inconsistent values)

## 🎯 Expected Outcomes

After completing this project, you should have:

1. **Clean dataset** with standardized formatting
2. **Data quality report** showing before/after metrics
3. **Reusable cleaning functions** for similar datasets
4. **Documentation** of cleaning decisions and rationale

### Quality Metrics to Achieve:
- **Completeness:** >95% non-null values
- **Uniqueness:** 100% unique customer records
- **Validity:** 100% valid email and phone formats
- **Consistency:** Standardized text formatting

## 🔍 Validation Checklist

- [ ] No duplicate customer records
- [ ] All email addresses follow valid format
- [ ] Phone numbers standardized to (XXX) XXX-XXXX format
- [ ] State codes standardized to 2-letter abbreviations
- [ ] ZIP codes follow XXXXX or XXXXX-XXXX format
- [ ] Dates in consistent YYYY-MM-DD format
- [ ] Missing value percentage documented

## 🚀 Extensions

Once you've completed the basic project, try these extensions:
- **Fuzzy matching** for similar company names
- **Address standardization** using geocoding APIs
- **Automated data profiling** pipeline
- **Data quality dashboard** with Streamlit
- **Real-time data validation** API

## 📚 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Data Cleaning with Python](https://realpython.com/python-data-cleaning-numpy-pandas/)
- [Handling Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)

## 🤝 Need Help?

If you get stuck:
1. Check the solution notebooks in the `solutions/` folder
2. Review the data cleaning functions in `src/`
3. Open an issue in the main repository
4. Join our community discussions

---

**Good luck with your data cleaning journey! 🧹✨**