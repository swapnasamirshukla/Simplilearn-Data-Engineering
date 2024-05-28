**Objective:** To utilize Hive features for data analysis and provide actionable insights to the HR team to improve employer-employee relationships based on current and ex-employee sentiments gathered from social media.

**Problem Statement:** The HR team is collecting feedback or sentiments from social media platforms to understand employee satisfaction levels. This data, scraped from Glassdoor, contains detailed reviews from 67,000 employees of major companies like Google, Amazon, Facebook, Apple, Microsoft, and Netflix.

**Domain:** Human Resources

**Analysis to be Done:** Exploratory analysis will be conducted to identify features and relationships influencing employee satisfaction. Actionable insights will be derived from historical data.

**Content:** The dataset (`employee_review_data.csv`) contains the following categories:

1. **Index:** Index number.
2. **Company:** Name of the company being reviewed.
3. **Location:** Global dataset, including country names or city and state if in the USA.
4. **Date Posted:** Date posted in MM DD, YYYY format.
5. **Job-Title:** Role of the reviewer, indicating "Current" or "Former" employee.
6. **Summary:** Short summary of the employee review.
7. **Pros:** Pros mentioned in the review.
8. **Cons:** Cons mentioned in the review.
9. **Overall Rating:** Rating on a scale of 1-5.
10. **Work/Life Balance Rating:** Rating on a scale of 1-5.
11. **Culture and Values Rating:** Rating on a scale of 1-5.
12. **Career Opportunities Rating:** Rating on a scale of 1-5.
13. **Comp and Benefits Rating:** Rating on a scale of 1-5.
14. **Senior Management Rating:** Rating on a scale of 1-5.
15. **Helpful Review Count:** Number of people who found the review helpful.

**Steps to Perform:**

1. Create a Hive table partitioned by country and bucketed by year and load the `employee_review_data.csv` file.
2. Impute missing values (none) for all rating columns with a numerical value between 0 and 5 by calculating the median for each rating field.
3. Write the final relation schema to a `review.csv` file in the HDFS home directory.
4. Display trends in overall ratings:
   - Globally by company, identifying trends at 25%, 50%, 75%.
   - Globally by company per year, identifying trends at 25%, 50%, 75%.
   - By company by country, identifying trends for each company by country at 25%, 50%, 75%.
5. Display the impact of employee status on rating a company by overall ratings field, company, and year.
6. Display the impact of job role on rating a company by overall ratings field, company, and year.
7. Display the relationship between the overall rating score vs. the rest of the rating field scores by company and document the findings.

**Findings Documentation:**

a) Which corporation is worth working for.
b) Classification of satisfied or unsatisfied employees.
