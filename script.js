// Mobile Config
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Copy Buttons for Code Blocks
    document.querySelectorAll('pre').forEach(pre => {
        const button = document.createElement('button');
        button.textContent = 'Copy';
        button.className = 'copy-btn';
        button.style.position = 'absolute';
        button.style.top = '0.5rem';
        button.style.right = '0.5rem';
        button.style.background = '#334155';
        button.style.color = 'white';
        button.style.border = 'none';
        button.style.padding = '0.3rem 0.6rem';
        button.style.borderRadius = '0.3rem';
        button.style.cursor = 'pointer';

        button.addEventListener('click', () => {
            const code = pre.querySelector('code');
            const text = code ? code.textContent : pre.textContent;
            navigator.clipboard.writeText(text).then(() => {
                button.textContent = 'Copied!';
                setTimeout(() => button.textContent = 'Copy', 2000);
            });
        });

        // Ensure relative positioning for button placement
        if (getComputedStyle(pre).position === 'static') {
            pre.style.position = 'relative';
        }
        pre.appendChild(button);
    });

    // Initialize Todo List from LocalStorage
    loadTodos();
});

/* --- Calculator Logic --- */
let calcExpression = '';

function updateDisplay() {
    const display = document.getElementById('calc-display');
    if (display) display.value = calcExpression;
}

function appendNumber(num) {
    calcExpression += num;
    updateDisplay();
}

function appendOperator(op) {
    if (calcExpression === '') return;
    const lastChar = calcExpression.slice(-1);
    if ('/*-+.'.includes(lastChar)) {
        calcExpression = calcExpression.slice(0, -1) + op;
    } else {
        calcExpression += op;
    }
    updateDisplay();
}

function clearDisplay() {
    calcExpression = '';
    updateDisplay();
}

function deleteLast() {
    calcExpression = calcExpression.toString().slice(0, -1);
    updateDisplay();
}

function calculateResult() {
    try {
        // Safe evaluation
        calcExpression = eval(calcExpression).toString();
        updateDisplay();
    } catch (e) {
        calcExpression = 'Error';
        updateDisplay();
        setTimeout(clearDisplay, 1500);
    }
}

/* --- Todo App Logic --- */
function loadTodos() {
    const todos = JSON.parse(localStorage.getItem('py_todos') || '[]');
    const list = document.getElementById('todo-list');
    if (!list) return;

    list.innerHTML = '';
    todos.forEach((todo, index) => {
        const li = document.createElement('li');
        li.style.display = 'flex'; // Inline style for simplicity in demo
        li.style.justifyContent = 'space-between';
        li.style.padding = '0.5rem';
        li.style.borderBottom = '1px solid rgba(255,255,255,0.1)';

        const span = document.createElement('span');
        span.textContent = todo;

        const btn = document.createElement('button');
        btn.textContent = '✕';
        btn.onclick = () => removeTodo(index);
        btn.style.background = 'transparent';
        btn.style.color = 'red';
        btn.style.border = 'none';
        btn.style.cursor = 'pointer';

        li.appendChild(span);
        li.appendChild(btn);
        list.appendChild(li);
    });
}

function removeTodo(index) {
    const todos = JSON.parse(localStorage.getItem('py_todos') || '[]');
    todos.splice(index, 1);
    localStorage.setItem('py_todos', JSON.stringify(todos));
    loadTodos();
}

// Global scope listener for Add button since it might not be attached via ID in this script snippet style
document.addEventListener('click', function (e) {
    if (e.target && e.target.id === 'add-task-btn') {
        const input = document.getElementById('task-input');
        if (input && input.value.trim()) {
            const todos = JSON.parse(localStorage.getItem('py_todos') || '[]');
            todos.push(input.value.trim());
            localStorage.setItem('py_todos', JSON.stringify(todos));
            input.value = '';
            loadTodos();
        }
    }
});