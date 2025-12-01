// Calculator functionality
document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('calc-display');
    let currentInput = '';
    let operator = '';
    let previousInput = '';

    document.querySelectorAll('.calc-btn').forEach(button => {
        button.addEventListener('click', () => {
            const value = button.dataset.value;

            if (value === 'C') {
                currentInput = '';
                operator = '';
                previousInput = '';
                display.value = '';
            } else if (value === '=') {
                if (previousInput && operator && currentInput) {
                    const result = calculate(parseFloat(previousInput), parseFloat(currentInput), operator);
                    display.value = result;
                    currentInput = result.toString();
                    operator = '';
                    previousInput = '';
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                if (currentInput) {
                    if (previousInput && operator) {
                        const result = calculate(parseFloat(previousInput), parseFloat(currentInput), operator);
                        display.value = result;
                        previousInput = result.toString();
                    } else {
                        previousInput = currentInput;
                    }
                    operator = value;
                    currentInput = '';
                }
            } else {
                currentInput += value;
                display.value = currentInput;
            }
        });
    });

    function calculate(a, b, op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return b !== 0 ? a / b : 'Error';
            default: return 0;
        }
    }
});</content>
<parameter name="filePath">projects/calculator.js