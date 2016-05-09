from flask import Flask
appp = Flask(__name__)

@appp.route("/")
def hello():
	return 'Lets try'

if __name__ == "__main__":
	appp.run()
