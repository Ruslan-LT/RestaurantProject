document.addEventListener("DOMContentLoaded", function () {
    const menuButtons = document.querySelectorAll(".main_button, .filter-button");

    menuButtons.forEach(button => {
        const index = button.getAttribute("data-index");
        const dropdownMenu = document.getElementById(`dropdown-menu-${index}`);

        button.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();

            document.querySelectorAll(".dropdown-menu").forEach(menu => {
                if (menu !== dropdownMenu) {
                    menu.classList.add("hidden");
                }
            });

            dropdownMenu.classList.toggle("hidden");
        });

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


document.addEventListener("DOMContentLoaded", function () {
    const filterButton = document.querySelector(".filter-button");
    const dropdownMenu = document.getElementById("filter-dropdown-menu");

    filterButton.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        dropdownMenu.classList.toggle("hidden");
    });

    document.addEventListener("click", function (event) {
        if (!filterButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });

});

const openBtn = document.getElementById('openCartBtn');
const modal = document.getElementById('cartModal');
const closeBtn = document.getElementById('closeModalBtn');

openBtn.onclick = () => modal.style.display = "block";
closeBtn.onclick = () => modal.style.display = "none";
window.onclick = (e) => {
  if (e.target === modal) modal.style.display = "none";
}