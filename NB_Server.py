from flask import Flask, request, render_template
import hashlib 
 
app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def main():
    return render_template("Index.html")
 
@app.route('/NewsBytesURLEncode', methods=["POST"])
def NewsBytesURLEncode():
	text = request.form['URL']
	result = hashlib.sha256(text.encode())
	return(result.hexdigest())
  

if __name__ == '__main__':

	app.run(host='0.0.0.0',port=8080)