import requests

from operator import itemgetter

#Make an API call, and store the response.
r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
print(f"Status code: {r.status_code}")

#Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:20]:
    #Make a separate API call for each submission.
    r = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json")
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()
    
    #Build a dict for each article
    submission_dict = {
        'title':response_dict['title'],
        'hn_link':f"http:news.ycombinator.com/item?id={submission_id}.json",
        'comments':response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


