// Fonction pour afficher un message d'erreur ou de succès
function showMessage(message, className) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ' + className;
    messageDiv.textContent = message;
    document.body.insertBefore(messageDiv, document.body.firstChild);

    setTimeout(function() {
        messageDiv.remove();
    }, 3000);
}

// Récupérer les paramètres d'URL
function getUrlParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

// Vérifier si le paramètre d'URL est présent
function isUrlParamPresent(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.has(param);
}

// Exemple d'utilisation pour afficher un message de succès
if (isUrlParamPresent('success')) {
    const successMessage = getUrlParam('success');
    showMessage(successMessage, 'success');
}

// Exemple d'utilisation pour afficher un message d'erreur
if (isUrlParamPresent('error')) {
    const errorMessage = getUrlParam('error');
    showMessage(errorMessage, 'error');
}
