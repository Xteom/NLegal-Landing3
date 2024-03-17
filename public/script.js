document.addEventListener('DOMContentLoaded', function() {
    // Using querySelector to select a single element
    const button = document.querySelector('#changeText');
    
    // Event listener for the button
    button.addEventListener('click', function() {
        // Using querySelector to select the first paragraph with class 'message'
        const message = document.querySelector('.message');
        
        // Change the text of the first paragraph
        message.textContent = 'Text changed!';
        
        // Selecting the first paragraph with the class 'highlight'
        const highlightedMessage = document.querySelector('.message.highlight');
        
        // Change the style of the highlighted message
        highlightedMessage.style.backgroundColor = 'yellow';
    });
});


