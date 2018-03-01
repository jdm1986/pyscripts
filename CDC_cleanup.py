#!/usr/bin/env python

import pandas as pd
from datetime import datetime
now = datetime.now()

c = pd.read_csv("../../../Desktop/Local/Monday Meeting/CDC.csv", index_col=False)

c.set_index('Project Id')

c.to_csv("cdc_test.csv", index=False)

# retain only necessary columns
clean_col = ['Project Name', 'Bid Date', 'Estimated Start Date', 'Type',
              'Status', 'Value', 'Address', 'City', 'State',
             'Company Name', 'Address.1', 'City.1', 'State.1', 'Role', 'Web Address',
             'Project Construction Data Company URL']
cleaned = c[clean_col]

# retain only values in Role that we are interested in seeing
cleaned2 = (cleaned.loc[cleaned['Role'].isin(['Owner', 'General Contractor', 'Apparent Low General Contractor',
                                              'Awarded General Contractor', 'Construction Manager'])])

# remove values in Type column that have no interest to us
cleaned3 = (cleaned2.loc[~cleaned['Type'].isin(['Renovation', 'Roof Replacement', 'Remodeling'])])


# convert Value column to float, sort by Value column
cleaned3 = cleaned3.copy()
cleaned3['Value'] = cleaned3['Value'].str.replace(',', '')
cleaned3['Value'] = cleaned3['Value'].str.replace('$', '')
cleaned3['Value'] = cleaned3['Value'].astype("float")
cleaned4 = cleaned3.sort_values("Value")


cleaned4.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=False)

# c.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=True)
