from mrjob.job import MRJob
from mrjob.step import MRStep

class SortedAmountSpentByCustomer(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_get_sum),
            MRStep(reducer=self.reducer_sort)
        ]
    
    def mapper(self, _, line):
        # Parse each line to extract customerId and amount
        customerId, productId, amount = line.strip().split(',')
        yield customerId, float(amount)
    
    def reducer_get_sum(self, customer_id, values):
        # Sum all amounts for each customer
        yield None, (sum(values), customer_id)

    def reducer_sort(self, _, customer_amount_pairs):
        # Sort customers by total amount in descending order
        sorted_pairs = sorted(customer_amount_pairs, reverse=True, key=lambda x: x[0])
        for total, customer_id in sorted_pairs:
            yield customer_id, f'{total:.2f}'

if __name__ == '__main__':
    SortedAmountSpentByCustomer.run()
