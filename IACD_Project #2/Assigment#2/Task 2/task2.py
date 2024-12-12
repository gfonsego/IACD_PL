from mrjob.job import MRJob
from mrjob.step import MRStep

class MinTemperatureByCaptital(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_min,reducer=self.reducer_get_min)
        ]
    
    def mapper_get_min(self, _, line):
        columns = line.strip().split(',')

        weather_station = columns[0]
        temperature = columns[3]

        yield weather_station, int(temperature)

    def reducer_get_min(self, weather_station, values):
        yield weather_station, min(values)

if __name__ == '__main__':
    MinTemperatureByCaptital.run()    