
document.querySelectorAll('.input-field').forEach(inputField => {
    inputField.addEventListener('focus', () => {
        inputField.classList.add('active');
    });
    inputField.addEventListener('blur', () => {
        if (inputField.value === '') {
            inputField.classList.remove('active');
        }
    });
});
document.getElementById('show-password').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        this.textContent = 'Hide';
    }
    else {
        passwordInput.type = 'password';
        this.textContent = 'Show';
    }   
});