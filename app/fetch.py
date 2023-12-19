import threading
import requests
from bs4 import BeautifulSoup
import time
from app.utils import timeit
    

class DomainCatcher:
    BASE_URL = "https://www.expireddomains.net/tld/"
    __HEADER = {
        "User-Agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Host"              : "www.expireddomains.net",
        "Accept-Language"   : "en-US,en;q=0.5",
        "Cache-Control"     : "no-cache",
             }
    
    def __init__(self, extensions:list):
        self.extensions = extensions
        self.contents = []
        self.tables = []
        self.url_list = self.get_url_list()
        self.__response = []

    
    @timeit
    def get_url_list(self):
        return list(map(lambda x: self.BASE_URL+x, self.extensions))
    
    def __get_content(self, url):
        resp = requests.get(url, headers=self.__HEADER)
        resp.raise_for_status()
        self.contents.append(resp.content)
        
    @timeit
    def get_contents(self):
        self.thread_func(self.__get_content, self.url_list)
    
    def __get_table(self, content):
        soup = BeautifulSoup(content, "html.parser")
        div = soup.find("div", id="listing")
        self.tables.extend(div.find("tbody").find_all("tr"))
        
    @timeit
    def get_tables(self):
        for content in self.contents:
            self.__get_table(content)
        
    
    def __parse(self, table):
        domain_response = {}
        domain_response["domain"] = self.parser_helper(table, "field_domain")
        domain_response["bl"] = self.parser_helper(table, "field_bl")
        domain_response["domain_pop"] = self.parser_helper(table, "field_domainpop")
        domain_response["abirth"] = self.parser_helper(table, "field_abirth")
        domain_response["status_com"] = self.parser_helper(table, "field_statuscom")
        domain_response["status_net"] = self.parser_helper(table, "field_statusnet")
        domain_response["status_org"] = self.parser_helper(table, "field_statusorg")
        domain_response["status_de"] = self.parser_helper(table, "field_statusde")
        # domain_response["status_ld_registered"] = self.parser_helper(table, "field_status_ld_registered")
        domain_response["related_cnobi"] = self.parser_helper(table, "field_related_cnobi")
        domain_response["changes"] = self.parser_helper(table, "field_changes")
        domain_response["whois"] = self.parser_helper(table, "field_whois")
        self.__response.append(domain_response)
    
    @staticmethod
    def parser_helper(table, class_name):
        return table.find("td", class_=class_name).text.strip()
    
    @timeit
    def parser(self):
        for table in self.tables:
            self.__parse(table)
    
    @staticmethod
    def thread_func(_func, _list):
        thread_list = [threading.Thread(target=_func, args=(x, )) for x in _list]

        for thread in thread_list:
            time.sleep(0.5)
            thread.start()

        for thread in thread_list:
            thread.join()
    
    @timeit  
    def run(self):
        self.get_contents()
        self.get_tables()
        self.parser()
        return self.__response
        
    
if __name__ == "__main__":
    scraper = DomainCatcher(["com", "net"])
    scraper.run()
    
        
        
        
        
        
    
    

