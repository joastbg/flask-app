from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
    return render_template('index.html', headline="Most Recent Videos", page=1)
	
@app.route("/<page>", methods=['GET'])
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
	channels = ['Channel {0}'.format(x+1) for x in range(100)]
	h = {"headline": "Channels", "channels": channels}
	return render_template('channels.html', hash=h)
	
@app.route("/actors")
def pornstars():
    #return "Hello actors!"
	actors = ['Actor {0}'.format(x+1) for x in range(300)]
	h = {"headline": "Actors", "actors": actors}
	return render_template('actors.html', headline="Actors", hash=h)
	
@app.route("/search", methods=['POST'])
def search():
    q = request.values['q']

    return render_template('search.html', headline="Search", query=q)

if __name__ == "__main__":
	app.run(debug=True)
