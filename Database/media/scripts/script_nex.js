const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");

signInBtn.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});



document.addEventListener('DOMContentLoaded', function () {
    const errorCard = document.getElementById('error-card');
    const errorMessage = document.getElementById('error-message');

    // Fonction pour afficher le message d'erreur
    function showError(message) {
        errorMessage.innerHTML = message;
        errorCard.style.display = 'block';
    }

    // Fonction pour masquer le message d'erreur
    function hideError() {
        errorCard.style.display = 'none';
    }

    // Vérifiez si des erreurs existent initialement
    if (errorMessage.innerHTML.trim() !== "") {
        showError(errorMessage.innerHTML);
    }

    // Exemple : Masquer le message d'erreur après un délai (3 secondes dans cet exemple)
    setTimeout(hideError, 3000); // Cette ligne peut être utilisée pour masquer automatiquement le message après un certain délai
});

