#!/usr/bin/env python

import pandas as pd
from datetime import datetime
now = datetime.now()

c = pd.read_csv("../../../Desktop/Local/Monday Meeting/CDC.csv", index_col=False)

c.set_index('Project Id')

c.rename(columns={c.columns[25]: ''}).inplace = True
c.rename(columns={c.columns[27]: ''}).inplace = True
c.rename(columns={c.columns[28]: ''}).inplace = True

c.to_csv("cdc_test.csv", index=False)

clean_col = ['Project Name', 'Bid Date', 'Estimated Start Date', 'Type',
              'Status', 'Value', 'Address', 'City', 'State',
             'Company Name', 'Address.1', 'City.1', 'State.1', 'Role', 'Web Address',
             'Project Construction Data Company URL']
cleaned = c[clean_col]

cleaned2 = (cleaned.loc[cleaned['Role'].isin(['Owner', 'General Contractor', 'Apparent Low General Contractor',
                                              'Awarded General Contractor', 'Construction Manager'])])

cleaned3 = (cleaned2.loc[~cleaned['Type'].isin(['Renovation', 'Roof Replacement', 'Remodeling'])])

cleaned4 = cleaned3.sort_values(cleaned.columns[0])


cleaned4.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=False)

# c.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=True)# #
# # cleaned4 = cleaned3.sort_values(cleaned.columns[0])
#
# now = datetime.datetime.now()
# cleaned.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=False)

c.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=False)
