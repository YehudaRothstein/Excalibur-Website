document.addEventListener('DOMContentLoaded', function () {
    const navbarLinks = document.querySelectorAll('.navbar-menu a');

    navbarLinks.forEach(link => {
        link.addEventListener('mouseenter', function () {
            this.querySelector('::after').style.width = '100%';
        });

        link.addEventListener('mouseleave', function () {
            this.querySelector('::after').style.width = '0';
        });
    });
});
