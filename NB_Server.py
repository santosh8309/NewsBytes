from flask import Flask, request, render_template
import hashlib 
 
app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def main():
    return render_template("Index.html")
 
@app.route('/NewsBytesURLEncode', methods=["POST"])
def NewsBytesURLEncode():
	"""
	Using SHA256 hashing algorithm
	1.it is easy to compute the hash value for any given URL
	2.it is infeasible to generate a URL that has a given hash
	3.it is infeasible to modify a URL without changing the hash
	4.it is infeasible to find two different URLs with the same hash.
	"""
	text = request.form['URL']
	result = hashlib.sha256(text.encode())
	return("Hashed URL: "+format(result.hexdigest()))
  

if __name__ == '__main__':

	app.run(host='0.0.0.0',port=80)