/* ============================================================
   core.js
   Core JavaScript for Ahmed Zaki Portfolio
   Author: Ahmed Zaki
   Purpose: Connects frontend with Flask backend, handles animations,
            scroll interactions, API fetches, and dynamic content
   ============================================================ */

/* ============================================================
   SECTION ANIMATION ON SCROLL
   ============================================================ */
const sections = document.querySelectorAll("section");

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
}, { threshold: 0.2 });

sections.forEach(section => observer.observe(section));

/* ============================================================
   FETCH PROFILE DATA FROM PYTHON BACKEND
   ============================================================ */
fetch("/api/profile")
    .then(response => response.json())
    .then(data => {
        console.log("Profile Loaded:", data);

        // تغيير عنوان الصفحة ديناميكيًا
        document.title = data.name + " | Legendary Portfolio";

        // يمكن إضافة مزيد من التفاعل باستخدام البيانات
        // 🔴 مثال: إضافة الرؤية إلى قسم Vision
        const visionSection = document.querySelector(".vision");
        if (visionSection) {
            const p = document.createElement("p");
            p.textContent = data.vision;
            visionSection.appendChild(p);
        }
    })
    .catch(err => console.error("Failed to load profile:", err));

/* ============================================================
   RECORD VISITOR TO FLASK BACKEND (Scholarship Committee)
   ============================================================ */
fetch("/api/visit", { method: "POST" })
    .then(response => response.json())
    .then(data => console.log("Visitor logged:", data))
    .catch(err => console.error("Failed to log visitor:", err));

/* ============================================================
   DYNAMIC PROJECT CARDS CREATION EXAMPLE
   ============================================================ */
const projectsGrid = document.querySelector(".projects-grid");
if (projectsGrid) {
    const projects = [
        {
            title: "Advanced AI Assistant",
            desc: "An AI-based project enhancing creativity and productivity."
        },
        {
            title: "Cinematic Motion Design",
            desc: "A full animation project with storytelling through visuals."
        },
        {
            title: "Web Platform UX",
            desc: "Modern web platform focusing on performance and aesthetics."
        }
    ];

    projects.forEach(proj => {
        const card = document.createElement("div");
        card.classList.add("project-card");

        const h3 = document.createElement("h3");
        h3.textContent = proj.title;
        card.appendChild(h3);

        const p = document.createElement("p");
        p.textContent = proj.desc;
        card.appendChild(p);

        projectsGrid.appendChild(card);
    });
}

/* ============================================================
   SMOOTH SCROLL FOR NAVIGATION (IF ANY)
   ============================================================ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

/* ============================================================
   QUOTES HOVER EFFECT (Dynamic)
   ============================================================ */
const quotes = document.querySelectorAll(".quotes blockquote");
quotes.forEach(quote => {
    quote.addEventListener("mouseenter", () => {
        quote.style.color = "gold";
        quote.style.transform = "scale(1.05)";
        quote.style.boxShadow = "0 0 35px rgba(255,215,0,0.35)";
    });

    quote.addEventListener("mouseleave", () => {
        quote.style.color = "";
        quote.style.transform = "";
        quote.style.boxShadow = "";
    });
});

/* ============================================================
   ADDITIONAL INTERACTIVE FUNCTIONS
   ============================================================ */

/*
    🔴 يمكنك إضافة وظائف جديدة هنا:
    - Dynamic gallery
    - Interactive AI simulations
    - Real-time data from backend
*/

/* ============================================================
   END OF core.js
   ============================================================ */
