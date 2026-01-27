document.getElementById('volunteerForm').addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent actual page reload
            
            // Simulate sending data
            const btn = this.querySelector('button');
            const originalText = btn.innerText;
            
            btn.innerText = 'Sending...';
            btn.disabled = true;

            setTimeout(() => {
                alert('Thank you for registering! We will contact you soon.');
                btn.innerText = 'Submitted!';
                this.reset(); // Clear form
                
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.disabled = false;
                }, 2000);
            }, 1500);
        });