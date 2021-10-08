import requests
from bs4 import BeautifulSoup
class Scrape:
    def __init__(self,path,root):
        self.visited=[]
        self.v_titles=[]
        self.root=root
        self.path=open(path+".txt","w")
        self.keypath=open(path+"_keywords.txt","w")
        self.path2=open(path+"_all.txt","w")
        self.keypath2=open(path+"_all_keywords.txt","w")
    def run(self,urls):
        scraped_urls = []
        for url in urls:
            if url not in self.visited:
                res=requests.get(url)
                soup=BeautifulSoup(res.text,"html.parser")
                for atag in soup.find_all("a"):
                    link = atag.get("href")
                    if link and self.root in link:
                        scraped_urls.append(link)
                if not soup.find("title"):
                    continue
                page_title=soup.find("title").text.lower().strip()
                if not soup.find('meta',attrs={'name': 'keywords'}):
                    continue
                all_keywords=list(set([key.strip().lower() for key in soup.find('meta',attrs={'name': 'keywords'}).get('content').split(',') if key.strip().lower() in ['lifehacker','techcrunch']]))
                extracted_keywords=[keyword for keyword in all_keywords if keyword in page_title]
                print("TITLE:\t\t\t"+page_title)
                print("ALL KEYWORDS:\t\t"+','.join(all_keywords))
                print("EXTRACTED KEYWORDS:\t"+','.join(extracted_keywords))
                if page_title and all_keywords and page_title not in self.v_titles:
                    self.path2.write(page_title+'\n')
                    self.keypath2.write(','.join(all_keywords)+'\n')
                    print("append to dataset2")
                if page_title and extracted_keywords and page_title not in self.v_titles:
                    self.path.write(page_title+'\n')
                    self.keypath.write(','.join(extracted_keywords)+'\n')
                    print("append to dataset1")
                self.v_titles.append(page_title)
        self.visited+=urls
        if scraped_urls:
            self.run(list(set(scraped_urls)))

                

scrape=Scrape("lifehacker",'https://lifehacker.com/')
scrape.run(['https://lifehacker.com/'])
#scrape=Scrape("techcrunch",'https://techcrunch.com')
#scrape.run(['http://www.techcrunch.com'])

