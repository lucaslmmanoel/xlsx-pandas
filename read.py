import numpy as np
import pandas as pd

file = r'file.xls'
data = pd.read_excel(file)
print(data)