from __future__ import print_function
from resteasy import RESTEasy
from flask import Flask

#Request jokes from endpoint
api = RESTEasy(base_url='http://api.icndb.com/jokes/random/')

#Flask server
app = Flask(__name__)


### Print 10 random jokes
jokes = api.route('jokes')
random = jokes.route('random')

#Creating endpoint to return 10 Chuck Norris jokes
@app.route('/getJokes')
def index():
	for i in range(10):
		return(random.get())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#http://127.0.0.1:5000/getJokes to view the output
