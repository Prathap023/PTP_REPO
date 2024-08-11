// scripts.js

// Dynamic Gallery
document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.gallery');

    const projects = [
        { title: 'Project 1', description: 'Description of Project 1' },
        { title: 'Project 2', description: 'Description of Project 2' },
        { title: 'Project 3', description: 'Description of Project 3' },
        // Add more projects as needed
    ];

    projects.forEach(project => {
        const projectDiv = document.createElement('div');
        projectDiv.className = 'project-item';
        projectDiv.innerHTML = `<h3>${project.title}</h3><p>${project.description}</p>`;
        gallery.appendChild(projectDiv);
    });
});

// Form Validation
const form = document.getElementById('contact-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (name === '' || email === '' || message === '') {
        alert('Please fill out all fields.');
        return;
    }

    alert('Thank you for your message!');
    form.reset();
});

// Smooth Scroll
document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add to scripts.js

// Scroll Animation
const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + window.innerHeight;

    sections.forEach(section => {
        if (scrollPos > section.offsetTop + section.offsetHeight / 2) {
            section.classList.add('visible');
        }
    });
});
