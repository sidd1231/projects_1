import requests
from bs4 import  BeautifulSoup
import pprint

res=requests.get('https://news.ycombinator.com/news')

soup=BeautifulSoup(res.text,'html.parser')
title=soup.select('.title')
links=soup.select('.titlelink')
subtxt=soup.select('.subtext')
# print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist ,key=lambda K:K['votes'] ,reverse=True)


def create_custom_hn(links,subtxt):
    hn=[]
    for inx, itm in enumerate(links):
        title=links[inx].getText()
        href=links[inx].get('href',None)
        votes=subtxt[inx].select('.score')
        if len(votes):

          points=int(votes[0].getText().replace(' points',''))
          if points >99:
             hn.append({'title':title,'link':href,'votes':points})
    

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links,subtxt))


/class=morelink