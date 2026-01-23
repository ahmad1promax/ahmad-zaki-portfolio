from flask import Flask, render_template, request, flash, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key-2024'

# بيانات الموقع (يمكن تحويلها لقاعدة بيانات لاحقاً)
SITE_DATA = {
    "name": "أحمد زكي",
    "title": "مطور ويب ومصمم واجهات",
    "email": "ahmed@example.com",
    "phone": "+20 100 000 0000",
    "location": "القاهرة، مصر",
    "bio": "مطور ويب متخصص في بناء تطبيقات ويب حديثة باستخدام Python وFlask. أحول الأفكار إلى واقع رقمي.",
    "years_experience": "3+",
    "projects_completed": "50+",
    "happy_clients": "40+"
}

PROJECTS = [
    {
        "id": 1,
        "title": "متجر إلكتروني",
        "description": "متجر إلكتروني متكامل مع نظام دفع وإدارة طلبات",
        "category": "Web App",
        "technologies": ["Python", "Flask", "JavaScript", "MySQL"],
        "image": "project1.jpg",
        "live_url": "https://example.com",
        "github_url": "https://github.com"
    },
    {
        "id": 2,
        "title": "منصة تعليمية",
        "description": "منصة للدورات التعليمية مع نظام متابعة الطلاب",
        "category": "Education",
        "technologies": ["Python", "Django", "React", "PostgreSQL"],
        "image": "project2.jpg",
        "live_url": "https://example.com",
        "github_url": "https://github.com"
    },
    {
        "id": 3,
        "title": "تطبيق إدارة المهام",
        "description": "تطبيق ويب لإدارة المهام والمشاريع الشخصية",
        "category": "Productivity",
        "technologies": ["Python", "Flask", "SQLite", "Bootstrap"],
        "image": "project3.jpg",
        "live_url": "https://example.com",
        "github_url": "https://github.com"
    }
]

SKILLS = [
    {"name": "Python", "level": 90, "category": "Backend"},
    {"name": "Flask/Django", "level": 85, "category": "Backend"},
    {"name": "JavaScript", "level": 80, "category": "Frontend"},
    {"name": "HTML/CSS", "level": 95, "category": "Frontend"},
    {"name": "SQL/MySQL", "level": 75, "category": "Database"},
    {"name": "Git/GitHub", "level": 85, "category": "Tools"},
    {"name": "Linux/Server", "level": 70, "category": "DevOps"},
    {"name": "UI/UX Design", "level": 65, "category": "Design"}
]

SERVICES = [
    {
        "icon": "💻",
        "title": "تطوير الويب",
        "description": "بناء تطبيقات ويب متكاملة ومواقع ديناميكية"
    },
    {
        "icon": "📱",
        "title": "تطبيقات متجاوبة",
        "description": "تصميم متجاوب يعمل على جميع الأجهزة"
    },
    {
        "icon": "🔧",
        "title": "صيانة المواقع",
        "description": "صيانة دورية وتحسين أداء المواقع"
    },
    {
        "icon": "🎨",
        "title": "تصميم واجهات",
        "description": "تصميم واجهات مستخدم جذابة وسهلة الاستخدام"
    }
]

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', 
                         data=SITE_DATA,
                         projects=PROJECTS[:3],
                         skills=SKILLS,
                         services=SERVICES,
                         current_year=current_year)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', 
                         projects=PROJECTS,
                         data=SITE_DATA)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', 
                             project=project,
                             data=SITE_DATA)
    return redirect(url_for('projects_page'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # هنا يمكن إضافة إرسال الإيميل أو حفظ في قاعدة بيانات
        flash('شكراً على رسالتك! سأرد عليك قريباً.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', data=SITE_DATA)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    # API endpoint للاتصال (للاستخدام مع JavaScript)
    data = request.json
    # معالجة البيانات هنا
    return {"message": "تم استلام رسالتك بنجاح", "status": "success"}

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=SITE_DATA), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', data=SITE_DATA), 500

# Context Processor لتمرير البيانات لكل الصفحات
@app.context_processor
def inject_data():
    return dict(data=SITE_DATA, current_year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
