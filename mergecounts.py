import pandas as pd
d1 = pd.read_csv('d1_genecounts.csv')
d2 = pd.read_csv('d2_genecounts.csv')
d3 = pd.read_csv('d3_genecounts.csv')

c1 = pd.read_csv('c1_genecounts.csv')
c2 = pd.read_csv('c2_genecounts.csv')
c3 = pd.read_csv('c3_genecounts.csv')

d1 = d1[:-1] # drop '*' row of unaligned gene reads
d2 = d2[:-1] # drop '*' row of unaligned gene reads
d3 = d3[:-1] # drop '*' row of unaligned gene reads
c1 = c1[:-1] # drop '*' row of unaligned gene reads
c2 = c2[:-1] # drop '*' row of unaligned gene reads
c3 = c3[:-1] # drop '*' row of unaligned gene reads

## Normalize counts 
d1['drought_1_cnt'] = d1['drought_1_cnt']/d1['drought_1_cnt'].sum()
d2['drought_2_cnt'] = d2['drought_2_cnt']/d2['drought_2_cnt'].sum()
d3['drought_3_cnt'] = d3['drought_3_cnt']/d3['drought_3_cnt'].sum()
c1['control_1_cnt'] = c1['control_1_cnt']/c1['control_1_cnt'].sum()
c2['control_2_cnt'] = c2['control_2_cnt']/c2['control_2_cnt'].sum()
c3['control_3_cnt'] = c3['control_3_cnt']/c3['control_3_cnt'].sum()


joint = d1.merge(d2, how='outer', on='gene')
joint = joint.merge(d3, how='outer', on='gene')
joint = joint.merge(c1, how='outer', on='gene')
joint = joint.merge(c2, how='outer', on='gene')
joint = joint.merge(c3, how='outer', on='gene')

joint = joint.fillna(0)
joint.to_csv('merged_genecounts.csv', index=False)

