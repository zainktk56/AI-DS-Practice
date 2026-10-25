import pandas as pd

# data=[1,34,45,3,34,56,6875,333,333,34,55]

#  pandas series to list 
# series=pd.Series(data)

# print(series.tolist())

# Pandas program to add, subtract, multiple and divide two Pandas Series.

# data1=[2, 4, 6, 8, 10]
# data2=[1, 3, 5, 7, 9]

# s1=pd.Series(data1)
# s2=pd.Series(data2)

# print(f"Series 1 To List ",s1)
# print(f"Series 2 To List ",s2)

# print(f"ADD BOTH SERIES : ", s1 + s2)

# print(f"SUBTRACT BOTH SERIES : ", s1 - s2)

# print(f"MULTIPLY BOTH SERIES : ", s1 * s2)

# print(f"DIVIDE BOTH SERIES : ", s1 / s2)


# Series Comparison
# Pandas program to compare the elements of the two Pandas Series.

# data1=[2, 4, 6, 8, 10]
# data2=[1, 3, 5, 7, 10]

# s1=pd.Series(data1)
# s2=pd.Series(data2)

# print(s1 == s2)
# print(s1 > s2)
# print(s2 > s1)

# Dict to Series
# Pandas program to convert a dictionary to a Pandas series.

# series=pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800})
# print(series)

# Array to Series 
# Pandas program to convert a NumPy array to a Pandas series

# series=pd.Series( [10, 20, 30, 40, 50])
# print(series)

# Change Series DataType
# Pandas program to change the data type of given a column or a Series.

# series=pd.Series([10,20,"pyhton",300.12,400])
# change_datatype=pd.to_numeric(series,errors='coerce')

# print(change_datatype)

