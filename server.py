from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    ran_num = random.randint(1, 10)
    
    today = datetime.datetime.now()
    current_year = today.year
    my_name = "Katy Smoot"
    return render_template('index.html', num=ran_num, current_year=current_year, my_name=my_name)

@app.route('/guess/<name>')
def guess_name(name):
    URLg = "https://api.genderize.io?name="
    URLa = "https://api.agify.io?name="
    gender_response = requests.get(URLg + name)
    age_response = requests.get(URLa + name)
    gen = gender_response.json()["gender"]
    age = age_response.json()["age"]
    return render_template('guess.html', name=name.title(), gender=gen, age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

@app.route('/post/<int:num>')
def get_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('post.html', posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)