// Dark mode is always enabled
document.body.classList.add('dark-mode');

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