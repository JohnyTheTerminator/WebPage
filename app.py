from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('hero.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/story-time')
def story_time():
    return render_template('story_time.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/credentials')
def credentials():
    return render_template('credentials.html')

@app.route('/data-game')
def data_game():
    return render_template('data_game.html')

if __name__ == '__main__':
    app.run(debug=True)
