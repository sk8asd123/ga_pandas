import pandas.io.ga as ga
#print top 30 landing pages
                     
df = ga.read_ga(['pageviews','entrances'], 
                         dimensions=['date', 'landingPagePath'], 
                         start_date='2013-04-01')

reset_df = df.reset_index()
sorted_df = reset_df.sort(columns=['pageviews','entrances'], ascending = False)

print (sorted_df.head(30))

