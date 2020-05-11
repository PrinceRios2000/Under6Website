
from flask import Flask, render_template, url_for, redirect
from PIL import Image
app = Flask(__name__)

products = [
	{
		'id': 't-shirt.jpg',
		'product_name': 'Under6 T-Shirt',
		'price': '50.00 USD',
		'buy_now': 'Add to cart'
	}
]

lst = []

@app.route('/')
def home():
  return render_template('template.html')

@app.route('/shop')
def shop():
	return render_template('template2.html', dict = products)

@app.route('/cart')
def cart():
	return render_template('template3.html')

if __name__ == '__main__':
  app.run(debug=True)


