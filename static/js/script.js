// Navbar
const hamburger = document.querySelector(".hamburger");
const items = document.querySelector(".items")

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    items.classList.toggle("active")
})

document.querySelectorAll(".items").forEach( n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    items.classList.remove("active") ;      
    }))


document.addEventListener("DOMContentLoaded", function() {
const nav = document.querySelector('.nav');

window.addEventListener('scroll', function() {
    if (window.scrollY > 0) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});
});  

//About

var typed = new Typed(".auto-type", {
    strings: ["Front-End developer.", "Back-End developer.", "Full-Stack developer."],
    typeSpeed:150,
    backSpeed:150,
    loop: true


})

//Skills
const skillsSection = document.getElementById('skills');
const technicalSkills = document.querySelector('.technical-skills');
const tools = document.querySelector('.tools');

const handleScroll = () => {
    const skillsSectionRect = skillsSection.getBoundingClientRect();

    if (skillsSectionRect.top < window.innerHeight * 0.5) {
        technicalSkills.classList.add('active');
        tools.classList.add('active');

        // Remove the scroll event listener to prevent interference
        window.removeEventListener('scroll', handleScroll);
    }
};

window.addEventListener('scroll', handleScroll);

// Initial check in case the skills section is already visible on page load
handleScroll();