# 확률에 관련된 기능을 모아놓은 클래스
# 확장 가능성을 고려해서 만듦
import math

class Stat:
    def get_average(self, scores):
        """
        get_average(score_dict_raw_data)->int average_of_scores
        """
        s = 0
        for score in scores:
            s += score
        return s // len(scores)

    def get_variation(self, scores, avg):
        """
        get_variance(score_dict_raw_data)->int variance_of_scores
        """
        s = 0
        for score in scores:
            s += score
        return round(s/len(scores), 1)

    def get_std_dev(self, variation):
        """
        get_std_dev(score_dict_raw_data)->int standard_dev_of_raw_variance
        """
        tmp = round(math.sqrt(variation))
        return tmp

# s = Stat()
# s.get_variation((10,20),10)