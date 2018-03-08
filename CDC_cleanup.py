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
cleaned = (cleaned.loc[cleaned['Role'].isin(['General Contractor', 'Apparent Low General Contractor',
                                              'Awarded General Contractor', 'Construction Manager'])])

cleaned = (cleaned.loc[~cleaned['Type'].isin(['Renovation', 'Roof Replacement', 'Remodeling'])])


# convert Value column to float, sort by Value column
cleaned = cleaned.copy()
cleaned['Value'] = cleaned['Value'].str.replace(',', '')
cleaned['Value'] = cleaned['Value'].str.replace('$', '')
cleaned['Value'] = cleaned['Value'].astype("float")
cleaned = cleaned.sort_values("Value")

for value in cleaned['Value']:
    value = ('${0:,.0f}'.format(value))


cleaned.to_csv(f"../../../Desktop/Local/Monday Meeting/CDC {now.month}-{now.day}-{now.year}.csv", index=False)

