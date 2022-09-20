import re
from collections import defaultdict 

def solution(word, pages):
    word = word.lower()
    answer = 0
    outlinks = defaultdict(list)
    urls = defaultdict(list)
    
    for i, page in enumerate(pages):
        page = page.lower()
        body = page.split('<body>\n')[1]
        body = body.split('</body>')[0]
        meta = page.split('<meta')[2]
        meta = meta.split('/>')[0]
        url = meta.split("https://")[1]
        
        url = url.replace("\"","")
        urls[url] = [i,0,0]
        
        a=body.split("<a")
        outlink = 0
        basic = 0
        for text in a:
            if text.startswith(' href'):
                link = text.split("https://")[1]
                link = link.split("\">")[0]
                outlinks[url].append(link)
                outlink+=1
                text = text.split("</a>")[1]
                text=re.split(r"[^a-z]",text)
                basic += text.count(word)
                print(text)
                
            else:
                text=re.split(r"[^a-z]",text)
                basic += text.count(word)
        
        urls[url]=[i,basic,outlink,0]
    
    for link in outlinks.keys():
        for inlink in outlinks[link]:
            if inlink in urls.keys():
                urls[inlink][3] += urls[link][1] / urls[link][2]
    
    urls = sorted(urls.items(), key=lambda x: -(x[1][1]+x[1][3]))
    print(urls)
    return urls[0][1][0]