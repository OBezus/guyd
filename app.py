from flask import Flask
app = Flask(__name__)

@appp.route("/")
def hello():
	return 'Lets try'

if __name__ == "__main__":
	app.run()
