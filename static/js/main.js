// وظيفة لتشغيل الصوت الحماسي عند الضغط على الزر
document.addEventListener('DOMContentLoaded', function() {
    const music = document.getElementById('background-music');
    
    // تشغيل/إيقاف الصوت عند الضغط على القسم
    const homeSection = document.querySelector('.home');
    homeSection.addEventListener('click', function() {
        if (music.paused) {
            music.play();
        } else {
            music.pause();
        }
    });
    
    // تأثيرات التحميل (Fade In) عند التمرير
    const sections = document.querySelectorAll('section');
    window.addEventListener('scroll', function() {
        sections.forEach(function(section) {
            if (isInViewport(section)) {
                section.style.opacity = 1;
                section.style.transform = "translateY(0)";
            } else {
                section.style.opacity = 0;
                section.style.transform = "translateY(50px)";
            }
        });
    });

    // التحقق إذا كان العنصر في نافذة العرض
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return rect.top >= 0 && rect.bottom <= window.innerHeight;
    }
});
