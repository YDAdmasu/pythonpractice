prices = [10,20,30,40,50]
eps = [1,2,3,4,5]
index = 0
def stock_price(prices,eps,index):
    pe = prices[index] / eps[index]
    return pe
print(stock_price(prices,eps,index))
# this code have a time complexity of O(1) because it is not dependent on the size of the input