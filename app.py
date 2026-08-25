import os
from flask import Flask, render_template

app = Flask(__name__)

# DATA
PROFICIENCY = [
    {"name": "Python", "stars": 3.5}
    
]

PROJECTS = [
    {
        "title": "Workflewai",
        "category": "Editorial",
        "year": "2024",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAECKo7HUP0tU2nO5oLe1A8iq6DT-VEEpluqQjSvEmqDzzTceqY1fPOxJN9PxBa6aq4bguFfxE2tdTkhVUqc9vE94MY0sIpe7ddOz5JVSNprpoiC46pXtebmJaroWpKsFrQFUKO7md7efHFX2-oz7UrivofD0_mDoz9_5b3VUN2_k-mDMIAPZPZ-uPIfbEAnb_rEcfNcA9MaSsIQfyhBPIX63P1KFJ0BOnvctZM1uVt6gsBB3NUhpAYVcPD6PxIMfOh5_k_LRDooKI",
        "link": "https://workflewai.vercel.app"
    }
]

PHOTOGRAPHY_ROUTE_NAME = "photography"
PHOTOGRAPHY_LINK = f"/{PHOTOGRAPHY_ROUTE_NAME}"

SOCIAL_LINKS = {
    "instagram": "https://instagram.com/yourusername",
    "github": "https://github.com/yourusername"
}

@app.route('/')
def index():
    return render_template('index.html', 
                          proficiency=PROFICIENCY, 
                          projects=PROJECTS, 
                          photography_link=PHOTOGRAPHY_LINK,
                          social_links=SOCIAL_LINKS)



@app.route(f'/{PHOTOGRAPHY_ROUTE_NAME}')
def photography():
    return render_template('photography.html')

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)

app = app
