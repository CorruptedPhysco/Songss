from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Mock database for songs
songs = []

# Route for viewers to see the songs
@app.route('/')
def index():
    return render_template('index.html', songs=songs)

# Admin route to add new songs
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        song_name = request.form['song']
        songs.append(song_name)
        return redirect(url_for('index'))
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)
  
