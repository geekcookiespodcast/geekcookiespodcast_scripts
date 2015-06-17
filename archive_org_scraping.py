#!/home/geekcookies/env/bin/python

import requests
import bs4
import time
import csv

response = requests.get('https://archive.org/search.php?query=Geekcookiespodcast')
soup = bs4.BeautifulSoup(response.text)
actual_date = time.strftime("%Y-%m-%d %H:%M:%S")
path = "/home/geekcookies/geekcookies.brapi.net/"

# ## One element test
#
# Let's test one (the first) element in the HTML tree, extract the important data there.
#cell = soup.findAll(attrs={"class" : "hitCell"})[0]
#dic = {'date': actual_date,'filename' : str(cell.a.contents[0]),'comment' : str(cell.contents[4]),'downloads' : int(cell.contents[-1])}
#for key,value in dic.iteritems():
#   print key , type(value),value

# ## All element
#
# Extract data from all elements in the HTML tree with list comprehension.
def function_or_default(function, argument, default):
    try:
        result = function(argument)
    except:
        result = default
    return result

search_results = soup.findAll(attrs={"class" : "item-ia"})
output = []
for r in search_results:
    row = []
    row.append(actual_date) # insert actual date
    # this follow the new archive page format as on 03.2015
    row.append(str(r.findChildren(attrs={"class" : "ttl C C2"})[0].a.text)) # get title
    row.append(str(r.findChildren(attrs={"class" : "hidden-tiles views C C1"})[0].findChildren(attrs={"class" : "hidden-xs"})[0].text)) # get views
    output.append(row)

with open(path+"archive.org_geekcookiespodcast.csv", "ab") as f:
    writer = csv.writer(f,delimiter=',',quotechar='"', lineterminator="\n")
    writer.writerows(output)
f.close()
# deserialize output for each entry

#convert to dict
cookies_dict = {}
for datetime,name,downloads in output:
    cookies_dict[name]=[datetime,downloads]
for name,val in cookies_dict.iteritems():
    if 'geekcookies_ep_0' in name:
        if 'geekcookies_ep_0' == name:
            output_row = [actual_date,str(int(cookies_dict[name][1])+int(cookies_dict[name+'_new'][1]))]
        else:
            continue
    else:
            output_row = val
    print name,val,output_row
    with open(path+name+".csv", "ab") as f:
        writer = csv.writer(f,delimiter=',',quotechar='"',lineterminator="\n")
        writer.writerows([ output_row ])
    f.close()

# using pandas
#cookies_df = pd.DataFrame.from_records(output,columns=['datetime','filename','downloads'])
#cookies_df.index =  pd.to_datetime(cookies_df.datetime)
#cookies_df.drop('datetime', axis=1, inplace=True)

#for stri in cookies_df.filename.unique():
    #if 'geekcookies_ep_0' in stri:
        #if 'geekcookies_ep_0' == stri:
            #(cookies_df.ix[cookies_df.filename == stri+'_new','downloads']+ \
            #cookies_df.ix[cookies_df.filename == stri,'downloads']).fillna(value=0).to_csv("/home/geekcookies/geekcookies.brapi.net/"+stri+".csv", sep=',', encoding='utf-8')
    #else:
        #cookies_df.ix[cookies_df.filename == stri,'downloads'].to_csv("/home/geekcookies/geekcookies.brapi.net/"+stri+".csv", sep=',', encoding='utf-8')



