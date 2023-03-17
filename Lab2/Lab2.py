import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
import numpy as np
import pandas as pd
from zat.log_to_dataframe import LogToDataFrame
df = LogToDataFrame()
z_df = df.create_dataframe('dns.log')
domains = z_df['query']
domains.name = 'CNAME'
df = pd.read_csv('Fhosts.data', sep="\s+", names=['redirect_to','CNAME'])
bd_domains = df['CNAME']
merged = pd.merge(domains, bd_domains, on='CNAME', how='left', indicator='exists')
merged['exists'] = np.where(merged.exists == 'both', True,False)
count = merged['exists'].value_counts()[1]
percentile = round(merged['exists'].value_counts(normalize=True)[1]*100, 2)
print("DNS имен из списков трафика: {}.".format(count), "Процент нежелательного трафика: {}%.".format(percentile), sep='\n')
