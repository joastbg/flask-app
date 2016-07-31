from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
    return render_template('index.html', headline="Welcome to my page!")

@app.route("/videos")
def videos():
    return "Hello videos!"

@app.route("/categories")
def categories():
    return "Hello categories!"
	
@app.route("/channels")
def channels():
    return "Hello channels!"
	
@app.route("/pornstars")
def pornstars():
    return "Hello pornstars!"
	
@app.route("/search")
def search():
    return "Hello search!"

if __name__ == "__main__":
	app.run(debug=True)
