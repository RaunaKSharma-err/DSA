class ProductOfNumbers:

    def __init__(self):
        self.ans = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.ans = [1]
        else:
            self.ans.append(self.ans[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.ans):
            return 0
        return self.ans[-1]


obj = ProductOfNumbers()
obj.add(3);        
obj.add(0);    
obj.add(2);       
obj.add(5);        
obj.add(4);  
param_2 = obj.getProduct(4)
print(param_2)