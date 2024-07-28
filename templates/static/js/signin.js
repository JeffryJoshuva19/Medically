function validateForm() {
    var username = document.getElementById('username');
    var password = document.getElementById('password');

    var usernameError = document.getElementById('usernameError');
    var passwordnameError = document.getElementById('passwordnameError');

    usernameError.textContent = '';
    passwordnameError.textContent = '';

    if (username.value.trim() === '') {
        usernameError.textContent = 'Please enter your Username';
        username.focus();
        return false;
    }
    if (password.value.trim() === '') {
        passwordnameError.textContent = 'Please enter your Password';
        password.focus();
        return false;
    } else if (password.value.trim().length < 8) {
        passwordnameError.textContent = 'Password should be at least 8 characters';
        password.focus();
        return false;
    }

    return true;
}