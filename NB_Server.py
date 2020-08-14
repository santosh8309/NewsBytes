from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def main():
    print("Hello! You have arrived at a default page!")
 
@app.route('/NewsBytes', methods=["GET", "POST"])
def Encode_():
	
	return render_template("Index.html")

if __name__ == '__main__':

	app.run(host='0.0.0.0',port=80)