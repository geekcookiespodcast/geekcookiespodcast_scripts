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

# extract the results
output = {}
title_regex = '(geekcookies_ep_[0-9]+)(.+)$'
for tmp in result['response']['docs']:
    # take care of new version of episodes with an extra _string at the end
    #if '_new' in tmp['title']:
    if re.match(title_regex ,tmp['title']):
        title = re.compile(title_regex).search(tmp['title']).group(1)
        #title = '_'.join(tmp['title'].split('_')[:-1])
    else:
        title = tmp['title']
    if title not in output:
        output[title] = 0
    output[title]=output[title]+tmp['downloads']
    #print tmp['title'],tmp['downloads']
    print title,output[title]
    print '-'*40

# cycle in the output dictionary
for name,val in output.iteritems():
    with open(path+name+".csv", "ab") as f:
        writer = csv.writer(f,delimiter=',',quotechar='"',lineterminator="\n")
        writer.writerows([ output_row ])
    f.close()
