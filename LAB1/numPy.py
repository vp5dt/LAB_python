import numpy as np
from collections import Counter

value=np.random.randint(20, size=15)
cnt = Counter(value)
print(value)
mostfrequent=cnt.most_common(1)
print("Most frequent number was:")
print(mostfrequent[0][0])
print("Number of times it was repeated:")
print(mostfrequent[0][1])