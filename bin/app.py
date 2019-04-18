from flask import *
from figure.parabola import Parabola
import json

app = Flask(__name__)


@app.route("/")
def main():
	return "Welcome!"


@app.route("/figures")
def figures():
	return "Welcome!"


@app.route("/go/parabola", methods=['GET', 'POST'])
def go():
	q = Parabola()
	try:
		q.set_all(request.get_json())
		return json.dumps(q.calculate())
	except AttributeError:
		return 'Error: "application/JSON" Only'


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

#
#	@after_this_request
#	def add_header(response):
#		try:
#			response.set_cookie('a', str(int(request.cookies.get('a', ''))+1))
#		except ValueError:
#			response.set_cookie('a', str(0))
#
#		return response
#	request.accept_mimetypes.best_match([
#		'application/json'
#	])
