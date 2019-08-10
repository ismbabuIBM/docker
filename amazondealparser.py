from flask import Flask
import bs4, requests

app = Flask(__name__)

@app.route("/")
def hello():
	print('')
	try:
		URL = input('Please enter URL of any Amazon Deal of the Day item: ')
		page = requests.get(URL)
		page.raise_for_status()
		
		soup = bs4.BeautifulSoup(page.text, 'html.parser') #defining Soup object
			
		#parsing product name & price using CSS Selector element
		nameElement = soup.select('#productTitle')
		dealPriceElement = soup.select('#priceblock_dealprice')
			
		#retrieving exact product name & price String strip method 
		proName = nameElement[0].text.strip()
		proDealPrice = dealPriceElement[0].text.strip()

		#return product name & price on screen
		return "<b>The Name of the Product is: </b>" + proName + " ...........& <b>It's in the Deal Price of: </b>"+ proDealPrice
	
	except:
		return "This is an invalid URL..." 

if __name__ == "__main__":
	app.run(host='0.0.0.0')

