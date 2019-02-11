import math
from openpyxl import load_workbook

wb = load_workbook('class_1.xlsx')
ws = wb.active
g = ws.rows

raw_data = {k.value :v.value for k,v in g}

print(raw_data)

scores = list(raw_data.values())

#평균
s = 0
for score in scores:
    s += score

avg = s // len(scores)

#분산
s = 0

for score in scores:
    s+=(score-avg)**2

variance = round(s//len(scores), 1)

#표준편차

std_dev = round(math.sqrt(variance), 1)

print('평균 : {}, 분산: {}, 표준편차: {}'.format(avg, variance, std_dev))