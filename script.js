document.addEventListener("DOMContentLoaded", function () {
    
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            card.classList.add('touched');
            setTimeout(() => card.classList.remove('touched'), 300);
        });
    });

    const scrollBtn = document.getElementById("backToTop");
    window.addEventListener("scroll", () => {
        scrollBtn.style.display = window.scrollY > 300 ? "block" : "none";
    });

    scrollBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
