document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("menu_button");
    const dropdownMenu = document.getElementById("dropdown-menu");

    menuButton.addEventListener("click", function () {
        dropdownMenu.classList.toggle("hidden");
    });

    document.addEventListener("click", function (event) {
        if (!menuButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });


    document.addEventListener("mousemove", (event) => {
        let moveX = (event.clientX / window.innerWidth - 0.5) * 10;
        let moveY = (event.clientY / window.innerHeight - 0.5) * 10;

        document.body.style.backgroundPosition = `${50 + moveX}% ${50 + moveY}%`;
    });
});