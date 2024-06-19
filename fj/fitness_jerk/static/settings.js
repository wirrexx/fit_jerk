document.addEventListener('DOMContentLoaded', function() {
    const options = document.querySelectorAll('.option input[type="radio"]');
    const selectedAvatarContainer = document.getElementById('selected-avatar');
    
    options.forEach(option => {
        option.addEventListener('change', function() {
            const label = option.parentElement.textContent.trim(); // Get text content excluding child elements
            const imgSrc = option.parentElement.querySelector('img').src;
            
            selectedAvatarContainer.innerHTML = `<img src="${imgSrc}" alt="${label}"> ${label}`;
        });
    });
});