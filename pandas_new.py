import pandas as pd
import numpy as np

# to work with one dimensional entry
series_1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
print(series_1)

"""
Output : 
0    1.5
1    2.5
2    3.0
3    4.5
4    5.0
5    6.0
dtype: float64
"""

series_2 = pd.Series(["India", "Canada", "Germany"], name="Countries")
print(series_2)

"""
0      India
1     Canada
2    Germany
Name: Countries, dtype: object
# Here Name is a column header
"""

series_3 = pd.Series({"India": "New Delhi", "Japan": "Tokyo", "UK": "London"})
print(series_3)
print(series_3["India"])
print(series_3["Japan"])


"""
India    New Delhi
Japan        Tokyo
UK          London
dtype: object
New Delhi
Tokyo
"""
