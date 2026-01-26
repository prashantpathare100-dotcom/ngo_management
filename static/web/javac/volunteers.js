document.getElementById('volunteerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Simple success message
    alert('Thank you! 🙏 Your application has been received. We will contact you within 24 hours.');
    
    // Reset form
    this.reset();
    
    // Optional: Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
});