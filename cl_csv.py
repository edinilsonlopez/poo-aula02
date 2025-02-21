import csv_class
#import pandas as pd

# df = pd.read_csv("./data.csv")
# #df.info()
# df_filtrado = df[df['estado'] == 'SP']

# print(df_filtrado)

path = './data.csv'
col = 'estado'
val = 'SP'

df_data = csv_class.csv_processor(path)
df_data.load_csv()
print(df_data.filter_df(col,val))
