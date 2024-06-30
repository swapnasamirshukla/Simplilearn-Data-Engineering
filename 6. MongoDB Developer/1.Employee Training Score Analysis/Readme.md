```markdown
# Description

PQR Corp is a leading corporate training provider. A lot of prestigious organizations send their employees to PQR Corp for training on different skills. As a distinct training provider, PQR Corp has decided to share an analysis report with their clients. This report will help their clients know the employees who have completed training and evaluation exams, their strengths, and areas where employees need improvement. This is going to be a unique selling feature for PQR Corp. As PQR Corp is already doing great business and they train a large number of people every month, they have a huge amount of data to deal with. They have hired you as an expert and want your help to solve this problem.

## Attributes of Data

- **Id**: ID of the person who was trained
- **Name**: Name of the person who was trained
- **Evaluation**: Evaluation term
- **Score**: Score achieved by the person for the specific term

A person can undergo multiple evaluations. Each evaluation will have a unique result score.

### Sample Data

```json
{
  "_id": 0,
  "name": "Ancy",
  "results": [
    {"evaluation": "term1", "score": 1.463179736705023},
    {"evaluation": "term2", "score": 11.78273309957772},
    {"evaluation": "term3", "score": 6.676176060654615}
  ]
}
```

## Tasks

PQR Corp has assigned the following tasks to you to analyze the results:

1. Find count and percentage of employees who failed in term 1, the passing score being 37
2. Find employees who failed in aggregate (term1 + term2 + term3)
3. Find the average score of trainees for term1
4. Find the average score of trainees for aggregate (term1 + term2 + term3)
5. Find the number of employees who failed in all three (term1 + term2 + term3)
6. Find the number of employees who failed in any of the three (term1 + term2 + term3)

