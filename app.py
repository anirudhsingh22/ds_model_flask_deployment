# Import Libraries
from flask import Flask, request
import pickle
# Create a Flask App
app = Flask(__name__)
# Create a method that responds to homepage request
@app.route('/', methods=['POST'])
def get_predictions():
	# Create Results Label
	result = ['setosa', 'versicolor', 'virginica']
	# Load the model
	model = pickle.load(open('model.pkl','rb'))
	# Get request data
	data = request.get_json()
	# get the Prediction
	index = int(model.predict([[
		data["sepal_length"],
		data["sepal_width"],
		data["petal_length"],
		data["petal_width"]
	]]))
	# return the predicted label
	return { 'predicton': result[index] }

