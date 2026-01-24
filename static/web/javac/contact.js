// Contact Form Submission
document.getElementById('contactForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    
    // Simple validation
    if(name && email && message) {
        // In real application, you would send data to server here
        alert(`Thank you ${name}! Your message has been sent successfully. We will contact you soon.`);
        
        // Reset form
        document.getElementById('contactForm').reset();
    } else {
        alert('Please fill all required fields.');
    }
});