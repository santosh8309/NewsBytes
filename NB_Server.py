from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def main():
    print("Hello! You have arrived at a default page!")
 
@app.route('/NewsBytes', methods=["GET", "POST"])
def Encode_():
	print("Hello, Santosh!")
	return "True"

if __name__ == '__main__':

	app.run(host='0.0.0.0',port=8080)