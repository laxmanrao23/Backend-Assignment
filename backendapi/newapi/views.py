from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup



# Create your views here.
def index(request):
    if request.method == "POST":
        country = request.POST.get('country')
        URL = 'https://en.wikipedia.org/wiki/' + country
        print(URL)
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')

        s = soup.find_all('a')[7]
        var1 = str(s)
        k_lst = var1.split("\"")
        flag_link = "https:" + str(k_lst[21].split(",")[0])
        print(flag_link)

        capitals = []
        s1 = soup.find_all('a')[25].text
        s1 = str(s1)
        capitals.append(s1)
        if len(capitals)>1:
            print(capitals)
        print(s1)

        largest_city = []
        s3 = soup.find_all('a')[27].text
        largest_city.append(s3)
        s4 = soup.find_all('a')[28].text 
        largest_city.append(s4)
        if len(largest_city)>1:
            print(largest_city)

        official_languages = []
        s5 = soup.find_all('a')[29].text 
        official_languages.append(s5)
        s6 = soup.find_all('a')[30].text
        official_languages.append(s6)
        if len(official_languages) > 1:
            print(official_languages)
       

        area_total = []
        s7 = soup.find_all('td')[28].text 
        s3 = s7.split(" ")
        s4 = str(s3[0])
        k_lst2 = []
        for i in s4:
            if i!='[':
                k_lst2.append(i)
            else:
                break
        print(k_lst2)
        s3 = ""
        for i in k_lst2:
            if i==',':
                continue
            s3 += i
        area_total = int(s3)
        print(area_total)

        population = ""
        s8 = soup.find_all('td')[30].text 
        s3  = str(s8)
        k_lst3 = []
        for i in s3:
            if i!="[":
                k_lst3.append(i)
            else:
                break
        s3 = ""
        for i in k_lst3:
            s3 += i
        population = str(s3)
        print(population)

        GDP_nominal = ""
        s9 = soup.find_all('td')[37].text 
        s3 = str(s9)
        k_lst4 = []
        for i in s3:
            if i!='[':
                k_lst4.append(i)
            else:
                break
        s3 = ""
        for i in k_lst4:
            s3 += i
        GDP_nominal = s3
        print(GDP_nominal)

        context = {}
        context = {'flag_link': flag_link, 'capital':capitals, 'largest_city': largest_city, 'official_languages': official_languages, 'area_total': area_total, 'Population': population, 'GDP_nominal': GDP_nominal}
        #print(context)
        json_object = json.dumps(context, indent = 4)
        
        print("JSON SCRAPING")
        print(json_object)



        return render(request, 'api.html')
    else:
        return render(request, 'api.html')