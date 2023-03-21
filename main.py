from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    URL = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(URL)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('post.html', posts=all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)
