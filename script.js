let time = 25 * 60;
let interval = null;

function updateDisplay() {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;
    document.getElementById("timer").innerText =
        `${minutes}:${seconds.toString().padStart(2, "0")}`;
}

function startTimer() {
    if (interval) return;
    interval = setInterval(() => {
        if (time > 0) {
            time--;
            updateDisplay();
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(interval);
    interval = null;
}

function resetTimer() {
    pauseTimer();
    time = 25 * 60;
    updateDisplay();
}

updateDisplay();



document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".check-item").forEach((checkbox) => {
        const key = checkbox.dataset.key;

        checkbox.checked = localStorage.getItem(key) === "true";

        checkbox.addEventListener("change", () => {
            localStorage.setItem(key, checkbox.checked);
        });
    });

    loadQuote();
    loadTheme();
});



const quotes = [
    "Focus on progress, not perfection.",
    "Small steps every day lead to big results.",
    "Stay consistent and trust the process.",
    "Discipline beats motivation.",
    "Do one thing at a time, and do it well.",
    "Your future self will thank you.",
    "Start where you are. Use what you have.",
    "Do it for YOU",
    "Believe you can and you're halfway there.",
    "Life is short. Enjoy it while you can.",
];

function newQuote() {
    const quote = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById("quote-text").innerText = quote;
    localStorage.setItem("quote", quote);
}

function loadQuote() {
    const saved = localStorage.getItem("quote");
    if (saved) {
        document.getElementById("quote-text").innerText = saved;
    } else {
        newQuote();
    }
}



function toggleDarkMode() {
    document.body.classList.toggle("dark");
    localStorage.setItem(
        "darkMode",
        document.body.classList.contains("dark")
    );
}

function loadTheme() {
    const dark = localStorage.getItem("darkMode") === "true";
    if (dark) {
        document.body.classList.add("dark");
    }
}
