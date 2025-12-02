// Theme toggle
const themeToggle = document.getElementById('theme-toggle');
const savedTheme = localStorage.getItem('theme') || 'dark';
document.body.classList.add(savedTheme === 'light' ? 'light-mode' : 'dark-mode');

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const isLight = document.body.classList.contains('light-mode');
        document.body.classList.remove(isLight ? 'light-mode' : 'dark-mode');
        document.body.classList.add(isLight ? 'dark-mode' : 'light-mode');
        localStorage.setItem('theme', isLight ? 'dark' : 'light');
    });
}

// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js');
    });
}

// Progress tracking
const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');
const totalSections = document.querySelectorAll('.sidebar-nav a').length;
let completedSections = parseInt(localStorage.getItem('completedSections') || '0');

function updateProgress() {
    const percentage = (completedSections / totalSections) * 100;
    if (progressFill) progressFill.style.width = percentage + '%';
    if (progressText) progressText.textContent = Math.round(percentage) + '% Complete';
}

document.querySelectorAll('.sidebar-nav a').forEach(link => {
    link.addEventListener('click', () => {
        if (!link.classList.contains('completed')) {
            link.classList.add('completed');
            completedSections++;
            localStorage.setItem('completedSections', completedSections);
            updateProgress();
        }
    });
});

// Search functionality
function initSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;

    const searchData = [
        { title: 'Variables & Data Types', url: 'basics/variables.html' },
        { title: 'Conditionals', url: 'basics/conditionals.html' },
        { title: 'Loops', url: 'basics/loops.html' },
        { title: 'Functions', url: 'intermediate/functions.html' },
        { title: 'Classes & Objects', url: 'intermediate/classes.html' },
        { title: 'File Handling', url: 'intermediate/file_handling.html' },
        { title: 'Calculator Project', url: 'projects/calculator.html' },
        { title: 'Todo App', url: 'projects/todo_app.html' },
        { title: 'Data Analysis', url: 'projects/data_analysis.html' },
        { title: 'REST API', url: 'projects/advanced/rest_api.html' },
        { title: 'Web Scraper', url: 'projects/advanced/web_scraper.html' },
        { title: 'Chat App', url: 'projects/advanced/chat_app.html' },
        { title: 'Data Pipeline', url: 'projects/advanced/data_pipeline.html' },
        { title: 'Deployment Script', url: 'projects/advanced/deployment_script.html' }
    ];

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const results = searchData.filter(item =>
            item.title.toLowerCase().includes(query)
        );

        let dropdown = document.getElementById('search-dropdown');
        if (!dropdown) {
            dropdown = document.createElement('div');
            dropdown.id = 'search-dropdown';
            dropdown.className = 'search-dropdown';
            searchInput.parentElement.appendChild(dropdown);
        }

        if (query && results.length > 0) {
            dropdown.innerHTML = results.map(item =>
                `<a href="${item.url}">${item.title}</a>`
            ).join('');
            dropdown.style.display = 'block';
        } else {
            dropdown.style.display = 'none';
        }
    });
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});

// Add copy buttons to code blocks
document.addEventListener('DOMContentLoaded', () => {
    updateProgress();
    initSearch();

    document.querySelectorAll('pre').forEach(pre => {
        const button = document.createElement('button');
        button.textContent = 'Copy';
        button.className = 'copy-btn';
        button.addEventListener('click', () => {
            const code = pre.querySelector('code');
            const text = code ? code.textContent : pre.textContent;
            navigator.clipboard.writeText(text).then(() => {
                button.textContent = 'Copied!';
                setTimeout(() => button.textContent = 'Copy', 2000);
            });
        });
        pre.appendChild(button);
    });

    document.querySelectorAll('pre code').forEach(code => {
        const language = code.className.replace('language-', '');
        code.parentElement.setAttribute('data-language', language || 'python');
    });
});

</content>
<parameter name="filePath">script.js