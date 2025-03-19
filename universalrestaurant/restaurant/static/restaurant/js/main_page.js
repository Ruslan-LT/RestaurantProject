document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("menu_button");
    const dropdownMenu = document.getElementById("dropdown-menu");

    menuButton.addEventListener("click", function () {
        dropdownMenu.classList.toggle("hidden"); // Перемикає клас, що приховує меню
    });


    document.addEventListener("click", function (event) {
        if (!menuButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });
});