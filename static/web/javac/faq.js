// After DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // FAQ search functionality
    const faqSearch = document.getElementById('faqSearch');
    const accordionItems = document.querySelectorAll('.accordion-item');
    
    if (faqSearch) {
        faqSearch.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            
            accordionItems.forEach(item => {
                const question = item.querySelector('.accordion-button span').textContent.toLowerCase();
                const answer = item.querySelector('.accordion-body').textContent.toLowerCase();
                
                if (question.includes(searchTerm) || answer.includes(searchTerm)) {
                    item.style.display = 'block';
                    // Highlight the question
                    if (searchTerm.length > 0) {
                        highlightText(item, searchTerm);
                    } else {
                        removeHighlight(item);
                    }
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
    
    // Category filtering
    const categoryButtons = document.querySelectorAll('.category-btn');
    
    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Set active button
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const selectedCategory = this.getAttribute('data-category');
            
            // Filter FAQs
            accordionItems.forEach(item => {
                const itemCategory = item.getAttribute('data-category');
                
                if (selectedCategory === 'all' || itemCategory === selectedCategory) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
    
    // Function to highlight text
    function highlightText(element, searchTerm) {
        const questionElement = element.querySelector('.accordion-button span');
        const answerElement = element.querySelector('.accordion-body');
        
        highlightTextInElement(questionElement, searchTerm);
        highlightTextInElement(answerElement, searchTerm);
    }
    
    function highlightTextInElement(element, searchTerm) {
        const text = element.textContent;
        const regex = new RegExp(`(${searchTerm})`, 'gi');
        const highlightedText = text.replace(regex, '<mark class="bg-warning">$1</mark>');
        
        // Set as HTML not just textContent
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = highlightedText;
        
        // Replace original element
        const parent = element.parentNode;
        parent.replaceChild(tempDiv.firstChild, element);
    }
    
    function removeHighlight(element) {
        const marks = element.querySelectorAll('mark');
        marks.forEach(mark => {
            const parent = mark.parentNode;
            parent.replaceChild(document.createTextNode(mark.textContent), mark);
        });
    }
    
    // Add shadow to navbar on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.05)';
        }
    });
    
    // Smooth scroll when FAQ question clicked
    const accordionButtons = document.querySelectorAll('.accordion-button');
    accordionButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Scroll with delay so collapse animation completes
            setTimeout(() => {
                this.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }, 300);
        });
    });
    
    // Print FAQ feature
    const printButton = document.createElement('button');
    printButton.innerHTML = '<i class="fas fa-print me-2"></i>Print FAQ';
    printButton.className = 'btn btn-outline-secondary d-none d-md-inline-block position-fixed bottom-0 end-0 m-4';
    printButton.style.zIndex = '1000';
    printButton.addEventListener('click', function() {
        window.print();
    });
    document.body.appendChild(printButton);
});