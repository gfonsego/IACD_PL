from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class SortWordFrequency(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_sort)
        ]
    
    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_sort(self, _, word_count_pairs):
        sorted_pairs = sorted(word_count_pairs, reverse=True, key=lambda x: x[0])
        for count, word in sorted_pairs:
            yield word, count

if __name__ == '__main__':
    SortWordFrequency.run()
