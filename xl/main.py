from functions import *

data=get_data_from_excel('class_1.xlsx')
scores = list(data.values())

avg = get_average(scores)
variance = get_variance(scores,avg)
std_dev = get_std_dev(variance)

print("평균: {}, 분산: {}, 표준편차: {}".format(avg, variance, std_dev))
