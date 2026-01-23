# ============================================================
# app.py
# Backend Python Flask for Ahmed Zaki Legendary Portfolio
# Author: Ahmed Zaki
# Purpose: Serve the frontend, provide API endpoints,
#          log visitors, and enable dynamic interaction
# ============================================================

from flask import Flask, render_template, jsonify, request
from datetime import datetime
import os

# ============================================================
# CREATE FLASK APP
# ============================================================
app = Flask(__name__)

# ============================================================
# ROUTE: HOME PAGE
# ============================================================
@app.route("/")
def home():
    """
    🔴 يعرض الصفحة الرئيسية index.html
    Frontend يستهلك هذا الملف
    """
    return render_template("index.html")


# ============================================================
# API: PROFILE DATA
# ============================================================
@app.route("/api/profile")
def profile():
    """
    🔴 يعرض بياناتك الشخصية
    يمكن استدعاؤها في core.js
    """
    data = {
        "name": "Ahmed Zaki",
        "email": "a7med1.zaki@gmail.com",
        "phone": "+79185786926",
        "fields": [
            "Design",
            "Animation",
            "Programming",
            "Artificial Intelligence"
        ],
        "vision": "Creativity is freedom. Technology is power."
    }
    return jsonify(data)


# ============================================================
# API: LOG VISITOR
# ============================================================
@app.route("/api/visit", methods=["POST"])
def visit():
    """
    🔴 تسجيل كل زيارة من لجنة المنح أو الزوار
    يتم الطباعة في الكونسول ويمكن لاحقًا تخزينها في قاعدة بيانات
    """
    visitor_ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("===================================")
    print("🚀 New Visitor Detected")
    print(f"IP Address: {visitor_ip}")
    print(f"Time: {timestamp}")
    print("===================================")

    # يمكن لاحقًا تخزين البيانات في ملف أو قاعدة بيانات
    return jsonify({"status": "logged", "ip": visitor_ip, "time": timestamp})


# ============================================================
# API: DYNAMIC PROJECTS (Optional)
# ============================================================
@app.route("/api/projects")
def projects():
    """
    🔴 API لإرسال المشاريع ديناميكيًا للواجهة
    يمكن تعديل أو إضافة مشاريع لاحقًا
    """
    project_list = [
        {
            "title": "Advanced AI Assistant",
            "desc": "An AI-based project enhancing creativity and productivity."
        },
        {
            "title": "Cinematic Motion Design",
            "desc": "A full animation project with storytelling through visuals."
        },
        {
            "title": "Web Platform UX",
            "desc": "Modern web platform focusing on performance and aesthetics."
        }
    ]
    return jsonify(project_list)


# ============================================================
# RUN APP
# ============================================================
if __name__ == "__main__":
    """
    🔴 يمكنك تشغيل التطبيق محليًا بـ:
        python app.py
    وسيعمل على http://127.0.0.1:5000
    عند رفعه على Render:
        استخدم Gunicorn أو إعدادات Render الافتراضية
    """
    app.run(debug=True, host="0.0.0.0", port=5000)
