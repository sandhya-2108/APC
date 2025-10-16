import pandas as pd
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("Series:", s)
print("Element at index 1:", s[1])
print("Element at index 4:", s[4])

a = [1, 2, 3, 4, 5]
s = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
print(s)