from flask import Flask
from flask import request
from flask import send_from_directory
from flask import render_template

app = Flask(__name__, static_url_path='')

subtitles = """Most recent, Most popular, Top rated, Longest, Shortest""".split(", ")

@app.route("/")
def home():	
    return render_template('index.html', headline="Most Recent Videos", 
                            page=1, subtitles=subtitles, subpage="most-recent")
	
@app.route("/<page>", methods=['GET'])
def home_page(page):
    return render_template('index.html', headline="Most Recent Videos", 
                            page=int(float(page)), subtitles=subtitles)

@app.route("/videos")
def videos():	
	return render_template('videos.html', headline="Videos", 
                            page=1, subtitles=subtitles, subpage="most-recent")
	
@app.route("/videos/<p>")
def videos_page(p):
	page = 1	
	try:
		page = int(float(p))
	except ValueError:
		return render_template('videos.html', headline="Videos", 
                                page=1, subtitles=subtitles, subpage=p)
	
	return render_template('videos.html', headline="Videos", 
                            page=int(float(p)), subtitles=subtitles, subpage="Most recent")
	
@app.route("/video/<id>")
def video(id):
	return render_template('video.html', headline="Videos", id=id)

@app.route("/categories")
def categories():
	return render_template('categories.html', headline="Categories")
	
@app.route("/channels")
def channels():
	channels = ['Channel {0}'.format(x+1) for x in range(100)]
	h = {"headline": "Channels", "channels": channels}
	return render_template('channels.html', hash=h)
	
@app.route("/actors")
def pornstars():
	actors = ['Actor {0}'.format(x+1) for x in range(120)]
	h = {"headline": "Actors", "actors": actors}
	return render_template('actors.html', headline="Actors", hash=h)
	
@app.route("/search", methods=['POST'])
def search():
    q = request.values['q']
    return render_template('search.html', headline="\"" + q + "\" Videos", query=q, page=1)

if __name__ == "__main__":
	app.run(debug=True)
