from flask import Flask, render_template, request
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import urllib.request as urllib2
import datetime

app = Flask(__name__)

#currently only j2 compatible
@app.route('/get_available_UT', methods=['GET', 'POST'])
def index():
	d = datetime.date.today()
	#url = "http://hf-food.austin.utexas.edu/foodpro/pickMenu2.asp?locationNum=12&locationName=Jester+2nd+Floor+Dining&dtdate=" + \
	#    str(d.month) + "%2F" + str(d.day) + "%2F" + str(d.year) + \
	#   "&mealName=Dinner&sName=The+University+of+Texas+at+Austin+%2D+Housing+and+Dining"
	month = "03"
	day = "27"
	year = "2019"
	url_j2 = "http://hf-food.austin.utexas.edu/foodpro/pickMenu2.asp?locationNum=12&locationName=Jester+2nd+Floor+Dining&dtdate=" + \
    	month + "%2F" + day + "%2F" + year + \
    	"&mealName=Dinner&sName=The+University+of+Texas+at+Austin+%2D+Housing+and+Dining"
	content = urllib2.urlopen(url_j2).read()
	soup = BeautifulSoup(content)
	for link in soup.find_all('a'):
		url2 = "http://hf-food.austin.utexas.edu/foodpro/" + link.get('href')
		r = requests.get(url2)
		food_soup = BeautifulSoup(r.text)
		print(food_soup.text)
		massage_html(food_soup)
	return 'success'

#parse usable data from BeautifulSoup object and create food objects
def massage_html(obj):
	nutrition_map = {}
	food_name = obj.find("div", {"class": "labelrecipe"})
	ingredients = obj.find("span", {"class": "labelingredientsvalue"})
	allergens = obj.find("span", {"class": "labelallergensvalue"})
	nutrition_info = obj.findAll("font")
	for loc in range(0, len(nutrition_info)):
		print('start of object' + str(loc))
		spec_info = nutrition_info[loc].get_text()
		spec_info.strip()
		print(spec_info)

		nutrition_map[]
	#food_name = obj.find("div", {"class": "labelrecipe"})
	#food_name = obj.find("div", {"class": "labelrecipe"})
	#food_name = obj.find("div", {"class": "labelrecipe"})
	#food_name = obj.find("div", {"class": "labelrecipe"})
	#food_name = obj.find("div", {"class": "labelrecipe"})




@app.route('/store_user_preferences', methods=['PUT'])
def update_preferences():
	return 'welcome'

@app.route('/new_user', methods=['PUT'])
def create_user():
	return 'welcome'

@app.route('/suggest_menu')
def return_menu():
	return 'welcome'

@app.route('/')
def route():
	return 'welcome'

class food_():
	def __init__(self, name, tag, image, nutrition_map, allergens, ingredients):
		self.name = name
		self.tag = tag
		self.image = image
		self.nutrition_map = nutrition_map
		self.allergens = allergens
		self.ingredients = ingredients

class user_():
	def __init__(self, name, id, email, goals, image, height, weight, bmi, university, allergies, preferences, diet_restricitions):
		self.name = name
		self.id = id
		self.email = email
		self.image = goals
		self.height = height
		self.weight = weight
		self.bmi = bmi
		self.university = university
		self.allergies = allergies
		self.preferences = preferences
		self.diet_restricitions = diet_restricitions
