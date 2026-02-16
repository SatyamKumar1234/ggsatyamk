import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ==========================================
# EDIT YOUR CONTENT HERE - EASY TO MODIFY
# ==========================================

# HERO SECTION
HERO_DATA = {
    "name": "Satyam Kumar",
    "tagline": "STUDENT AND DEVELOPER",
    "location": "Delhi, India",
    "intro": "Welcome to my portfolio! I am a passionate Student and Developer dedicated to building elegant digital experiences. I specialize in backend development and enjoy exploring the intersection of design and technology.",
    "cta_text": "View The Gallery",
    "cta_icon": "auto_stories"
}

# CRAFT/ABOUT SECTION
CRAFT_DATA = {
    "headline": "The Library of Skills",
    "description": "Crafting a digital experience requires more than just code. It requires an eye for composition, a hand for texture, and a heart for storytelling.",
    "quote": "Every pixel should feel like it was placed there by a human hand.",
    "specialty_title": "Built with Intention",
    "specialty_desc": "I specialize in creating websites that break the 'bootstrap' mold. My tools of choice include Tailwind CSS for styling, GSAP for fluid motion, and a healthy dose of hand-drawn SVGs.",
    "skills": [
        {"name": "UI Design", "icon": "draw"},
        {"name": "Frontend", "icon": "code"},
        {"name": "Narrative", "icon": "history_edu"},
        {"name": "Animation", "icon": "motion_mode"}
    ]
}

# PROFICIENCY/STARS (shared with main page)
PROFICIENCY = [
    {"name": "Python", "stars": 2},
    {"name": "VibeCoding", "stars": 5},
    {"name": "Flask", "stars": 3},
    {"name": "Tailwind CSS", "stars": 4}
]

# PROJECTS (shared with main page)
PROJECTS = [
    {
        "title": "Workflewai",
        "category": "Editorial",
        "year": "2024",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAECKo7HUP0tU2nO5oLe1A8iq6DT-VEEpluqQjSvEmqDzzTceqY1fPOxJN9PxBa6aq4bguFfxE2tdTkhVUqc9vE94MY0sIpe7ddOz5JVSNprpoiC46pXtebmJaroWpKsFrQFUKO7md7efHFX2-oz7UrivofD0_mDoz9_5b3VUN2_k-mDMIAPZPZ-uPIfbEAnb_rEcfNcA9MaSsIQfyhBPIX63P1KFJ0BOnvctZM1uVt6gsBB3NUhpAYVcPD6PxIMfOh5_k_LRDooKI",
        "link": "https://workflewai.vercel.app",
        "description": "An AI-powered workflow automation platform with elegant UI.",
        "tech": ["Vue.js", "GSAP"]
    },
    {
        "title": "Aether Interface",
        "category": "Digital",
        "year": "2023",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBIdrXNHPWt9W_ExymxZG4AJ3_X2pRe5Yu8sm3Je9F2svIRnvKHHsnEfUhdhKpHgnMnzXWsJksov0wSFv4RVXt_DbmNv4JORE-rTPVb1aXENr4_N6t2o6XEPqkxV9xC9QQDN-aLyXvLlScBW7RSfwtBn0fjlbDeyoN-vOpxLiaAGikHKyM5t31lZ_TzCxDBtxXt8c8RQHt4FNneDeeq3nVI4ztvyNWnIeOZgOVM4qRZGbYB2CE5IN1r31Gnq3Lrqp-Ug-L0glq4_ak",
        "link": "https://example.com/aether",
        "description": "Experimental UI kit for immersive web experiences.",
        "tech": ["Three.js", "Tailwind"]
    },
    {
        "title": "Cartographer's UI",
        "category": "Tools",
        "year": "2024",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop",
        "link": "#",
        "description": "Custom map components for adventurous developers.",
        "tech": ["React", "SVG"]
    }
]

# SOCIAL LINKS
SOCIAL_LINKS = {
    "instagram": "https://instagram.com/yourusername",
    "github": "https://github.com/yourusername",
    "twitter": "https://twitter.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername"
}

# CONTACT INFO
CONTACT_DATA = {
    "email": "hello@satyamkumar.dev",
    "footer_text": "Hand-coded with curiosity and a lot of chai."
}

# NAVIGATION
PHOTOGRAPHY_ROUTE_NAME = "photography"
PHOTOGRAPHY_LINK = f"/{PHOTOGRAPHY_ROUTE_NAME}"

# ==========================================
# ROUTES
# ==========================================

@app.route('/')
def index():
    """Original dark snow theme"""
    return render_template('index.html', 
                          proficiency=PROFICIENCY, 
                          projects=PROJECTS, 
                          photography_link=PHOTOGRAPHY_LINK,
                          social_links=SOCIAL_LINKS,
                          hero=HERO_DATA)

@app.route('/alternative')
def alternative():
    """Storybook warm theme"""
    return render_template('alternative.html',
                          proficiency=PROFICIENCY,
                          projects=PROJECTS,
                          photography_link=PHOTOGRAPHY_LINK,
                          social_links=SOCIAL_LINKS,
                          hero=HERO_DATA,
                          craft=CRAFT_DATA,
                          contact=CONTACT_DATA)

@app.route(f'/{PHOTOGRAPHY_ROUTE_NAME}')
def photography():
    return render_template('photography.html')

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
