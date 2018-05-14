import os
import json
import requests
import urllib3

from flask import Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def Welcome():
	return render_template('index.htm')

@app.route('/score', methods=['GET', 'POST'])
def process_form_data():
	# Get the form data - result will contian all elements from the HTML form that was just submitted
	result = request.form

	#
	# The following lines are exactly the python code example form the Watson Machine Learning page
	#
	wml_credentials = {
	  "url": "https://ibm-watson-ml.mybluemix.net",
	  "access_key": "XXXXXXXXXXX",
	  "username": "XXXXXXXXXXX",
	  "password": "XXXXXXXXXXX",
	  "instance_id": "XXXXXXXXXXX"
	}

	scoring_endpoint = "https://ibm-watson-ml.mybluemix.net/v3/wml_instances/3423aa28-09e1-4287-985a-1e77f6018a5f/published_models/158537aa-fc60-488e-a2c5-36cea66cbfb3/deployments/1fde8fcc-7321-4d04-8e22-f6ebe313140d/online"

	headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
	url = '{}/v3/identity/token'.format(wml_credentials['url'])
	response = requests.get(url, headers=headers)

	mltoken = json.loads(response.text).get('token')

	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

	#
	# Here the example code is slightly modified. The input from the form is send.
	# (!) No checks on data is done here.
	#
	payload_scoring = {"values": [[result["mts2"], result["rooms"], result["distance_to_centre"], result["sauna"]]]}

	response_scoring = requests.post('https://ibm-watson-ml.mybluemix.net/v3/wml_instances/3423aa28-09e1-4287-985a-1e77f6018a5f/published_models/158537aa-fc60-488e-a2c5-36cea66cbfb3/deployments/1fde8fcc-7321-4d04-8e22-f6ebe313140d/online', json=payload_scoring, headers=header)
	
	# The result is send back as JSON. 
	#
	return jsonify( json.loads(response_scoring.text)) 
	
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
