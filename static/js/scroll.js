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

    const scrollElements = document.querySelectorAll('.content, .image-section, .sponsors-section, .videos-section, footer');

    const elementInView = (el, dividend = 1) => {
        const elementTop = el.getBoundingClientRect().top;

        return (
            elementTop <=
            (window.innerHeight || document.documentElement.clientHeight) / dividend
        );
    };

    const displayScrollElement = (element) => {
        element.classList.add('scrolled');
    };

    const hideScrollElement = (element) => {
        element.classList.remove('scrolled');
    };

    const handleScrollAnimation = () => {
        scrollElements.forEach((el) => {
            if (elementInView(el, 1.25)) {
                displayScrollElement(el);
            } else {
                hideScrollElement(el);
            }
        });
    };

    window.addEventListener('scroll', () => {
        handleScrollAnimation();
    });
});
