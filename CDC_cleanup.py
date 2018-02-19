#!/usr/bin/env python

import pandas as pd
import datetime

c = pd.read_csv("CDC.csv")
clean_col = ['Project Name', 'Bid Date', 'Estimated Start Date', 'Type', 'Status', 'Value', 'Address', 'City', 'State',
             'Company Name', 'Role', 'Web Address', 'Project Construction Data Company URL']
cleaned = c[clean_col]
now = datetime.datetime.now()
cleaned.to_csv(f"CDC {now.month}-{now.day}-{now.year}.csv", index=False)
