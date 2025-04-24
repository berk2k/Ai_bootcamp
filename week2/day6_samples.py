data = [10,20,30,40,50]
mean = sum(data) / len(data)

sorted_data = sorted(data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else \
    (sorted_data[len(data) // 2 -1] + sorted_data[len(data) // 2]) / 2
print("median: ", median)

from statistics import mode
print("mode: ", mode(data))

variance = sum((x - mean) ** 2 for x in data)/len(data)
# total = 0
# for x in data:
#     total += (x - mean) ** 2
# variance = total / len(data)
print("variance: ",variance)

std_dev = variance ** 0.5 
print("standard deviation:",std_dev)

# hypothesis testing 
import scipy.stats as stats, ttest_ind
sample_mean = mean 
z_score = 1.96

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5),
     sample_mean + z_score * (std_dev / len(data) ** 0.5))

print("95% confidence interval:",ci)

# sample dataset
group1 = [2.1,2.5,2.8,3.0,3.2]
group2 = [1.8,2.0,2.4,2.7,2.9]

# perform t-test
t_stat, p_value = ttest_ind(group1,group2)
print("t-statistic: ",t_stat)
print("p-value:",p_value)

# interpretation
alpha = 0.05
if p_value < alpha:
    print("reject the null hypothesis: significant difference")
else:
    print("fail to reject to null hypothesis: no significant difference")



