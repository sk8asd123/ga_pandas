# -*- coding: utf-8 -*- 
import pandas.io.ga as ga
import pandas as pd

# goes through profiles,accounts and provides aggregate of visits/pageviews
ids = {'123':'456'}

filters    = "source==Facebook";"medium==Social"

all_data = pd.DataFrame()

for profile, account in ids.iteritems():    
    df = ga.read_ga(['visits', 'pageviews'], 
                             dimensions=['date', 'landingPagePath', 'medium', 'campaign', 'source'], 
                             start_date='2013-03-01', end_date='2013-04-24',
                             account_id=account, profile_id=profile, filters=filters,
                             chunksize = 1000)

    for d in df:
        d['profile'] = profile  
        d = d.reset_index()
        all_data = all_data.append(d)

all_data.to_csv('C:\\tmp\\' + '322.csv', ',', line_terminator = '\n')


    
