# أضف في HTML_TEMPLATE بعد الـ Hero
'''
<!-- 🎯 Call to Action Section -->
<section class="section" style="background: var(--gradient-premium);">
    <div class="container" style="text-align: center;">
        <h2 style="color: white; font-size: 3.5rem; margin-bottom: 40px;">
            {{ "Ready to Transform Your Vision?" if g.current_lang == "en" else "جاهز لتحويل رؤيتك؟" }}
        </h2>
        <p style="color: white; font-size: 1.8rem; max-width: 800px; margin: 0 auto 60px;">
            {{ "Let's collaborate on your next groundbreaking project. Contact me now for elite-level consultation." if g.current_lang == "en" else "لنتعاون في مشروعك القادم الرائد. تواصل معي الآن للحصول على استشارة نخبوية." }}
        </p>
        <a href="#contact" class="btn" style="background: white; color: black; font-size: 1.5rem; padding: 25px 60px;">
            <i class="fas fa-rocket"></i>
            {{ "Start Project" if g.current_lang == "en" else "ابدأ المشروع" }}
        </a>
    </div>
</section>
'''
"""  لذلك اريد منك ان يكون الموقع باللغه الانجليزيه والعربيه فقط مع التاكد من اصلاح واضافه اي مصطلح.. مع الاخذ ف الاعتبار بتعديل الايقونه التي تغطي ع شعار التاج ,, واريد منك بعض الالوان الاخري مثل الاسود والذهبي والفضي بشكل مبدع , وساترك لي الاختيار باضافه بعض الخصائص الاخري التي تزيد من لمعان الموقع وبريقه , ويمكن ان تضع صوره جيفارا بشكل ملائم للتعويض عن صورتي وتكون بصيغه كاريزمااكمل لي هذا الموقع بتاء ع تلك التعليمات 
============================================================
✨ AHMAD ZAKI - ELITE PORTFOLIO MASTERPIECE ✨
موقع بورتفوليو نخبوي يجمع بين الفخامة والإبداع
============================================================
✅ لغتان فقط: English, العربية - للتأكد من الكمال
✅ تصميم فاخر بألوان الذهب والفضي والأسود
✅ أقسام متكاملة مع لمسات إبداعية
✅ أدوات تفاعلية مذهلة
✅ شخصية كاريزمية فريدة
============================================================
"""

from flask import Flask, render_template_string, request, jsonify, session, g
from datetime import datetime
import random
import json
import os
app = Flask(__name__)
app.secret_key = 'ahmad_zaki_elite_portfolio_2024_gold_edition'

# ============================================================
# 👑 معلومات المستخدم النخبوية - يمكنك التعديل هنا 👑
# ============================================================
USER_INFO = {
    "name": "AHMAD ZAKI",
    "arabic_name": "أحمد زكي",
    "title": "Visionary Creator & AI Maestro",
    "phone": "+79185786926",
    "email": "a7med1.zaki@gmail.com",
    "whatsapp": "+79185786926",
    "telegram": "@ahmadzaki",
    "location": "Global Visionary",
    "quote": "Where Innovation Meets Excellence",
    "website_name": "ZAKI | الذهبية"
}

# ============================================================
# 🌍 إعدادات اللغات - لغتان فقط للكمال 🌍
# ============================================================
LANGUAGES = [
    {"code": "en", "name": "English", "flag": "🇬🇧", "dir": "ltr"},
    {"code": "ar", "name": "العربية", "flag": "🇸🇦", "dir": "rtl"}
]

# ============================================================
# 🎯 المشاريع النخبوية - أضف مشاريعك الخاصة هنا 🎯
# ============================================================
PROJECTS = [
    {
        "id": 1,
        "title_en": "Golden AI Symphony",
        "title_ar": "سمفونية الذهب بالذكاء الاصطناعي",
        "category": "ai_art",
        "description_en": "AI-powered art installation blending 24K gold aesthetics with neural networks",
        "description_ar": "تركيب فني بتقنية الذكاء الاصطناعي يدمج جماليات الذهب عيار 24 مع الشبكات العصبية",
        "technologies": ["Python", "TensorFlow", "Neural Art", "3D Printing", "Gold Plating"],
        "year": "2024",
        "color": "#D4AF37",  # ذهبي
        "icon": "👑🤖"
    },
    {
        "id": 2,
        "title_en": "Silver Screen Masterpiece",
        "title_ar": "تحفة الشاشة الفضية",
        "category": "film",
        "description_en": "Award-winning short film with cinematic excellence and emotional depth",
        "description_ar": "فيلم قصير حائز على جوائز بتميز سينمائي وعمق عاطفي",
        "technologies": ["Cinema 4D", "After Effects", "DaVinci Resolve", "Dolby Atmos"],
        "year": "2023",
        "color": "#C0C0C0",  # فضي
        "icon": "🎬✨"
    },
    {
        "id": 3,
        "title_en": "Quantum Black Security",
        "title_ar": "الأمن الكمي الأسود",
        "category": "security",
        "description_en": "Military-grade encryption system using quantum computing and blockchain",
        "description_ar": "نظام تشفير عسكري المستوى باستخدام الحوسبة الكمومية وسلسلة الكتل",
        "technologies": ["Quantum Computing", "Blockchain", "C++", "Cryptography"],
        "year": "2024",
        "color": "#000000",  # أسود
        "icon": "🖤⚛️"
    },
    {
        "id": 4,
        "title_en": "Platinum UI Revolution",
        "title_ar": "ثورة واجهة البلاتين",
        "category": "design",
        "description_en": "Luxury user interface design for elite banking and finance applications",
        "description_ar": "تصميم واجهة مستخدم فاخرة لتطبيقات البنوك والتمويل النخبوية",
        "technologies": ["Figma", "React", "WebGL", "Motion Design"],
        "year": "2024",
        "color": "#E5E4E2",  # بلاتيني
        "icon": "💎🎨"
    },
    {
        "id": 5,
        "title_en": "Diamond Data Analytics",
        "title_ar": "تحليل بيانات الألماس",
        "category": "data_science",
        "description_en": "Cutting-edge data visualization platform for financial markets",
        "description_ar": "منصة تصور بيانات متطورة للأسواق المالية",
        "technologies": ["Python", "D3.js", "Machine Learning", "Big Data"],
        "year": "2023",
        "color": "#B9F2FF",  # ألماسي
        "icon": "💎📊"
    }
]

# ============================================================
# 🎨 التصاميم الفاخرة - أضف تصاميمك الخاصة هنا 🎨
# ============================================================
DESIGNS = [
    {
        "id": 1,
        "title_en": "Royal Brand Identity",
        "title_ar": "هوية العلامة الملكية",
        "type": "branding",
        "description_en": "Complete luxury brand system for royal clients",
        "description_ar": "نظام علامة تجارية فاخرة كامل للعملاء الملكيين",
        "tools": ["Illustrator", "Photoshop", "After Effects", "Blender"],
        "color": "#D4AF37"
    },
    {
        "id": 2,
        "title_en": "Elite Mobile Banking UI",
        "title_ar": "واجهة مصرفية نخبوية للجوال",
        "type": "ui_ux",
        "description_en": "Premium mobile banking interface for high-net-worth individuals",
        "description_ar": "واجهة مصرفية جوال متميزة للأفراد ذوي الثروات العالية",
        "tools": ["Figma", "Principle", "Swift", "Kotlin"],
        "color": "#000000"
    }
]

# ============================================================
# 🎬 الإبداعات السينمائية - أضف أفلامك هنا 🎬
# ============================================================
ANIMATIONS = [
    {
        "id": 1,
        "title_en": "Legacy of Visionaries",
        "title_ar": "إرث الرؤى",
        "type": "documentary",
        "description_en": "Documentary about revolutionary thinkers who changed the world",
        "description_ar": "فيلم وثائقي عن المفكرين الثوريين الذين غيروا العالم",
        "duration": "45:00",
        "tools": ["Premiere Pro", "After Effects", "Cinema 4D", "Color Grading"],
        "color": "#D4AF37"
    },
    {
        "id": 2,
        "title_en": "The Golden Ratio in Motion",
        "title_ar": "النسبة الذهبية في الحركة",
        "type": "motion_graphics",
        "description_en": "Animated exploration of mathematical beauty in nature and art",
        "description_ar": "استكشاف متحرك للجمال الرياضي في الطبيعة والفن",
        "duration": "8:30",
        "tools": ["After Effects", "Mathematica", "3D Animation", "Sound Design"],
        "color": "#C0C0C0"
    }
]

# ============================================================
# 💎 المهارات النخبوية - عدّل مهاراتك هنا 💎
# ============================================================
SKILLS = {
    "creative_excellence": [
        {"name": "Cinematic Direction", "level": 96, "icon": "🎬"},
        {"name": "Luxury Brand Design", "level": 94, "icon": "👑"},
        {"name": "3D Animation Mastery", "level": 92, "icon": "🎥"},
        {"name": "Visual Storytelling", "level": 95, "icon": "📖"}
    ],
    "technical_mastery": [
        {"name": "AI & Machine Learning", "level": 93, "icon": "🤖"},
        {"name": "Quantum Computing", "level": 88, "icon": "⚛️"},
        {"name": "Cybersecurity Elite", "level": 91, "icon": "🔐"},
        {"name": "Blockchain Development", "level": 89, "icon": "⛓️"}
    ],
    "strategic_vision": [
        {"name": "Innovation Strategy", "level": 95, "icon": "🚀"},
        {"name": "Digital Transformation", "level": 92, "icon": "💡"},
        {"name": "Global Communications", "level": 94, "icon": "🌍"},
        {"name": "Leadership & Mentoring", "level": 93, "icon": "👨‍💼"}
    ]
}

# ============================================================
# 📜 الشهادات النخبوية - أضف شهاداتك هنا 📜
# ============================================================
CERTIFICATIONS = [
    {
        "title_en": "Elite AI Architect Certification",
        "title_ar": "شهادة مهندس الذكاء الاصطناعي النخبوي",
        "issuer": "MIT Artificial Intelligence",
        "year": "2024",
        "credential": "AI-ELITE-2024-MIT"
    },
    {
        "title_en": "Master Creative Director",
        "title_ar": "المخرج الإبداعي الرئيسي",
        "issuer": "Hollywood Film Institute",
        "year": "2023",
        "credential": "MCD-2023-HFI"
    },
    {
        "title_en": "Quantum Security Specialist",
        "title_ar": "أخصائي الأمن الكمي",
        "issuer": "CERN Security Division",
        "year": "2023",
        "credential": "QSS-2023-CERN"
    },
    {
        "title_en": "Luxury Brand Strategist",
        "title_ar": "استراتيجي العلامات التجارية الفاخرة",
        "issuer": "LVMH Excellence Program",
        "year": "2024",
        "credential": "LBS-2024-LVMH"
    }
]

# ============================================================
# 🏆 الإنجازات البارزة - أضف إنجازاتك هنا 🏆
# ============================================================
ACHIEVEMENTS = [
    {
        "title_en": "Global Innovation Award 2024",
        "title_ar": "جائزة الابتكار العالمية 2024",
        "description_en": "Recognized for groundbreaking work in AI-art fusion",
        "description_ar": "تم التكريم لعمل رائد في دمج الذكاء الاصطناعي والفن",
        "year": "2024",
        "icon": "🏆"
    },
    {
        "title_en": "Forbes 30 Under 30 - Technology",
        "title_ar": "فوربس 30 تحت 30 - التكنولوجيا",
        "description_en": "Selected as one of the most influential young tech innovators",
        "description_ar": "تم الاختيار كأحد أكثر المبتكرين الشباب تأثيراً في التكنولوجيا",
        "year": "2023",
        "icon": "⭐"
    },
    {
        "title_en": "Cannes Lions Grand Prix",
        "title_ar": "الجائزة الكبرى لمهرجان كان",
        "description_en": "Highest honor at the world's most prestigious creative festival",
        "description_ar": "أعلى شرف في أعرس مهرجان إبداعي في العالم",
        "year": "2023",
        "icon": "🦁"
    }
]

# ============================================================
# 💬 اقتباسات العظماء - أضف اقتباساتك المفضلة 💬
# ============================================================
QUOTES = [
    {
        "text_en": "The question isn't who is going to let me; it's who is going to stop me.",
        "text_ar": "السؤال ليس من سوف يسمح لي؛ بل من سوف يمنعني.",
        "author": "Ayn Rand",
        "color": "#D4AF37"
    },
    {
        "text_en": "The only way to do great work is to love what you do.",
        "text_ar": "الطريقة الوحيدة للقيام بعمل عظيم هي أن تحب ما تفعله.",
        "author": "Steve Jobs",
        "color": "#000000"
    },
    {
        "text_en": "Innovation distinguishes between a leader and a follower.",
        "text_ar": "الابتكار يميز بين القائد والتابع.",
        "author": "Steve Jobs",
        "color": "#C0C0C0"
    },
    {
        "text_en": "The future belongs to those who prepare for it today.",
        "text_ar": "المستقبل ينتمي لأولئك الذين يستعدون له اليوم.",
        "author": "Malcolm X",
        "color": "#D4AF37"
    },
    {
        "text_en": "Be the change that you wish to see in the world.",
        "text_ar": "كن التغيير الذي تريد أن تراه في العالم.",
        "author": "Mahatma Gandhi",
        "color": "#C0C0C0"
    },
    {
        "text_en": "The journey of a thousand miles begins with one step.",
        "text_ar": "رحلة الألف ميل تبدأ بخطوة واحدة.",
        "author": "Lao Tzu",
        "color": "#D4AF37"
    }
]

# ============================================================
# 🌈 نظام الألوان الفاخر - الذهب والفضي والأسود 🌈
# ============================================================
COLOR_PALETTE = {
    "primary": "#000000",          # أسود عميق
    "secondary": "#1A1A1A",        # أسود فاتح
    "accent_gold": "#D4AF37",      # ذهبي كلاسيكي
    "accent_gold_light": "#FFD700", # ذهبي لامع
    "accent_silver": "#C0C0C0",    # فضي
    "accent_silver_dark": "#A9A9A9", # فضي داكن
    "accent_platinum": "#E5E4E2",  # بلاتيني
    "accent_diamond": "#B9F2FF",   # ألماسي
    "light": "#F5F5F5",            # فاتح جداً
    "dark": "#121212",             # داكن
    "success": "#2ECC71",          # أخضر
    "warning": "#F39C12",          # برتقالي
    "danger": "#E74C3C",           # أحمر
    "gradient_gold": "linear-gradient(135deg, #D4AF37, #FFD700, #FFED4E)",
    "gradient_silver": "linear-gradient(135deg, #C0C0C0, #E5E4E2, #FFFFFF)",
    "gradient_black": "linear-gradient(135deg, #000000, #1A1A1A, #2C2C2C)",
    "gradient_premium": "linear-gradient(135deg, #000000, #D4AF37, #C0C0C0)"
}

# ============================================================
# 🔧 الأدوات التفاعلية الفاخرة - أضف أدواتك الخاصة 🔧
# ============================================================
TOOLS = [
    {
        "name": "Golden Color Harmony",
        "icon": "🎨",
        "description_en": "Create stunning gold-based color palettes",
        "description_ar": "إنشاء لوحات ألوان مذهلة قائمة على الذهب"
    },
    {
        "name": "Luxury Font Pairing",
        "icon": "🔤",
        "description_en": "Discover perfect font combinations for luxury designs",
        "description_ar": "اكتشاف تركيبات الخطوط المثالية للتصاميم الفاخرة"
    },
    {
        "name": "Elite Calculator",
        "icon": "🧮",
        "description_en": "Premium calculator with currency and unit conversions",
        "description_ar": "آلة حاسبة متميزة مع تحويل العملات والوحدات"
    },
    {
        "name": "Vision Board Creator",
        "icon": "✨",
        "description_en": "Create digital vision boards for your projects",
        "description_ar": "إنشاء لوحات رؤية رقمية لمشاريعك"
    },
    {
        "name": "Creative Timer",
        "icon": "⏱️",
        "description_en": "Pomodoro timer optimized for creative work",
        "description_ar": "مؤقت بومودورو محسّن للعمل الإبداعي"
    }
]

# ============================================================
# 👑 نبذة عني النخبوية - عدّل النبذة كما تريد 👑
# ============================================================
ABOUT_ME = {
    "intro_en": "I am a visionary creator who transcends conventional boundaries, merging artistic brilliance with technological mastery to craft experiences that redefine excellence.",
    "intro_ar": "أنا مبدع رؤيوي يتجاوز الحدود التقليدية، دمجاً للروعة الفنية مع الإتقان التكنولوجي لصنع تجارب تعيد تعريف التميز.",
    
    "passion_en": "My passion is creating digital masterpieces that blend luxury aesthetics with cutting-edge functionality. I believe in creating work that not only performs flawlessly but also inspires awe.",
    "passion_ar": "شغفي هو خلق تحف رقمية تدمج بين جماليات الفخامة والوظائف المتطورة. أؤمن بخلق عمل لا يعمل بشكل لا تشوبه شائبة فحسب، بل يلهم الرهبة أيضاً.",
    
    "skills_en": "I combine elite expertise in cinematic direction, AI innovation, quantum security, and luxury branding. My diverse skill set allows me to approach challenges with unparalleled creativity and precision.",
    "skills_ar": "أجمع بين الخبرة النخبوية في الإخراج السينمائي، ابتكار الذكاء الاصطناعي، الأمن الكمي، والعلامات التجارية الفاخرة. مجموعتي المتنوعة من المهارات تسمح لي بمواجهة التحديات بإبداع ودقة لا مثيل لهما.",
    
    "vision_en": "My vision is to pioneer the future of creative technology, building solutions that elevate human experience while maintaining the highest standards of excellence and innovation.",
    "vision_ar": "رؤيتي هي ريادة مستقبل التكنولوجيا الإبداعية، بناء حلول ترفع من تجربة الإنسان مع الحفاظ على أعلى معايير التميز والابتكار."
}

# ============================================================
# 🎭 الترجمات الكاملة للغتين - عدّل النصوص كما تريد 🎭
# ============================================================
TRANSLATIONS = {
    "en": {
        "nav_home": "Home",
        "nav_about": "About Me",
        "nav_projects": "Projects",
        "nav_designs": "Designs",
        "nav_animations": "Cinema",
        "nav_skills": "Skills",
        "nav_certificates": "Certificates",
        "nav_achievements": "Achievements",
        "nav_tools": "Tools",
        "nav_contact": "Contact",
        
        "hero_title": "AHMAD ZAKI",
        "hero_subtitle": "Where Innovation Meets Excellence",
        "hero_description": "Visionary Creator & AI Maestro crafting digital masterpieces",
        
        "sections_about_me": "About Me",
        "sections_featured_projects": "Featured Projects",
        "sections_creative_designs": "Creative Designs",
        "sections_animated_creations": "Cinematic Works",
        "sections_technical_skills": "Technical Skills",
        "sections_certifications": "Certifications",
        "sections_achievements": "Achievements",
        "sections_interactive_tools": "Interactive Tools",
        "sections_inspirational_quotes": "Inspirational Quotes",
        "sections_contact_me": "Get In Touch",
        
        "buttons_view_project": "View Project",
        "buttons_view_design": "View Design",
        "buttons_watch_video": "Watch Film",
        "buttons_contact_me": "Contact Me",
        "buttons_download_cv": "Download CV",
        "buttons_send_message": "Send Message",
        "buttons_get_quote": "New Quote",
        "buttons_try_tool": "Try Tool",
        "buttons_view_all": "View All",
        
        "contact_phone": "Phone",
        "contact_email": "Email",
        "contact_whatsapp": "WhatsApp",
        "contact_telegram": "Telegram",
        "contact_copy": "Click to copy",
        "contact_name": "Name",
        "contact_subject": "Subject",
        "contact_message": "Message",
        
        "footer_quick_links": "Quick Links",
        "footer_stay_connected": "Stay Connected",
        "footer_rights": "All rights reserved",
        "footer_made_with": "Crafted with",
        "footer_passion": "Excellence in every pixel"
    },
    "ar": {
        "nav_home": "الرئيسية",
        "nav_about": "عني",
        "nav_projects": "المشاريع",
        "nav_designs": "التصاميم",
        "nav_animations": "الأفلام",
        "nav_skills": "المهارات",
        "nav_certificates": "الشهادات",
        "nav_achievements": "الإنجازات",
        "nav_tools": "الأدوات",
        "nav_contact": "تواصل",
        
        "hero_title": "أحمد زكي",
        "hero_subtitle": "حيث يلتقي الابتكار بالتميز",
        "hero_description": "مبدع رؤيوي ومعلم الذكاء الاصطناعي يصنع تحفاً رقمية",
        
        "sections_about_me": "عني",
        "sections_featured_projects": "المشاريع المميزة",
        "sections_creative_designs": "التصاميم الإبداعية",
        "sections_animated_creations": "الأعمال السينمائية",
        "sections_technical_skills": "المهارات التقنية",
        "sections_certifications": "الشهادات",
        "sections_achievements": "الإنجازات",
        "sections_interactive_tools": "الأدوات التفاعلية",
        "sections_inspirational_quotes": "اقتباسات ملهمة",
        "sections_contact_me": "تواصل معي",
        
        "buttons_view_project": "عرض المشروع",
        "buttons_view_design": "عرض التصميم",
        "buttons_watch_video": "مشاهدة الفيلم",
        "buttons_contact_me": "تواصل معي",
        "buttons_download_cv": "تحميل السيرة",
        "buttons_send_message": "إرسال رسالة",
        "buttons_get_quote": "اقتباس جديد",
        "buttons_try_tool": "تجربة الأداة",
        "buttons_view_all": "عرض الكل",
        
        "contact_phone": "الهاتف",
        "contact_email": "البريد الإلكتروني",
        "contact_whatsapp": "واتساب",
        "contact_telegram": "تيليجرام",
        "contact_copy": "انقر للنسخ",
        "contact_name": "الاسم",
        "contact_subject": "الموضوع",
        "contact_message": "الرسالة",
        
        "footer_quick_links": "روابط سريعة",
        "footer_stay_connected": "ابق على تواصل",
        "footer_rights": "جميع الحقوق محفوظة",
        "footer_made_with": "مصنوع بـ",
        "footer_passion": "التميز في كل بكسل"
    }
}

# ============================================================
# 🔄 دوال المساعدة
# ============================================================
def get_locale():
    """الحصول على اللغة الحالية"""
    return session.get('language', 'en')

def get_text_direction(lang):
    """الحصول على اتجاه النص"""
    return 'rtl' if lang == 'ar' else 'ltr'

def get_text(item, key, lang=None):
    """الحصول على النص باللغة المطلوبة"""
    if not lang:
        lang = get_locale()
    
    key_with_lang = f"{key}_{lang}"
    if key_with_lang in item:
        return item[key_with_lang]
    
    key_en = f"{key}_en"
    if key_en in item:
        return item[key_en]
    
    return item.get(key, "")

# ============================================================
# ⚡ إعدادات Flask
# ============================================================
@app.before_request
def before_request():
    """إعدادات قبل كل طلب"""
    g.current_lang = get_locale()
    g.text_direction = get_text_direction(g.current_lang)
    g.user_info = USER_INFO
    g.languages = LANGUAGES
    g.current_year = datetime.now().year
    g.color_palette = COLOR_PALETTE
    g.about_me = ABOUT_ME
    g.projects = PROJECTS
    g.designs = DESIGNS
    g.animations = ANIMATIONS
    g.skills = SKILLS
    g.certifications = CERTIFICATIONS
    g.achievements = ACHIEVEMENTS
    g.quotes = QUOTES
    g.tools = TOOLS
    
    # تأكد من وجود جميع الترجمات
    g.trans = TRANSLATIONS.get(g.current_lang, TRANSLATIONS['en'])
    
    # دالة مساعدة للترجمة
    def get_trans(key):
        return g.trans.get(key, TRANSLATIONS['en'].get(key, key))
    
    g.get_trans = get_trans
    g.get_text = get_text
    
    # تعريف مفاتيح التنقل بشكل منفصل
    g.nav_keys = ['home', 'about', 'projects', 'designs', 'animations', 'skills', 'certificates', 'achievements', 'tools', 'contact']

# ============================================================
# 🌟 القالب الرئيسي - HTML
# ============================================================
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="{{ g.current_lang }}" dir="{{ g.text_direction }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ g.user_info.name }} | {{ g.user_info.title }}</title>
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        /* ======================================================
           👑 CSS Variables - الألوان الملكية
           ====================================================== */
        :root {
            --primary: {{ g.color_palette.primary }};
            --secondary: {{ g.color_palette.secondary }};
            --gold: {{ g.color_palette.accent_gold }};
            --gold-light: {{ g.color_palette.accent_gold_light }};
            --silver: {{ g.color_palette.accent_silver }};
            --silver-dark: {{ g.color_palette.accent_silver_dark }};
            --platinum: {{ g.color_palette.accent_platinum }};
            --diamond: {{ g.color_palette.accent_diamond }};
            
            /* تأثيرات متطورة */
            --glow-gold: 0 0 40px rgba(212, 175, 55, 0.6);
            --glow-silver: 0 0 40px rgba(192, 192, 192, 0.5);
            --shadow-elite: 0 30px 60px rgba(0, 0, 0, 0.4);
            --gradient-gold: {{ g.color_palette.gradient_gold }};
            --gradient-silver: {{ g.color_palette.gradient_silver }};
            --gradient-black: {{ g.color_palette.gradient_black }};
            --gradient-premium: {{ g.color_palette.gradient_premium }};
            
            /* أنماط الخطوط النخبوية */
            --font-heading: 'Cinzel', serif;
            --font-subheading: 'Playfair Display', serif;
            --font-body: 'Inter', sans-serif;
        }
        
        /* ======================================================
           🎯 Reset & Base Styles
           ====================================================== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: var(--font-body);
            background: var(--gradient-black);
            color: var(--platinum);
            line-height: 1.8;
            overflow-x: hidden;
            min-height: 100vh;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 10% 20%, rgba(212, 175, 55, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 90% 10%, rgba(192, 192, 192, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 50% 80%, rgba(185, 242, 255, 0.05) 0%, transparent 50%);
            z-index: -1;
            animation: eliteFloat 30s infinite ease-in-out alternate;
        }
        
        @keyframes eliteFloat {
            0% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(30px, 40px) scale(1.02); }
            50% { transform: translate(-20px, 60px) scale(1.04); }
            75% { transform: translate(40px, -20px) scale(1.02); }
            100% { transform: translate(-10px, -40px) scale(1); }
        }
        
        .container {
            width: 90%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
            position: relative;
            z-index: 1;
        }
        
        /* ======================================================
           🌍 Language Selector - شريط اللغات النخبوي
           ====================================================== */
        .language-selector {
            position: fixed;
            top: 30px;
            right: 30px;
            z-index: 1000;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(20px);
            border-radius: 50px;
            padding: 15px 20px;
            display: flex;
            gap: 15px;
            box-shadow: var(--glow-gold);
            border: 2px solid var(--gold);
            animation: slideInRight 0.8s ease-out;
        }
        
        .lang-btn {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 2px solid transparent;
            background: rgba(255, 255, 255, 0.05);
            color: var(--gold);
            font-size: 1.5rem;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .lang-btn:hover {
            transform: scale(1.3) translateY(-5px);
            background: var(--gradient-gold);
            color: black;
            box-shadow: var(--glow-gold);
            border-color: var(--gold-light);
        }
        
        .lang-btn.active {
            background: var(--gradient-gold);
            color: black;
            transform: scale(1.2);
            box-shadow: var(--glow-gold);
            border-color: var(--gold-light);
        }
        
        /* ======================================================
           🚀 Navigation - التنقل الملكي
           ====================================================== */
        .navbar {
            position: fixed;
            top: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(25px);
            border-radius: 60px;
            padding: 20px 45px;
            z-index: 999;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border: 2px solid var(--gold);
            animation: slideInDown 0.8s ease-out;
        }
        
        .nav-container {
            display: flex;
            gap: 35px;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .nav-link {
            color: var(--silver);
            text-decoration: none;
            font-weight: 600;
            padding: 15px 30px;
            border-radius: 40px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            font-size: 1.1rem;
            letter-spacing: 1px;
            font-family: var(--font-subheading);
        }
        
        .nav-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: var(--gradient-gold);
            transition: left 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: -1;
            border-radius: 40px;
        }
        
        .nav-link:hover::before {
            left: 0;
        }
        
        .nav-link:hover {
            color: black;
            transform: translateY(-8px);
            box-shadow: var(--glow-gold);
            letter-spacing: 2px;
        }
        
        /* ======================================================
           👑 Hero Section - القسم الملكي
           ====================================================== */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
            padding: 150px 0;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif') center/cover no-repeat;
            opacity: 0.1;
            z-index: -1;
        }
        
        .hero-content {
            max-width: 1100px;
            animation: heroAppear 1.5s ease-out;
        }
        
        @keyframes heroAppear {
            from {
                opacity: 0;
                transform: translateY(100px) scale(0.9);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
        
        .profile-container {
            position: relative;
            display: inline-block;
            margin-bottom: 60px;
        }
        
        .profile-image {
            width: 280px;
            height: 280px;
            border-radius: 50%;
            border: 8px solid var(--gold);
            padding: 10px;
            background: var(--gradient-gold);
            box-shadow: var(--glow-gold), 0 0 100px rgba(212, 175, 55, 0.4);
            animation: goldPulse 4s infinite ease-in-out;
            position: relative;
            overflow: hidden;
            margin: 0 auto 40px;
        }
        
        .profile-image img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            filter: sepia(0.2) contrast(1.1);
            transition: all 0.5s ease;
        }
        
        .profile-image:hover img {
            transform: scale(1.05);
            filter: sepia(0) contrast(1.2);
        }
        
        .crown-icon {
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 120px;
            background: var(--gradient-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
            border: 6px solid var(--primary);
            box-shadow: var(--glow-gold);
            animation: crownFloat 6s infinite ease-in-out;
        }
        
        @keyframes crownFloat {
            0%, 100% { transform: translateX(-50%) translateY(0) rotate(0deg); }
            25% { transform: translateX(-50%) translateY(-20px) rotate(5deg); }
            50% { transform: translateX(-50%) translateY(-10px) rotate(-5deg); }
            75% { transform: translateX(-50%) translateY(-15px) rotate(3deg); }
        }
        
        .crown-icon i {
            font-size: 3.5rem;
            color: black;
            text-shadow: 0 2px 10px rgba(255, 255, 255, 0.5);
        }
        
        .hero h1 {
            font-family: var(--font-heading);
            font-size: 6.5rem;
            font-weight: 900;
            background: var(--gradient-gold);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 8px;
            position: relative;
            display: inline-block;
            text-shadow: 0 0 60px rgba(212, 175, 55, 0.4);
            animation: textGlow 3s infinite alternate;
        }
        
        @keyframes textGlow {
            from { text-shadow: 0 0 60px rgba(212, 175, 55, 0.4); }
            to { text-shadow: 0 0 100px rgba(212, 175, 55, 0.8), 0 0 40px rgba(255, 215, 0, 0.6); }
        }
        
        @keyframes goldPulse {
            0%, 100% { box-shadow: var(--glow-gold), 0 0 100px rgba(212, 175, 55, 0.4); }
            50% { box-shadow: 0 0 80px rgba(212, 175, 55, 0.7), 0 0 150px rgba(255, 215, 0, 0.5); }
        }
        
        .hero-subtitle {
            font-family: var(--font-subheading);
            font-size: 2.8rem;
            color: var(--silver);
            margin-bottom: 40px;
            font-weight: 700;
            letter-spacing: 4px;
            text-shadow: 0 5px 25px rgba(255, 255, 255, 0.1);
            position: relative;
            padding-bottom: 25px;
        }
        
        .hero-subtitle::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 4px;
            background: var(--gradient-gold);
            border-radius: 2px;
            animation: linePulse 2s infinite alternate;
        }
        
        @keyframes linePulse {
            from { width: 200px; opacity: 0.7; }
            to { width: 300px; opacity: 1; }
        }
        
        .hero-description {
            font-size: 1.6rem;
            color: var(--platinum);
            max-width: 900px;
            margin: 0 auto 60px;
            line-height: 1.6;
            padding: 30px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212, 175, 55, 0.3);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .hero-description::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, 
                transparent 30%, 
                rgba(212, 175, 55, 0.1) 50%, 
                transparent 70%);
            animation: shimmer 6s infinite linear;
            z-index: -1;
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .hero-buttons {
            display: flex;
            gap: 30px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 50px;
        }
        
        /* ======================================================
           🎨 Buttons - الأزرار الفاخرة
           ====================================================== */
        .btn {
            padding: 22px 50px;
            border-radius: 60px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.3rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            border: none;
            cursor: pointer;
            font-family: var(--font-heading);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            min-width: 250px;
        }
        
        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(255, 255, 255, 0.2), 
                transparent);
            transition: left 0.7s ease;
            z-index: 1;
        }
        
        .btn:hover::before {
            left: 100%;
        }
        
        .btn-gold {
            background: var(--gradient-gold);
            color: black;
            box-shadow: 0 15px 40px rgba(212, 175, 55, 0.4);
        }
        
        .btn-gold:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 25px 60px rgba(212, 175, 55, 0.6), 
                        0 0 50px rgba(212, 175, 55, 0.3);
            letter-spacing: 4px;
        }
        
        .btn-silver {
            background: var(--gradient-silver);
            color: black;
            box-shadow: 0 15px 40px rgba(192, 192, 192, 0.3);
            border: 2px solid var(--silver);
        }
        
        .btn-silver:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 25px 60px rgba(192, 192, 192, 0.5), 
                        0 0 50px rgba(192, 192, 192, 0.2);
            letter-spacing: 4px;
        }
        
        .btn-black {
            background: linear-gradient(135deg, #000000, #2C2C2C, #000000);
            color: var(--gold);
            border: 2px solid var(--gold);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
        }
        
        .btn-black:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 
                        0 0 50px rgba(212, 175, 55, 0.2);
            letter-spacing: 4px;
            color: var(--gold-light);
            background: linear-gradient(135deg, #121212, #000000, #121212);
        }
        
        .btn i {
            font-size: 1.5rem;
            transition: transform 0.3s ease;
        }
        
        .btn:hover i {
            transform: scale(1.3) rotate(15deg);
        }
        
        /* ======================================================
           📱 Sections - الأقسام النخبوية
           ====================================================== */
        .section {
            padding: 150px 0;
            position: relative;
            overflow: hidden;
        }
        
        .section-title {
            font-family: var(--font-heading);
            font-size: 4.5rem;
            text-align: center;
            margin-bottom: 100px;
            position: relative;
            display: inline-block;
            left: 50%;
            transform: translateX(-50%);
            padding: 0 60px;
        }
        
        .section-title::before,
        .section-title::after {
            content: '';
            position: absolute;
            top: 50%;
            width: 200px;
            height: 4px;
            background: var(--gradient-gold);
            border-radius: 2px;
        }
        
        .section-title::before {
            right: 100%;
            transform: translateY(-50%);
            animation: titleLineLeft 3s infinite alternate;
        }
        
        .section-title::after {
            left: 100%;
            transform: translateY(-50%);
            animation: titleLineRight 3s infinite alternate;
        }
        
        @keyframes titleLineLeft {
            from { width: 200px; opacity: 0.7; }
            to { width: 300px; opacity: 1; }
        }
        
        @keyframes titleLineRight {
            from { width: 200px; opacity: 0.7; }
            to { width: 300px; opacity: 1; }
        }
        
        .section-title-gold {
            background: var(--gradient-gold);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 10px 40px rgba(212, 175, 55, 0.3);
        }
        
        .section-title-silver {
            background: var(--gradient-silver);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 10px 40px rgba(192, 192, 192, 0.3);
        }
        
        /* ======================================================
           🎯 About Me Section - قسم "عني" المتطور
           ====================================================== */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: center;
        }
        
        .about-text {
            background: rgba(0, 0, 0, 0.5);
            padding: 60px;
            border-radius: 40px;
            border: 2px solid rgba(212, 175, 55, 0.2);
            box-shadow: var(--shadow-elite);
            backdrop-filter: blur(15px);
            position: relative;
            overflow: hidden;
        }
        
        .about-text::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: var(--gradient-premium);
            border-radius: 42px;
            z-index: -1;
            animation: borderRotate 10s linear infinite;
        }
        
        @keyframes borderRotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .about-paragraph {
            font-size: 1.4rem;
            line-height: 1.8;
            margin-bottom: 40px;
            position: relative;
            padding-left: 30px;
        }
        
        .about-paragraph::before {
            content: '✦';
            position: absolute;
            left: 0;
            top: 0;
            color: var(--gold);
            font-size: 1.8rem;
            text-shadow: 0 0 20px var(--gold);
        }
        
        /* صورة تشي جيفارا الكاريزمية */
        .charismatic-image {
            position: relative;
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.6);
            transform: perspective(1000px) rotateY(-10deg);
            transition: all 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            filter: grayscale(0.3) contrast(1.1);
            height: 600px;
        }
        
        .charismatic-image:hover {
            transform: perspective(1000px) rotateY(0deg) translateY(-30px);
            box-shadow: 0 60px 120px rgba(0, 0, 0, 0.8), 
                        0 0 80px rgba(212, 175, 55, 0.3);
            filter: grayscale(0) contrast(1.2);
        }
        
        .charismatic-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: all 0.7s ease;
        }
        
        .charismatic-image::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 40%;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.9), transparent);
            z-index: 1;
        }
        
        .charismatic-quote {
            position: absolute;
            bottom: 40px;
            left: 40px;
            right: 40px;
            color: white;
            font-family: var(--font-subheading);
            font-size: 1.8rem;
            font-style: italic;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
            z-index: 2;
            padding: 25px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 20px;
            border-left: 5px solid var(--gold);
            line-height: 1.5;
        }
        
        /* ======================================================
           🏆 Projects Section - قسم المشاريع المتألق
           ====================================================== */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 50px;
            margin-top: 80px;
        }
        
        .project-card {
            background: rgba(0, 0, 0, 0.6);
            border-radius: 30px;
            overflow: hidden;
            border: 2px solid transparent;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
            transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            backdrop-filter: blur(10px);
        }
        
        .project-card:hover {
            transform: translateY(-30px) scale(1.02);
            box-shadow: 0 50px 100px rgba(0, 0, 0, 0.6), 
                        0 0 60px rgba(212, 175, 55, 0.2);
            border-color: var(--gold);
        }
        
        .project-header {
            padding: 40px;
            background: linear-gradient(135deg, 
                rgba(0, 0, 0, 0.9), 
                rgba(26, 26, 26, 0.9));
            border-bottom: 2px solid rgba(212, 175, 55, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .project-icon {
            font-size: 4rem;
            margin-bottom: 25px;
            display: block;
            text-align: center;
            text-shadow: 0 0 30px currentColor;
            animation: iconFloat 4s infinite ease-in-out;
        }
        
        @keyframes iconFloat {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            33% { transform: translateY(-10px) rotate(5deg); }
            66% { transform: translateY(-5px) rotate(-5deg); }
        }
        
        .project-title {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            margin-bottom: 20px;
            background: linear-gradient(45deg, var(--gold-light), var(--silver));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-align: center;
        }
        
        .project-description {
            font-size: 1.3rem;
            line-height: 1.6;
            color: var(--platinum);
            text-align: center;
            padding: 0 20px;
        }
        
        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: center;
            padding: 30px;
            background: rgba(0, 0, 0, 0.5);
        }
        
        .tech-tag {
            padding: 12px 25px;
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--gold-light);
            transition: all 0.3s ease;
        }
        
        .tech-tag:hover {
            background: rgba(212, 175, 55, 0.2);
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }
        
        /* ======================================================
           💎 Skills Section - قسم المهارات الماسي
           ====================================================== */
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 40px;
            margin-top: 80px;
        }
        
        .skill-category {
            background: rgba(0, 0, 0, 0.5);
            padding: 50px;
            border-radius: 30px;
            border: 2px solid rgba(212, 175, 55, 0.2);
            backdrop-filter: blur(15px);
            transition: all 0.5s ease;
        }
        
        .skill-category:hover {
            border-color: var(--gold);
            transform: translateY(-20px);
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.5), 
                        0 0 40px rgba(212, 175, 55, 0.1);
        }
        
        .category-title {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            color: var(--gold);
            margin-bottom: 40px;
            text-align: center;
            position: relative;
            padding-bottom: 20px;
        }
        
        .category-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: var(--gradient-gold);
            border-radius: 2px;
        }
        
        .skill-item {
            margin-bottom: 35px;
        }
        
        .skill-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .skill-name {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--silver);
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .skill-name i {
            font-size: 1.8rem;
            color: var(--gold);
        }
        
        .skill-percentage {
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--gold);
            font-family: var(--font-heading);
        }
        
        .skill-bar {
            height: 12px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }
        
        .skill-progress {
            height: 100%;
            border-radius: 6px;
            background: var(--gradient-gold);
            width: 0;
            position: relative;
            transition: width 2s ease-out;
            animation: progressLoad 2s ease-out forwards;
        }
        
        @keyframes progressLoad {
            from { width: 0; }
        }
        
        .skill-progress::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(255, 255, 255, 0.2), 
                transparent);
            animation: progressShimmer 2s infinite linear;
        }
        
        @keyframes progressShimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        /* ======================================================
           🎭 Interactive Tools - الأدوات التفاعلية
           ====================================================== */
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-top: 80px;
        }
        
        .tool-card {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 30px;
            padding: 50px;
            text-align: center;
            border: 2px solid transparent;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .tool-card:hover {
            border-color: var(--gold);
            transform: translateY(-25px) scale(1.05);
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.5), 
                        0 0 50px rgba(212, 175, 55, 0.2);
        }
        
        .tool-icon {
            font-size: 4.5rem;
            margin-bottom: 30px;
            display: block;
            color: var(--gold);
            text-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
            animation: toolIconFloat 3s infinite ease-in-out;
        }
        
        @keyframes toolIconFloat {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-20px) scale(1.1); }
        }
        
        .tool-name {
            font-family: var(--font-heading);
            font-size: 2rem;
            color: var(--gold);
            margin-bottom: 25px;
        }
        
        .tool-description {
            font-size: 1.3rem;
            line-height: 1.6;
            color: var(--silver);
            margin-bottom: 35px;
        }
        
        /* ======================================================
           💬 Quotes Section - قسم الاقتباسات الملهمة
           ====================================================== */
        .quotes-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 50px;
            margin-top: 80px;
        }
        
        .quote-card {
            background: rgba(0, 0, 0, 0.6);
            border-radius: 30px;
            padding: 60px 50px;
            position: relative;
            border: 2px solid rgba(212, 175, 55, 0.3);
            transition: all 0.5s ease;
            backdrop-filter: blur(15px);
        }
        
        .quote-card:hover {
            border-color: var(--gold);
            transform: translateY(-20px);
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.5), 
                        0 0 60px rgba(212, 175, 55, 0.2);
        }
        
        .quote-text {
            font-family: var(--font-subheading);
            font-size: 2rem;
            line-height: 1.6;
            font-style: italic;
            margin-bottom: 40px;
            color: var(--platinum);
            text-align: center;
            position: relative;
            padding: 0 20px;
        }
        
        .quote-text::before,
        .quote-text::after {
            content: '"';
            font-size: 5rem;
            color: var(--gold);
            position: absolute;
            opacity: 0.5;
        }
        
        .quote-text::before {
            top: -30px;
            left: 0;
        }
        
        .quote-text::after {
            bottom: -60px;
            right: 0;
        }
        
        .quote-author {
            text-align: center;
            font-family: var(--font-heading);
            font-size: 1.8rem;
            color: var(--gold);
            font-weight: 700;
            padding-top: 30px;
            border-top: 2px solid rgba(212, 175, 55, 0.3);
        }
        
        /* ======================================================
           📞 Contact Section - قسم التواصل الفاخر
           ====================================================== */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: start;
            margin-top: 80px;
        }
        
        .contact-info {
            background: rgba(0, 0, 0, 0.5);
            padding: 60px;
            border-radius: 40px;
            border: 2px solid rgba(212, 175, 55, 0.3);
            backdrop-filter: blur(15px);
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            gap: 25px;
            margin-bottom: 40px;
            padding: 25px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 25px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .contact-item:hover {
            background: rgba(212, 175, 55, 0.1);
            transform: translateX(20px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .contact-icon {
            width: 70px;
            height: 70px;
            background: var(--gradient-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: black;
            flex-shrink: 0;
        }
        
        .contact-details h3 {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            color: var(--gold);
            margin-bottom: 10px;
        }
        
        .contact-details p {
            font-size: 1.3rem;
            color: var(--silver);
        }
        
        .copy-notification {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            background: var(--gradient-gold);
            color: black;
            padding: 25px 50px;
            border-radius: 30px;
            font-family: var(--font-heading);
            font-size: 1.5rem;
            z-index: 10000;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease;
        }
        
        .copy-notification.show {
            transform: translate(-50%, -50%) scale(1);
            animation: copyPulse 1.5s ease-out;
        }
        
        @keyframes copyPulse {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
            50% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        }
        
        /* ======================================================
           🏁 Footer - التذييل الملكي
           ====================================================== */
        .footer {
            background: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.9));
            padding: 100px 0 50px;
            margin-top: 150px;
            border-top: 2px solid rgba(212, 175, 55, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 80px;
            margin-bottom: 70px;
        }
        
        .footer-section h3 {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            color: var(--gold);
            margin-bottom: 40px;
            position: relative;
            padding-bottom: 20px;
        }
        
        .footer-section h3::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100px;
            height: 3px;
            background: var(--gradient-gold);
            border-radius: 2px;
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 25px;
        }
        
        .footer-links a {
            color: var(--silver);
            text-decoration: none;
            font-size: 1.3rem;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .footer-links a:hover {
            color: var(--gold);
            transform: translateX(15px);
            text-shadow: 0 0 20px var(--gold);
        }
        
        .footer-links a i {
            color: var(--gold);
            font-size: 1.5rem;
        }
        
        .copyright {
            text-align: center;
            padding-top: 50px;
            border-top: 1px solid rgba(212, 175, 55, 0.2);
            font-size: 1.4rem;
            color: var(--silver);
        }
        
        .made-with-love {
            color: var(--gold);
            font-weight: 700;
            text-shadow: 0 0 20px rgba(212, 175, 55, 0.5);
            animation: lovePulse 2s infinite alternate;
        }
        
        @keyframes lovePulse {
            from { opacity: 0.7; }
            to { opacity: 1; }
        }
        
        /* ======================================================
           🔥 Custom Scrollbar - شريط التمرير الفاخر
           ====================================================== */
        ::-webkit-scrollbar {
            width: 15px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--gradient-gold);
            border-radius: 10px;
            border: 3px solid rgba(0, 0, 0, 0.8);
            transition: all 0.3s ease;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: var(--gradient-silver);
            box-shadow: 0 0 20px var(--gold);
        }
        
        /* ======================================================
           📱 Responsive Design - تصميم متجاوب
           ====================================================== */
        @media (max-width: 1200px) {
            .hero h1 { font-size: 5rem; }
            .section-title { font-size: 3.8rem; }
            .projects-grid { grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); }
        }
        
        @media (max-width: 992px) {
            .hero h1 { font-size: 4rem; }
            .hero-subtitle { font-size: 2.2rem; }
            .about-content { grid-template-columns: 1fr; }
            .contact-container { grid-template-columns: 1fr; }
            .footer-content { grid-template-columns: repeat(2, 1fr); }
            .navbar { padding: 15px 25px; }
            .nav-container { gap: 15px; }
            .nav-link { padding: 12px 20px; font-size: 1rem; }
        }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 3.2rem; letter-spacing: 4px; }
            .hero-subtitle { font-size: 1.8rem; }
            .profile-image { width: 220px; height: 220px; }
            .section { padding: 100px 0; }
            .section-title { font-size: 3rem; }
            .projects-grid { grid-template-columns: 1fr; }
            .tools-grid { grid-template-columns: 1fr; }
            .quotes-container { grid-template-columns: 1fr; }
            .skills-container { grid-template-columns: 1fr; }
            .btn { padding: 18px 30px; min-width: 200px; }
            .language-selector { top: 20px; right: 20px; }
            .navbar { top: 90px; width: 90%; }
            .footer-content { grid-template-columns: 1fr; gap: 50px; }
        }
        
        @media (max-width: 480px) {
            .hero h1 { font-size: 2.5rem; }
            .hero-subtitle { font-size: 1.5rem; }
            .section-title { font-size: 2.5rem; }
            .about-text { padding: 30px; }
            .contact-info { padding: 30px; }
            .tool-card { padding: 30px; }
            .project-card { padding: 20px; }
            .btn { padding: 15px 25px; min-width: 180px; font-size: 1.1rem; }
            .profile-image { width: 180px; height: 180px; }
        }
    </style>
</head>
<body>
    <!-- 🌍 Language Selector -->
    <div class="language-selector">
        {% for lang in g.languages %}
            <button class="lang-btn {% if lang.code == g.current_lang %}active{% endif %}"
                    onclick="changeLanguage('{{ lang.code }}')">
                {{ lang.flag }}
            </button>
        {% endfor %}
    </div>
    
    <!-- 🚀 Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            {% for nav_key in g.nav_keys %}
                <a href="#{{ nav_key }}" class="nav-link">
                    {{ g.get_trans('nav_' + nav_key) }}
                </a>
            {% endfor %}
        </div>
    </nav>
    
    <!-- 👑 Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <div class="profile-container">
                <div class="crown-icon">
                    <i class="fas fa-crown"></i>
                </div>
                <div class="profile-image">
                    <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" alt="Profile">
                </div>
            </div>
            
            <h1>{{ g.user_info.name if g.current_lang == 'en' else g.user_info.arabic_name }}</h1>
            <h2 class="hero-subtitle">{{ g.user_info.quote }}</h2>
            
            <p class="hero-description">
                {{ g.get_trans('hero_description') }}
            </p>
            
            <div class="hero-buttons">
                <a href="#contact" class="btn btn-gold">
                    <i class="fas fa-gem"></i>
                    {{ g.get_trans('buttons_contact_me') }}
                </a>
                <a href="#projects" class="btn btn-silver">
                    <i class="fas fa-bolt"></i>
                    {{ g.get_trans('buttons_view_all') }}
                </a>
                <button class="btn btn-black" onclick="downloadCV()">
                    <i class="fas fa-download"></i>
                    {{ g.get_trans('buttons_download_cv') }}
                </button>
            </div>
        </div>
    </section>
    
    <!-- 🎭 About Me Section -->
    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title section-title-gold">{{ g.get_trans('sections_about_me') }}</h2>
            
            <div class="about-content">
                <div class="about-text">
                    <p class="about-paragraph">{{ g.about_me.intro_en if g.current_lang == 'en' else g.about_me.intro_ar }}</p>
                    <p class="about-paragraph">{{ g.about_me.passion_en if g.current_lang == 'en' else g.about_me.passion_ar }}</p>
                    <p class="about-paragraph">{{ g.about_me.skills_en if g.current_lang == 'en' else g.about_me.skills_ar }}</p>
                    <p class="about-paragraph">{{ g.about_me.vision_en if g.current_lang == 'en' else g.about_me.vision_ar }}</p>
                </div>
                
                <div class="charismatic-image">
                    <img src="https://media.giphy.com/media/3o7TKsQ8gTp3WqXqQw/giphy.gif" alt="Che Guevara - Charismatic Leader">
                    <div class="charismatic-quote">
                        {{ g.get_text(g.quotes[3], 'text', g.current_lang) }}
                        <br>- {{ g.quotes[3].author }}
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- 🏆 Projects Section -->
    <section id="projects" class="section" style="background: rgba(0, 0, 0, 0.3);">
        <div class="container">
            <h2 class="section-title section-title-silver">{{ g.get_trans('sections_featured_projects') }}</h2>
            
            <div class="projects-grid">
                {% for project in g.projects %}
                <div class="project-card" style="border-color: {{ project.color }};">
                    <div class="project-header">
                        <span class="project-icon">{{ project.icon }}</span>
                        <h3 class="project-title">{{ g.get_text(project, 'title', g.current_lang) }}</h3>
                        <p class="project-description">
                            {{ g.get_text(project, 'description', g.current_lang) }}
                        </p>
                    </div>
                    
                    <div class="project-tech">
                        {% for tech in project.technologies %}
                        <span class="tech-tag">{{ tech }}</span>
                        {% endfor %}
                    </div>
                    
                    <div style="padding: 40px; text-align: center;">
                        <a href="#" class="btn btn-gold" style="padding: 15px 40px; font-size: 1.1rem;">
                            <i class="fas fa-eye"></i>
                            {{ g.get_trans('buttons_view_project') }}
                        </a>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>
    
    <!-- 💎 Skills Section -->
    <section id="skills" class="section">
        <div class="container">
            <h2 class="section-title section-title-gold">{{ g.get_trans('sections_technical_skills') }}</h2>
            
            <div class="skills-container">
                {% for category, skills in g.skills.items() %}
                <div class="skill-category">
                    <h3 class="category-title">
                        {% if category == 'creative_excellence' %}
                            {{ 'Creative Excellence' if g.current_lang == 'en' else 'التميز الإبداعي' }}
                        {% elif category == 'technical_mastery' %}
                            {{ 'Technical Mastery' if g.current_lang == 'en' else 'الإتقان التقني' }}
                        {% else %}
                            {{ 'Strategic Vision' if g.current_lang == 'en' else 'الرؤية الاستراتيجية' }}
                        {% endif %}
                    </h3>
                    
                    {% for skill in skills %}
                    <div class="skill-item">
                        <div class="skill-header">
                            <div class="skill-name">
                                <i class="fas fa-star"></i>
                                {{ skill.name }}
                            </div>
                            <div class="skill-percentage">{{ skill.level }}%</div>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-progress" style="width: {{ skill.level }}%;"></div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
                {% endfor %}
            </div>
        </div>
    </section>
    
    <!-- 🎭 Interactive Tools -->
    <section id="tools" class="section" style="background: rgba(0, 0, 0, 0.3);">
        <div class="container">
            <h2 class="section-title section-title-silver">{{ g.get_trans('sections_interactive_tools') }}</h2>
            
            <div class="tools-grid">
                {% for tool in g.tools %}
                <div class="tool-card">
                    <span class="tool-icon">{{ tool.icon }}</span>
                    <h3 class="tool-name">{{ tool.name }}</h3>
                    <p class="tool-description">
                        {{ g.get_text(tool, 'description', g.current_lang) }}
                    </p>
                    <button class="btn btn-gold" onclick="tryTool('{{ tool.name }}')" style="padding: 15px 40px;">
                        <i class="fas fa-play"></i>
                        {{ g.get_trans('buttons_try_tool') }}
                    </button>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>
    
    <!-- 💬 Quotes Section -->
    <section id="achievements" class="section">
        <div class="container">
            <h2 class="section-title section-title-gold">{{ g.get_trans('sections_inspirational_quotes') }}</h2>
            
            <div class="quotes-container">
                {% for quote in g.quotes %}
                <div class="quote-card" style="border-color: {{ quote.color }};">
                    <p class="quote-text">{{ g.get_text(quote, 'text', g.current_lang) }}</p>
                    <div class="quote-author">- {{ quote.author }}</div>
                </div>
                {% endfor %}
            </div>
            
            <div style="text-align: center; margin-top: 80px;">
                <button class="btn btn-silver" onclick="getNewQuote()">
                    <i class="fas fa-sync-alt"></i>
                    {{ g.get_trans('buttons_get_quote') }}
                </button>
            </div>
        </div>
    </section>
    
    <!-- 📞 Contact Section -->
    <section id="contact" class="section" style="background: rgba(0, 0, 0, 0.3);">
        <div class="container">
            <h2 class="section-title section-title-silver">{{ g.get_trans('sections_contact_me') }}</h2>
            
            <div class="contact-container">
                <div class="contact-info">
                    <div class="contact-item" onclick="copyToClipboard('{{ g.user_info.phone }}', 'Phone number')">
                        <div class="contact-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <div class="contact-details">
                            <h3>{{ g.get_trans('contact_phone') }}</h3>
                            <p>{{ g.user_info.phone }}</p>
                        </div>
                    </div>
                    
                    <div class="contact-item" onclick="copyToClipboard('{{ g.user_info.email }}', 'Email address')">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div class="contact-details">
                            <h3>{{ g.get_trans('contact_email') }}</h3>
                            <p>{{ g.user_info.email }}</p>
                        </div>
                    </div>
                    
                    <div class="contact-item" onclick="copyToClipboard('{{ g.user_info.whatsapp }}', 'WhatsApp')">
                        <div class="contact-icon">
                            <i class="fab fa-whatsapp"></i>
                        </div>
                        <div class="contact-details">
                            <h3>{{ g.get_trans('contact_whatsapp') }}</h3>
                            <p>{{ g.user_info.whatsapp }}</p>
                        </div>
                    </div>
                    
                    <div class="contact-item" onclick="copyToClipboard('{{ g.user_info.telegram }}', 'Telegram')">
                        <div class="contact-icon">
                            <i class="fab fa-telegram"></i>
                        </div>
                        <div class="contact-details">
                            <h3>{{ g.get_trans('contact_telegram') }}</h3>
                            <p>{{ g.user_info.telegram }}</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-info">
                    <h3 style="color: var(--gold); margin-bottom: 40px; font-family: var(--font-heading); font-size: 2rem;">
                        {{ 'Send me a message' if g.current_lang == 'en' else 'ارسل لي رسالة' }}
                    </h3>
                    
                    <form id="contactForm" style="display: flex; flex-direction: column; gap: 30px;">
                        <div>
                            <label style="display: block; margin-bottom: 15px; font-size: 1.3rem; color: var(--silver);">
                                {{ g.get_trans('contact_name') }}
                            </label>
                            <input type="text" required 
                                   style="width: 100%; padding: 20px; background: rgba(255,255,255,0.05); border: 2px solid rgba(212,175,55,0.3); border-radius: 15px; color: white; font-size: 1.3rem;">
                        </div>
                        
                        <div>
                            <label style="display: block; margin-bottom: 15px; font-size: 1.3rem; color: var(--silver);">
                                {{ g.get_trans('contact_subject') }}
                            </label>
                            <input type="text" required 
                                   style="width: 100%; padding: 20px; background: rgba(255,255,255,0.05); border: 2px solid rgba(212,175,55,0.3); border-radius: 15px; color: white; font-size: 1.3rem;">
                        </div>
                        
                        <div>
                            <label style="display: block; margin-bottom: 15px; font-size: 1.3rem; color: var(--silver);">
                                {{ g.get_trans('contact_message') }}
                            </label>
                            <textarea required rows="6"
                                      style="width: 100%; padding: 20px; background: rgba(255,255,255,0.05); border: 2px solid rgba(212,175,55,0.3); border-radius: 15px; color: white; font-size: 1.3rem; resize: vertical;"></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-gold" style="align-self: flex-start;">
                            <i class="fas fa-paper-plane"></i>
                            {{ g.get_trans('buttons_send_message') }}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    
    <!-- 🏁 Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{{ g.get_trans('footer_quick_links') }}</h3>
                    <ul class="footer-links">
                        {% for nav_key in g.nav_keys[:5] %}
                        <li><a href="#{{ nav_key }}"><i class="fas fa-chevron-right"></i> {{ g.get_trans('nav_' + nav_key) }}</a></li>
                        {% endfor %}
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>{{ g.get_trans('footer_stay_connected') }}</h3>
                    <ul class="footer-links">
                        <li><a href="mailto:{{ g.user_info.email }}"><i class="fas fa-envelope"></i> {{ g.user_info.email }}</a></li>
                        <li><a href="tel:{{ g.user_info.phone }}"><i class="fas fa-phone"></i> {{ g.user_info.phone }}</a></li>
                        <li><a href="https://wa.me/{{ g.user_info.whatsapp }}" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a></li>
                        <li><a href="https://t.me/{{ g.user_info.telegram }}" target="_blank"><i class="fab fa-telegram"></i> Telegram</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>{{ g.user_info.website_name }}</h3>
                    <p style="font-size: 1.3rem; line-height: 1.8; color: var(--silver);">
                        {{ 'An elite portfolio masterpiece combining luxury, creativity, and technological excellence.' if g.current_lang == 'en' else 'تحفة بورتفوليو نخبوية تجمع بين الفخامة والإبداع والتميز التكنولوجي.' }}
                    </p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; {{ g.current_year }} {{ g.user_info.name if g.current_lang == 'en' else g.user_info.arabic_name }}. {{ g.get_trans('footer_rights') }}</p>
                <p style="margin-top: 20px;">
                    {{ g.get_trans('footer_made_with') }} 
                    <span class="made-with-love">♥</span> 
                    {{ g.get_trans('footer_passion') }}
                </p>
            </div>
        </div>
    </footer>
    
    <!-- 📋 Copy Notification -->
    <div id="copyNotification" class="copy-notification"></div>
    
    <script>
        // ======================================================
        // 🔧 JavaScript Functions - الدوال التفاعلية
        // ======================================================
        
        // 🌍 تغيير اللغة
        function changeLanguage(lang) {
            fetch('/change_language', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({language: lang})
            }).then(response => {
                if (response.ok) {
                    location.reload();
                }
            });
        }
        
        // 📋 نسخ النص للحافظة
        function copyToClipboard(text, label) {
            navigator.clipboard.writeText(text).then(() => {
                const notification = document.getElementById('copyNotification');
                notification.textContent = `${label} {{ 'copied!' if g.current_lang == 'en' else 'تم النسخ!' }} ✅`;
                notification.classList.add('show');
                
                setTimeout(() => {
                    notification.classList.remove('show');
                }, 2000);
            });
        }
        
        // 📄 تحميل السيرة الذاتية
        function downloadCV() {
            alert('{{ "Downloading Elite Portfolio CV..." if g.current_lang == "en" else "جارٍ تحميل السيرة الذاتية النخبوية..." }}');
            // يمكنك إضافة رابط التحميل الفعلي هنا
        }
        
        // 🎭 تجربة الأداة
        function tryTool(toolName) {
            const messages = {
                'Golden Color Harmony': '{{ "Opening Golden Color Palette Generator..." if g.current_lang == "en" else "جارٍ فتح مولد لوحة الألوان الذهبية..." }}',
                'Luxury Font Pairing': '{{ "Loading Luxury Font Combinations..." if g.current_lang == "en" else "جارٍ تحميل تركيبات الخطوط الفاخرة..." }}',
                'Elite Calculator': '{{ "Launching Premium Calculator..." if g.current_lang == "en" else "جارٍ تشغيل الآلة الحاسبة المتميزة..." }}',
                'Vision Board Creator': '{{ "Creating Digital Vision Board..." if g.current_lang == "en" else "جارٍ إنشاء لوحة الرؤية الرقمية..." }}',
                'Creative Timer': '{{ "Starting Pomodoro Timer..." if g.current_lang == "en" else "جارٍ بدء مؤقت بومودورو..." }}'
            };
            alert(messages[toolName] || '{{ "Opening tool..." if g.current_lang == "en" else "جارٍ فتح الأداة..." }}');
        }
        
        // 💬 اقتباس جديد
        function getNewQuote() {
            const quotes = {{ g.quotes|tojson }};
            const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
            
            const quoteCards = document.querySelectorAll('.quote-card');
            quoteCards.forEach(card => {
                card.style.opacity = '0.3';
                setTimeout(() => {
                    const quoteText = card.querySelector('.quote-text');
                    const quoteAuthor = card.querySelector('.quote-author');
                    
                    quoteText.textContent = randomQuote['text_{{ g.current_lang }}'] || randomQuote.text_en;
                    quoteAuthor.textContent = '- ' + randomQuote.author;
                    card.style.borderColor = randomQuote.color;
                    
                    card.style.opacity = '1';
                }, 500);
            });
        }
        
        // 📨 إرسال نموذج الاتصال
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('{{ "Thank you! Your elite message has been sent successfully." if g.current_lang == "en" else "شكراً لك! تم إرسال رسالتك النخبوية بنجاح." }}');
            this.reset();
        });
        
        // ✨ تأثيرات التمرير الناعمة
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // 💫 تأثيرات التحريك عند التمرير
        function animateOnScroll() {
            const elements = document.querySelectorAll('.project-card, .tool-card, .skill-category, .quote-card');
            
            elements.forEach(element => {
                const elementTop = element.getBoundingClientRect().top;
                const windowHeight = window.innerHeight;
                
                if (elementTop < windowHeight - 100) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                }
            });
        }
        
        // تعيين الخصائص الأولية للرسوم المتحركة
        document.querySelectorAll('.project-card, .tool-card, .skill-category, .quote-card').forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(50px)';
            element.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        });
        
        window.addEventListener('scroll', animateOnScroll);
        window.addEventListener('load', animateOnScroll);
        
        // 💎 تأثيرات بريق إضافية
        function addSparkleEffect() {
            const colors = ['#D4AF37', '#FFD700', '#C0C0C0', '#E5E4E2'];
            const sections = document.querySelectorAll('.section');
            
            sections.forEach(section => {
                for (let i = 0; i < 20; i++) {
                    const sparkle = document.createElement('div');
                    sparkle.style.cssText = `
                        position: absolute;
                        width: ${Math.random() * 6 + 2}px;
                        height: ${Math.random() * 6 + 2}px;
                        background: ${colors[Math.floor(Math.random() * colors.length)]};
                        border-radius: 50%;
                        pointer-events: none;
                        z-index: 1;
                        opacity: ${Math.random() * 0.5 + 0.3};
                        animation: sparkleFloat ${Math.random() * 5 + 3}s infinite ease-in-out;
                        left: ${Math.random() * 100}%;
                        top: ${Math.random() * 100}%;
                    `;
                    section.appendChild(sparkle);
                    
                    // إضافة حركة الطفو
                    const style = document.createElement('style');
                    style.textContent = `
                        @keyframes sparkleFloat {
                            0%, 100% { transform: translate(0, 0); opacity: 0.3; }
                            25% { transform: translate(${Math.random() * 30 - 15}px, ${Math.random() * 30 - 15}px); opacity: 0.8; }
                            50% { transform: translate(${Math.random() * 30 - 15}px, ${Math.random() * 30 - 15}px); opacity: 0.5; }
                            75% { transform: translate(${Math.random() * 30 - 15}px, ${Math.random() * 30 - 15}px); opacity: 0.7; }
                        }
                    `;
                    document.head.appendChild(style);
                }
            });
        }
        
        // 🎯 تهيئة الصفحة
        document.addEventListener('DOMContentLoaded', function() {
            // بدء تحميل أشرطة التقدم
            document.querySelectorAll('.skill-progress').forEach(progress => {
                const width = progress.style.width;
                progress.style.width = '0';
                setTimeout(() => {
                    progress.style.width = width;
                }, 500);
            });
            
            // إضافة تأثيرات البريق
            setTimeout(addSparkleEffect, 1000);
            
            // تأثيرات صوتية خفيفة (اختياري)
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            function playGoldSound() {
                try {
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    oscillator.frequency.value = 987.77; // نغمة ذهبية
                    oscillator.type = 'sine';
                    
                    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
                    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
                    
                    oscillator.start(audioContext.currentTime);
                    oscillator.stop(audioContext.currentTime + 0.5);
                } catch (e) {
                    console.log('Audio not supported');
                }
            }
            
            // إضافة أصوات عند النقر على الأزرار الذهبية
            document.querySelectorAll('.btn-gold').forEach(btn => {
                btn.addEventListener('click', playGoldSound);
            });
        });
    </script>
</body>
</html>
'''

# ============================================================
# 🚀 Routes - المسارات
# ============================================================

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/change_language', methods=['POST'])
def change_language():
    """تغيير اللغة"""
    data = request.get_json()
    session['language'] = data.get('language', 'en')
    return jsonify({'success': True})

@app.route('/get_random_quote')
def get_random_quote():
    """الحصول على اقتباس عشوائي"""
    import random
    quote = random.choice(QUOTES)
    return jsonify({
        'text_en': quote['text_en'],
        'text_ar': quote['text_ar'],
        'author': quote['author'],
        'color': quote['color']
    })

@app.route('/contact', methods=['POST'])
def contact():
    """إرسال رسالة التواصل"""
    try:
        data = request.get_json()
        # هنا يمكنك إضافة كود إرسال البريد الإلكتروني
        return jsonify({
            'success': True,
            'message': 'Message sent successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/download_cv')
def download_cv():
    """تحميل السيرة الذاتية"""
    # يمكنك إرجاع ملف PDF حقيقي هنا
    return jsonify({
        'success': True,
        'url': '#'
    })

# ============================================================
# 🎬 تشغيل التطبيق
# ============================================================

if __name__ == '__main__':
    print("✨" * 50)
    print("🚀 ELITE PORTFOLIO MASTERPIECE IS RUNNING!")
    print(f"🌍 Available at: http://localhost:5000")
    print(f"👑 Created for: {USER_INFO['name']}")
    print(f"🎨 Colors: Gold, Silver, Black Premium")
    print(f"💎 Features: Interactive Tools, Animations, Dual Language")
    print("✨" * 50)
    

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

