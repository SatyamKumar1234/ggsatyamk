import os
from flask import Flask, render_template

# When app.py is in the root, Flask automatically finds templates and static folders
app = Flask(__name__)

# DATA FOR SATYAM KUMAR:
# Update these lists to change the content of your portfolio!
PROFICIENCY = [
    {"name": "Python", "stars": 2},
    {"name": "VibeCoding", "stars": 5}
]

PROJECTS = [
    {
        "title": "Workflewai",
        "category": "Editorial",
        "year": "2024",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAECKo7HUP0tU2nO5oLe1A8iq6DT-VEEpluqQjSvEmqDzzTceqY1fPOxJN9PxBa6aq4bguFfxE2tdTkhVUqc9vE94MY0sIpe7ddOz5JVSNprpoiC46pXtebmJaroWpKsFrQFUKO7md7efHFX2-oz7UrivofD0_mDoz9_5b3VUN2_k-mDMIAPZPZ-uPIfbEAnb_rEcfNcA9MaSsIQfyhBPIX63P1KFJ0BOnvctZM1uVt6gsBB3NUhpAYVcPD6PxIMfOh5_k_LRDooKI",
        "link": "https://workflewai.vercel.app"
    },
    {
        "title": "Aether Interface",
        "category": "Digital",
        "year": "2023",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBIdrXNHPWt9W_ExymxZG4AJ3_X2pRe5Yu8sm3Je9F2svIRnvKHHsnEfUhdhKpHgnMnzXWsJksov0wSFv4RVXt_DbmNv4JORE-rTPVb1aXENr4_N6t2o6XEPqkxV9xC9QQDN-aLyXvLlScBW7RSfwtBn0fjlbDeyoN-vOpxLiaAGikHKyM5t31lZ_TzCxDBtxXt8c8RQHt4FNneDeeq3nVI4ztvyNWnIeOZgOVM4qRZGbYB2CE5IN1r31Gnq3Lrqp-Ug-L0glq4_ak",
        "link": "https://example.com/aether"
    }
]

# PHOTOGRAPHY ROUTE SETTINGS
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


