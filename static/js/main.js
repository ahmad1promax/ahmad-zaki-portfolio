/* ============================================================
   sound.js
   Music & Sound Effects for Ahmed Zaki Portfolio
   Author: Ahmed Zaki
   Purpose: Handles background epic music, button interactions,
            and audio effects for inspiration and engagement
   ============================================================ */

/* ============================================================
   SELECT ELEMENTS
   ============================================================ */
const musicBtn = document.getElementById("musicBtn");
const bgMusic = document.getElementById("bgMusic");

/* ============================================================
   BACKGROUND MUSIC CONTROL (BUTTON MODE)
   ============================================================ */
let isPlaying = false;

musicBtn.addEventListener("click", () => {
    if (!isPlaying) {
        bgMusic.play();
        musicBtn.textContent = "⏸ Pause Music";
        isPlaying = true;
    } else {
        bgMusic.pause();
        musicBtn.textContent = "▶ Play Epic Music";
        isPlaying = false;
    }
});

/* ============================================================
   ADDITIONAL SOUND EFFECTS
   ============================================================ */

/*
   🔴 مثال: صوت عند تمرير الماوس على المشاريع
   يمكنك استبدال الصوت بصوتك الخاص في static/music/
*/
const hoverSound = new Audio("/static/music/hover.mp3");

const projectCards = document.querySelectorAll(".project-card");
projectCards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});

/* ============================================================
   OPTIONAL CLICK SOUND
   ============================================================ */
const clickSound = new Audio("/static/music/click.mp3");

// إضافة صوت عند الضغط على كل الزرار
document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        clickSound.currentTime = 0;
        clickSound.play();
    });
});

/* ============================================================
   DYNAMIC MUSIC SETTINGS
   ============================================================ */

/*
   🔴 يمكنك تعديل حجم الصوت الافتراضي أو مستوى الاستماع
*/
bgMusic.volume = 0.35;
hoverSound.volume = 0.25;
clickSound.volume = 0.2;

/* ============================================================
   LOOP BACKGROUND MUSIC
   ============================================================ */
bgMusic.loop = true;

/* ============================================================
   END OF sound.js
   ============================================================ */
