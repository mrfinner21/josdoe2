import requests
from bs4 import BeautifulSoup

address_list = open("C:\\Users\\josem\\Desktop\\btcadresses.txt")
n = 7429847930984782098478524688

while True:
    n += 1
    print(n)
    page = requests.get("https://lbc.cryptoguru.org/dio/" + str(n))
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in range(7,263,2):
         ads = list(list(soup.body)[9])[i].get_text().split()[2:]
         for t in address_list:
             if t[:-1] in ads:
                 print(str(n) + str(t))
                 file = open("plutus.txt","a")
                 fiile.write(str(n), + " " + str(t))
                 file.close()

        
    


    
