// Progress tracking using localStorage
const lessons = {
    basics: ['variables', 'conditionals', 'loops'],
    intermediate: ['functions', 'classes', 'file_handling'],
    projects: ['calculator', 'todo_app', 'data_analysis', 'rest_api', 'web_scraper']
};

function updateProgress() {
    let totalCompleted = 0;
    let totalLessons = 0;

    Object.keys(lessons).forEach(module => {
        const moduleLessons = lessons[module];
        let completed = 0;
        moduleLessons.forEach(lesson => {
            if (localStorage.getItem(`lesson_${lesson}`) === 'completed') {
                completed++;
                totalCompleted++;
            }
        });
        totalLessons += moduleLessons.length;
        document.getElementById(`${module}-progress`).textContent = `${completed}/${moduleLessons.length}`;
    });

    const overallPercent = Math.round((totalCompleted / totalLessons) * 100);
    document.getElementById('overall-progress').textContent = `${overallPercent}%`;
    document.getElementById('progress-fill').style.width = `${overallPercent}%`;
}

// Mark lesson as completed when clicked
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.lesson-link').forEach(link => {
        link.addEventListener('click', (e) => {
            const lesson = e.target.dataset.lesson;
            localStorage.setItem(`lesson_${lesson}`, 'completed');
            updateProgress();
        });
    });
    updateProgress();
});

// Dark mode is always enabled
document.body.classList.add('dark-mode');

// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js');
    });
}



// Add copy buttons to code blocks
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('pre').forEach(pre => {
        const button = document.createElement('button');
        button.textContent = 'Copy';
        button.className = 'copy-btn';
        button.addEventListener('click', () => {
            navigator.clipboard.writeText(pre.textContent).then(() => {
                button.textContent = 'Copied!';
                setTimeout(() => button.textContent = 'Copy', 2000);
            });
        });
        pre.appendChild(button);
    });
});

</content>
<parameter name="filePath">script.js