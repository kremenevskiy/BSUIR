import pandas as pd

ids = ['iphone8', 'iphone9', 'iphoneX', 'iphoneXs']
cnt = [10, 20, 30, 40]
price = [500, 700, 900, 1000]

df = pd.DataFrame({'name': ids, 'count': cnt, 'price': price})
df.to_csv('data.csv', index=False)
