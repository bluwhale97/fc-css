#라이브러리

import math
from openpyxl import load_workbook

def get_data_from_excel(filename):
    """
    get_data_from_excel(filename)->{'name1' : score1, 'name2' : 'score2'}
    """
    wb = load_workbook(filename)
    ws = wb.active
    g = ws.rows

    raw_data = {k.value :v.value for k,v in g}
    return raw_data

def get_average(scores):
    """
    get_average(score_dict_raw_data)->int average_of_scores
    """

    s = 0
    for score in scores:
        s += score

    return s // len(scores)

def get_variance(scores, avg):
    """
    get_variance(score_dict_raw_data)->int variance_of_scores
    """
    s = 0
    for score in scores:
        s += score
    return round(s//len(scores), 1)


def get_std_dev(variance):
    """
    get_std_dev(score_dict_raw_data)->int standard_dev_of_raw_variance
    """

    return round(math.sqrt(variance), 1)

if __name__ == "__main__":
    li = [20,30,40,50]
    avg=get_average(li)
    print(avg)
    