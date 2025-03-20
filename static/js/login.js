(() => {
  const passwordInput = document.getElementById("password_input");

  // showPassword.addEventListener("click", () => {
  //   passwordInput.type =
  //     passwordInput.type === "password" ? "text" : "password";
  //   // showPassword.textContent =
  //   //   passwordInput.type === "password" ? "Show" : "Hide";
  // });
})();

function showLogin() {
    document.getElementById('ImLoggingIn').style.display = 'flex';
    document.getElementById('ImCreatingAnAccount').style.display = 'none';
    document.getElementById('loginButton').classList.add('sliderButtonActive');
    document.getElementById('loginButton').classList.remove('sliderButtonInactive');
    document.getElementById('signinButton').classList.add('sliderButtonInactive');
    document.getElementById('signinButton').classList.remove('sliderButtonActive');
}

function showSignup() {
    document.getElementById('ImLoggingIn').style.display = 'none';
    document.getElementById('ImCreatingAnAccount').style.display = 'flex';
    document.getElementById('loginButton').classList.add('sliderButtonInactive');
    document.getElementById('loginButton').classList.remove('sliderButtonActive');
    document.getElementById('signinButton').classList.add('sliderButtonActive');
    document.getElementById('signinButton').classList.remove('sliderButtonInactive');
}
