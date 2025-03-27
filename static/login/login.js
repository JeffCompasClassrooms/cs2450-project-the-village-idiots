(() => {
  const passwordInput = document.getElementById("password_input");
  const loginButton = document.getElementById('loginButton');
  const signinButton = document.getElementById('signinButton'); // added to make sure the slider buttons do not get an outline momentarially 

  [loginButton, signinButton].forEach(button => {
    button.addEventListener('mousedown', (e) => {
      e.preventDefault();
    }); button.addEventListener('click', () => {
      button.blur(); //to remove focus from the button and remove the outline
    });
  });
  document.addEventListener('DOMContentLoaded', () => {
    const toggleIcon = document.getElementsByClassName("passwordToggleIcon");
    toggleIcon.classList.add('password-closed');
  });
})();

//function to toggle the visibility of the password and to toggle the eye icon
function togglePassword() {
  var password = document.getElementById("password_input");
  var new_password = document.getElementById("new_password");
  var toggleIcons = document.getElementsByClassName("passwordToggleIcon");
  
  var activePasswordInput = password.offsetParent !== null ? password : new_password;
  var activeToggleIcon = activePasswordInput === password ? toggleIcons[0] : toggleIcons[1];
  
  if(activePasswordInput.type === "password") {
    activePasswordInput.type = "text";
    activeToggleIcon.src = "/static/login/images/eye_open.svg";
    activeToggleIcon.classList.add('password-closed');
  } else {
    activePasswordInput.type = "password";
    activeToggleIcon.src = "/static/login/images/eye_closed.svg";
    activeToggleIcon.classList.remove('password-closed');
  }
}

function showLogin() {
  const loginButton = document.getElementById('loginButton');
  const signinButton = document.getElementById('signinButton');

  document.getElementById('ImLoggingIn').style.display = 'flex';
  document.getElementById('ImCreatingAnAccount').style.display = 'none';

  loginButton.classList.add('sliderButtonActive');
  loginButton.classList.remove('sliderButtonInactive');  
  signinButton.classList.add('sliderButtonInactive');
  signinButton.classList.remove('sliderButtonActive');
}

function showSignup() {
  const loginButton = document.getElementById('loginButton');
  const signinButton = document.getElementById('signinButton');

  document.getElementById('ImLoggingIn').style.display = 'none';
  document.getElementById('ImCreatingAnAccount').style.display = 'flex';
  loginButton.classList.add('sliderButtonInactive');
  loginButton.classList.remove('sliderButtonActive');
  signinButton.classList.add('sliderButtonActive');
  signinButton.classList.remove('sliderButtonInactive');
}
