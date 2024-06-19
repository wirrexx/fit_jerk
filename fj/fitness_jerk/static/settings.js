document.addEventListener('DOMContentLoaded', function() {
    const options = document.querySelectorAll('.option input[type="radio"]');
    const selectedAvatarContainer = document.getElementById('selected-avatar');
    let selectedRadio = null;

    options.forEach(option => {
        option.addEventListener('click', function() {
            if (selectedRadio === this) {
                this.checked = false;
                selectedAvatarContainer.innerHTML = ''; // Clear the avatar display
                selectedRadio = null;
            } else {
                selectedRadio = this;
                const label = option.parentElement.textContent.trim(); // Get text content excluding child elements
                const imgSrc = option.parentElement.querySelector('img').src;
                
                selectedAvatarContainer.innerHTML = `<img src="${imgSrc}" alt="${label}"> ${label}`;
            }
        });
    });
});