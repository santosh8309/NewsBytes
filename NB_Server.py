from flask import Flask, request, render_template
 
app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def main():
    return render_template("Index.html")
 
@app.route('/NewsBytes', methods=["GET", "POST"])
def Encode_():
	text = request.form['URL']
	processed_text = text.upper()
	return processed_text

if __name__ == '__main__':

	app.run(host='0.0.0.0',port=80)