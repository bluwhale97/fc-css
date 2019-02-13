import statistics
from openpyxl import load_workbook

class DataHandler:
    # composition
    calculator = statistics.Stat()
    
    @classmethod
    def get_data_from_excel(cls, filename):
        """
        get_data_from_excel(filename)->{'name1' : score1, 'name2' : 'score2'}
        """
        wb = load_workbook(filename)
        ws = wb.active
        g = ws.rows

        raw_data = {k.value :v.value for k,v in g}
        return raw_data 

    def __init__(self, ExlFilename):
        self.raw_data = DataHandler.get_data_from_excel(ExlFilename)
    #   self.raw_data = self.get_data_from_excel()
        self.year_class = ExlFilename.split('.')[0].split('_')[1]

        # cache
        self.cache={}

    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.raw_data.values())
        
        return self.cache.get('scores')

    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.calculator.get_average(self.get_scores())

        return self.cache['average']

    def get_variation(self):
        if 'variaion' not in self.cache:
            self.cache['variation'] = self.calculator.get_variation(self.get_scores(),self.get_average())
        
        return self.cache['variation']

    def get_std_dev(self):
        if 'std_dev' not in self.cache:
            tmp = self.calculator.get_std_dev(self.get_variation())
            self.cache['std_dev'] = tmp        
        return self.cache['std_dev']

    def evaluate_class(self, avrg, total_avrg, std_dev, sd=20):
        if avrg < total_avrg and std_dev > sd:
            print('성적 저조, 실력차이 크다')
        elif avrg > total_avrg and std_dev > sd:
            print('성적 평균이상, 실력 차이 크다')
        elif avrg < total_avrg and std_dev < sd:
            print("학생 실력차이 적음, 성적 저조")
        elif avrg > total_avrg and std_dev < sd:
            print("성적 평균이상, 실력 차이 비슷")

    def get_evaluation(self, total_avrg, sd=20):
        print('*'*50)
        print('{} 반 성적 분석 결과'.format(self.year_class))
        print('{} 반의 평균은 {}점이고 분산은 {}이며 표준편차는 {}이다.'.format(
            self.year_class,
            self.get_average(),
            self.get_variation(),
            self.get_std_dev()
        ))
        print('*'*50)
        print('{}반 종합 평가'.format(self.year_class))
        print('*'*50)
        self.evaluate_class(self.get_average(), total_avrg, self.get_std_dev(), sd)
