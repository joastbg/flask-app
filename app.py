from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
    return render_template('index.html', headline="Welcome to my page!")

@app.route("/videos")
def videos():
    #return "Hello videos!"
	return render_template('index.html', headline="Videos")


@app.route("/categories")
def categories():
    #return "Hello categories!"
	return render_template('index.html', headline="Categories")
	
@app.route("/channels")
def channels():
    #return "Hello channels!"
	return render_template('index.html', headline="Channels")
	
@app.route("/actors")
def pornstars():
    #return "Hello actors!"
	return render_template('index.html', headline="Actors")
	
@app.route("/search")
def search():
    #return "Hello search!"
	return render_template('index.html', headline="Search")

if __name__ == "__main__":
	app.run(debug=True)
