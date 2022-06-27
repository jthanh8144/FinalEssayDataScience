import pandas as pd


clean = pd.read_csv('cleaned_data.csv')
raw = pd.read_csv('raw_data.csv')

for i in range(clean.shape[0]):
    if raw['Price'][i].find('m²') != -1:
        clean['Price'][i] = str(float(clean['Area'][i]) * float(raw['Price'][i].split(' ')[0]))

clean.to_csv('abc.csv', index=False, encoding='utf-8-sig')