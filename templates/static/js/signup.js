function validateForm() {
    var username = document.getElementById('username');
    var email = document.getElementById('email');
    var password = document.getElementById('password');

    var usernameError = document.getElementById('usernameError');
    var emailnameError = document.getElementById('emailnameError');
    var passwordnameError = document.getElementById('passwordnameError');

    usernameError.textContent = '';
    emailnameError.textContent = '';
    passwordnameError.textContent = '';

    if (username.value.trim() === '') {
        usernameError.textContent = 'Please enter your Username';
        username.focus();
        return false;
    }
    if (email.value.trim() === '') {
        emailnameError.textContent = 'Please enter your Email';
        email.focus();
        return false;
    } else {
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value.trim())) {
            emailnameError.textContent = 'Please enter a valid Email address';
            email.focus();
            return false;
        }
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