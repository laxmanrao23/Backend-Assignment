# Backend with Django, RestApi

Step 1: Created a virtual environment named “backendproject”.
--> py -m venv backendproject   #Venv Create
--> backendproject\Scripts\activate.bat   #Venv Activated
Step 2: Install all the packages in virtual environment required using pip.
1.	Django
2.	BeautifulSoap4
3.	Requests
4.	Json
5.	Djangorestframework
Step 3: Create a project named “backendapi”.
--> python -m django startproject RestApi
--> cd backednapi
Step 4: Create an app named “newapi”.
--> python -m django startapp newapi
Step 5: Verification of Project.
--> Python manage.py runserver
Step 6: Create the template folder and make necessary changes in settings.py file.
Step 7: Modify the urls.py and views.py to render the HTML file in template.
Step 8: Enter the country name in field of the HTML file and search.
Step 9: Retrieve the data through scraping in views.py in dictionary format.
Step 10: Convert the dictionary into JSON format.
--> context = {}
--> context = {'flag_link': flag_link, 'capital':capitals, 'largest_city': largest_city, 'official_languages': official_languages, 'area_total': area_total, 'population': population, 'GDP_nominal': GDP_nominal}
--> json_object = json.dumps(context, indent = 4)
Step 11: Print the JSON output in CMD.
Step 12: Freeze the requirements of the project in virtual environment.

