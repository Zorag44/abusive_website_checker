from requests import Request, Session
import json
import re
url='https://abusiveexperiencereport.googleapis.com/v1/violatingSites?key=[ur api key]'
headers={
    'Accept': 'application/json'
}
session=Session()
session.headers.update(headers)
response=session.get(url)
#parsing json data and converting it to a python dictionary
data=json.loads(response.text)
#just to check with indents to make it feasible to understand
dataf=json.dumps(data,indent=2)
sites=[]
#cleaning sorta
for i in range(len(data["violatingSites"])):
    site=data["violatingSites"][i]["reviewedSite"]
    sites.append(site)
search=input('enter the webiste in the form of (xyz.com) or a keyword:')
# if search in sites:
#     print(f'{search} is an abusive website.')
# else:
#     print('{} is not an abusive website'.format(search))
flag=False
#printing
for i in range(len(sites)):
    if re.search(search,sites[i]):
        print('{0} or {1} is an abusive site'.format(search,sites[i]))
        flag=False
        break
    else:
        flag=True
if flag:
    print('{0} is not an abusive site'.format(search))
#print(sites)        
