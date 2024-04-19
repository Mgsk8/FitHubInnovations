function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const toggleButton = document.querySelector('.password-toggle');
    
    if (passwordInput.type === 'password') {
      passwordInput.type = 'text';
      toggleButton.classList.remove('bi-eye');
      toggleButton.classList.add('bi-eye-slash');
    } else {
      passwordInput.type = 'password';
      toggleButton.classList.remove('bi-eye-slash');
      toggleButton.classList.add('bi-eye');
    }
  }