class Factorial:
    def __init__(self, num):
        self.num = num

    def get_fact(self):
        fact_num = self.num
        if fact_num < 0:
            return -1
        fact = 1
        while fact_num > 0:
            fact *= fact_num
            fact_num -= 1
        return fact

fact_obj = Factorial(8)
result = fact_obj.get_fact()
print(f"(result={result})")