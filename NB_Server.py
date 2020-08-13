from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def main():
    print("Hello! You have arrived at a default page!")
 
@app.route('/NewsBytes')
def Encode_():
	print("Hello, Santosh!")

if __name__ == '__main__':

	app.run(debug=True,port=80)