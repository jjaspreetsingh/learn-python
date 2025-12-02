// Dark mode is always enabled
document.body.classList.add('dark-mode');

// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js');
    });
}

// Progress tracking
const progressKey = 'python-learning-progress';

function updateProgress() {
    const progress = JSON.parse(localStorage.getItem(progressKey) || '{}');
    const currentPage = window.location.pathname;
    progress[currentPage] = true;
    localStorage.setItem(progressKey, JSON.stringify(progress));

    const totalPages = 15;
    const completedPages = Object.keys(progress).length;
    const percentage = Math.round((completedPages / totalPages) * 100);

    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.progress-text');

    if (progressFill) progressFill.style.width = percentage + '%';
    if (progressText) progressText.textContent = `${percentage}% Complete (${completedPages}/${totalPages})`;
}

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