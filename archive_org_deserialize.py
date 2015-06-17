import pandas as pd

path = "/home/geekcookies/geekcookies.brapi.net/"

cookies_df = pd.read_csv(path+'archive.org_geekcookiespodcast.csv',parse_dates=['datetime'], index_col=['datetime'])

for stri in cookies_df.filename.unique():
    if 'geekcookies_ep_0' in stri:
        if 'geekcookies_ep_0' == stri:
            (cookies_df.downloads[cookies_df.filename == stri]+ \
            cookies_df.downloads[cookies_df.filename == stri+'_new']).fillna(value=0).to_csv(path+stri+".csv", sep=',', encoding='utf-8')
    else:
        cookies_df.downloads[cookies_df.filename == stri].to_csv(path+stri+".csv", sep=',', encoding='utf-8')
