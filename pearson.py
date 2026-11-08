import numpy as np
from scipy.stats import pearsonr

study_hours = [1, 2, 3, 4, 5, 6]
marks = [20, 30, 40, 50, 60, 70]

correlation, p_value = pearsonr(study_hours, marks)
print("correlation" , correlation)
print("pvalue", p_value)

if correlation>0:
    print("Postive correlation")
elif correlation>0:
    print("Postive correlation")