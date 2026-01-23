from flask import Flask, render_template, request, jsonify, session
import random
from datetime import datetime
import os

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SESSION_PERMANENT'] = False

# ========== بيانات الموقع (تعدل هنا) ==========
PORTFOLIO_DATA = {
    "name": "Ahmad Zaki",
    "title": "Digital Creator & Full-Stack Developer",
    "tagline": "Crafting Digital Masterpieces",
    "email": "a7med1.zaki@gmail.com",  # ← غير الإيميل هنا
    "phone": "+7 918 578-69-26",  # ← غير الرقم هنا
    "location": "Global Nomad",
    "bio": "I create immersive digital experiences that blend art, technology, and innovation.",
    "years": "5+",
    "projects": "100+",
    "clients": "80+"
}

# ========== المشاريع الإبداعية ==========
CREATIVE_PROJECTS = [
    {
        "id": 1,
        "title": "Quantum Canvas",
        "category": "Interactive Art",
        "description": "AI-generated art platform with real-time collaboration",
        "tech": ["Python", "TensorFlow", "WebGL", "WebRTC"],
        "icon": "🎨",
        "image": "project1.jpg"  # ← ضع صورتك هنا: static/images/projects/project1.jpg
    }
]

# ========== تطبيقات مسلية ==========
ENTERTAINMENT_APPS = [
    {
        "name": "Code Symphony",
        "type": "Music Visualizer",
        "description": "Visualize code execution as music",
        "icon": "🎵",
        "link": "#"
    }
]

# ========== وسائل التواصل ==========
CONTACT_METHODS = [
    {
        "platform": "WhatsApp",
        "username": "+7 918 578-69-26",
        "link": "https://wa.me/79185786926",
        "icon": "whatsapp",
        "color": "#25D366"
    },
    {
        "platform": "Telegram",
        "username": "@ahmed_zaki",  # ← ضع يوزر تيليجرام الحقيقي
        "link": "https://t.me/ahmed_zaki",
        "icon": "telegram",
        "color": "#0088cc"
    },
    {
        "platform": "Email",
        "username": "a7med1.zaki@gmail.com",
        "link": "mailto:a7med1.zaki@gmail.com",
        "icon": "envelope",
        "color": "#EA4335"
    }
]

# ========== مقولات ملهمة ==========
INSPIRATIONAL_QUOTES = [
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "category": "Success"
    },
    {
        "text": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs",
        "category": "Innovation"
    }
]

@app.route('/')
def home():
    """الصفحة الرئيسية - هنا تعرض كل المحتوى"""
    return render_template('index.html',
                         data=PORTFOLIO_DATA,
                         projects=CREATIVE_PROJECTS,
                         apps=ENTERTAINMENT_APPS,
                         contacts=CONTACT_METHODS,
                         quotes=INSPIRATIONAL_QUOTES,
                         current_year=datetime.now().year)

# ========== مسارات API ==========
@app.route('/api/visitor')
def visitor_api():
    """API لحساب الزوار (اختياري)"""
    return jsonify({"visitors": random.randint(1000, 5000)})

@app.route('/api/quote')
def random_quote():
    """API للحصول على مقولة عشوائية"""
    quotes = INSPIRATIONAL_QUOTES
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
