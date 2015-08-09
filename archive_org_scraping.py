#!/usr/bin/python

import json
import urllib2
import pandas as pd
import re
import time

### get the data as json
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
resp = opener.open('https://archive.org/advancedsearch.php?q=creator%3A%22Geekcookiespodcast%22&fl%5B%5D=downloads&fl%5B%5D=publicdate&fl%5B%5D=title&sort%5B%5D=addeddate+asc&sort%5B%5D=&sort%5B%5D=&rows=50&page=1&indent=yes&output=json')
data = resp.read()
result = json.loads(data)

### make a dataframe
gc_df = pd.DataFrame(result['response']['docs'])

### collapse different fileversion
gc_df.title = gc_df.title.apply(lambda x : re.match("^(geekcookies_ep_\d+).*$",x).group(1))
grouped_df = gc_df.groupby('title').sum()
grouped_df['datetime'] = time.strftime("%Y-%m-%d %H:%M:%S")
grouped_df['title'] = grouped_df.index
grouped_df = grouped_df.set_index('datetime').ix[:,('title','downloads')]

### append to general file
grouped_df.fillna(value=0).to_csv('geekcookies.brapi.net/archive.org_geekcookiespodcast.csv', sep=',', encoding='utf-8',header=None,index=True, mode='a')

### append to single files
grouped_df.fillna(value=0).to_csv('geekcookies.brapi.net/archive.org_geekcookiespodcast.csv', sep=',', encoding='utf-8',header=None,index=True, mode='a')
for row_index, row in grouped_df.iterrows():
    row['datetime'] = row_index
    print row.title+'.csv'
    row.ix[['datetime','downloads']].fillna(value=0).to_frame().transpose().to_csv('geekcookies.brapi.net/'+row.title+'.csv', sep=',', encoding='utf-8',header=None,index=False, mode='a')
