from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
    return render_template('index.html', headline="Most Recent Videos", page=1)
	
@app.route("/<page>")
def home_page(page):
    return render_template('index.html', headline="Most Recent Videos", page=int(float(page)))

@app.route("/videos")
def videos():
    #return "Hello videos!"
	return render_template('videos.html', headline="Videos")

@app.route("/video/<id>")
def video(id):
    #return "Hello videos!"	
	return render_template('video.html', headline="Videos", id=id)


@app.route("/categories")
def categories():
    #return "Hello categories!"
	return render_template('categories.html', headline="Categories")
	
@app.route("/channels")
def channels():
    #return "Hello channels!"
	return render_template('channels.html', headline="Channels")
	
@app.route("/actors")
def pornstars():
    #return "Hello actors!"
	return render_template('actors.html', headline="Actors")
	
@app.route("/search")
def search():
    #return "Hello search!"
	return render_template('search.html', headline="Search")

if __name__ == "__main__":
	app.run(debug=True)
