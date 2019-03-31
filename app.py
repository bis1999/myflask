from flask import Flask,render_template,request
from datetime import datetime 


# App is an object 
#
app = Flask(__name__)





@app.route("/")
def index():
	return "Welcome"

@app.route("/hello")
def hello():
	print(request.args)
	naam= "Bisman"
	data = [
	        ["Ram",9,9],
	        ["Shayam",10,9],
	        ["Ravi",9,7]]

	colors = ["red","green","blue"]

	

	return render_template("test.html",name = naam,
		now = datetime.now(),
		data = data,colors = colors)


@app.route("/form",methods = ["GET","POST"])
def submit_data():
	if request.method == "GET":
		return render_template("form.html")

	else:
		name = request.form.get("name")
		clas = request.form.get("class")
		image = request.files.get("image")
		ext = image.filename.split(".")[-1]
		image.save("static/images/{}.{}".format(name,ext))
		return "your name is {} and class is {}".format(name,clas)







if __name__ == "__main__":
	app.run(use_reloader = True,debug = True )
