document.addEventListener("DOMContentLoaded", function () {
    const menuButtons = document.querySelectorAll(".main_button");

    menuButtons.forEach(button => {
        const index = button.getAttribute("data-index");
        const dropdownMenu = document.getElementById(`dropdown-menu-${index}`);

        button.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();

            // Закриваємо всі інші відкриті меню перед відкриттям нового
            document.querySelectorAll(".dropdown-menu").forEach(menu => {
                if (menu !== dropdownMenu) {
                    menu.classList.add("hidden");
                }
            });

            dropdownMenu.classList.toggle("hidden");
        });

        // Закриття меню при кліку поза ним
        document.addEventListener("click", function (event) {
            if (!button.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add("hidden");
            }
        });
    });

    document.addEventListener("mousemove", (event) => {
        let moveX = (event.clientX / window.innerWidth - 0.5) * 10;
        let moveY = (event.clientY / window.innerHeight - 0.5) * 10;
        document.body.style.backgroundPosition = `${50 + moveX}% ${50 + moveY}%`;
    });
});