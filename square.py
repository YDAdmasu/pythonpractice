n = [1,2,3,4,5]
def square(n):
    square = []
    for i in n:
        square.append(i*i)
    return square
print(square(n))
#using list comprehension
n = [1,2,3,4,5]
square = [i*i for i in n]
print(square)
# this an example of O(n) time complexity