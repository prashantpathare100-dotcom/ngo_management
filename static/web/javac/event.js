// Custom JavaScript for NGO Events Page

document.addEventListener('DOMContentLoaded', function() {
    
    // Event Modal Data
    const eventData = {
        'medical-camp': {
            title: 'Free Medical Camp',
            category: 'Health',
            date: 'December 25, 2023',
            time: '9:00 AM - 4:00 PM',
            location: 'Central Park, Downtown',
            capacity: '200 participants',
            description: 'Join us for a day of free medical services including health checkups, consultations, and basic screenings. Our team of volunteer doctors and nurses will provide essential healthcare services to underserved communities.',
            expectations: [
                'Free health checkups and consultations',
                'Blood pressure and sugar level tests',
                'Basic medical screenings',
                'Health education sessions',
                'Free medication for common ailments'
            ],
            audience: 'This event is open to all community members, with priority given to low-income families and individuals without access to regular healthcare.',
            note: 'Please bring any existing medical records. No registration fee required.'
        },
        'digital-workshop': {
            title: 'Digital Literacy Workshop',
            category: 'Education',
            date: 'December 2, 2023',
            time: '10:00 AM - 2:00 PM',
            location: 'Community Center',
            capacity: '50 participants',
            description: 'Learn essential digital skills in this hands-on workshop designed for beginners. Perfect for seniors and those new to technology.',
            expectations: [
                'Basic computer operation',
                'Internet browsing and safety',
                'Email communication',
                'Microsoft Office basics',
                'Smartphone usage'
            ],
            audience: 'Open to all ages, especially recommended for seniors and individuals with limited digital experience.',
            note: 'Computers will be provided. Bring your own device if preferred.'
        },
        'cleanup-drive': {
            title: 'City Cleanup Drive',
            category: 'Environment',
            date: 'December 10, 2023',
            time: '8:00 AM - 12:00 PM',
            location: 'Riverside Park',
            capacity: '100 volunteers',
            description: 'Join our community cleanup initiative to make our city cleaner and greener. Together we can make a difference!',
            expectations: [
                'Park and riverbank cleanup',
                'Waste segregation training',
                'Recycling education',
                'Team building activities',
                'Refreshments provided'
            ],
            audience: 'All ages welcome. Families encouraged to participate. Children under 16 must be accompanied by an adult.',
            note: 'Gloves and cleanup equipment will be provided. Wear comfortable clothing and closed shoes.'
        },
        'winter-relief': {
            title: 'Winter Relief Distribution',
            category: 'Relief',
            date: 'December 15, 2023',
            time: '11:00 AM - 3:00 PM',
            location: 'Downtown Shelter',
            capacity: '75 volunteers',
            description: 'Help us distribute winter essentials to homeless and low-income families during the cold season.',
            expectations: [
                'Sorting and organizing donations',
                'Distribution of winter clothes',
                'Blanket and sleeping bag distribution',
                'Hot meal service',
                'Community engagement'
            ],
            audience: 'Volunteers of all ages. Physical ability to lift and distribute items is helpful.',
            note: 'We welcome donations of winter clothing, blankets, and non-perishable food items.'
        }
    };
    
    // Event Modal Setup
    const eventModal = document.getElementById('eventModal');
    
    if (eventModal) {
        eventModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget;
            const eventId = button.getAttribute('data-event');
            const eventInfo = eventData[eventId] || eventData['medical-camp'];
            
            // Update modal content
            document.getElementById('modalEventTitle').textContent = eventInfo.title;
            document.getElementById('modalCategory').textContent = eventInfo.category;
            document.getElementById('modalDate').textContent = eventInfo.date;
            document.getElementById('modalTime').textContent = eventInfo.time;
            document.getElementById('modalLocation').textContent = eventInfo.location;
            document.getElementById('modalCapacity').textContent = eventInfo.capacity;
            document.getElementById('modalDescription').textContent = eventInfo.description;
            document.getElementById('modalNote').textContent = eventInfo.note;
            document.getElementById('modalAudience').textContent = eventInfo.audience;
            
            // Update expectations list
            const expectationsList = document.getElementById('modalExpectations');
            expectationsList.innerHTML = '';
            eventInfo.expectations.forEach(expectation => {
                const li = document.createElement('li');
                li.textContent = expectation;
                expectationsList.appendChild(li);
            });
            
            // Update modal title
            document.getElementById('eventModalLabel').textContent = eventInfo.title;
        });
    }
    
    // Register Button Click Handler
    const registerModalBtn = document.getElementById('registerModalBtn');
    if (registerModalBtn) {
        registerModalBtn.addEventListener('click', function() {
            const eventTitle = document.getElementById('modalEventTitle').textContent;
            alert(`Thank you for your interest in "${eventTitle}"! Our team will contact you with registration details shortly.`);
            
            // Close modal
            const modal = bootstrap.Modal.getInstance(eventModal);
            modal.hide();
        });
    }
    
    // Filter Tabs Functionality
    const filterTabs = document.querySelectorAll('#eventsTab button[data-bs-toggle="pill"]');
    const eventCards = document.querySelectorAll('.event-card');
    
    filterTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const target = this.getAttribute('data-bs-target');
            
            if (target === '#all') {
                // Show all cards
                eventCards.forEach(card => {
                    card.style.display = 'block';
                    card.parentElement.style.display = 'block';
                });
            } else {
                // Filter by category
                const category = target.replace('#', '');
                
                eventCards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    if (cardCategory === category) {
                        card.style.display = 'block';
                        card.parentElement.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                        card.parentElement.style.display = 'none';
                    }
                });
            }
        });
    });
    
    // Add animation to cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-on-scroll');
            }
        });
    }, observerOptions);
    
    // Observe event cards and process steps
    document.querySelectorAll('.event-card, .process-step, .impact-stat, .gallery-item').forEach(el => {
        observer.observe(el);
    });
    
    // Add CSS for scroll animation
    const style = document.createElement('style');
    style.textContent = `
        .animate-on-scroll {
            animation: fadeInUp 0.8s ease-out forwards;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
    
    // Quick Stats Counter Animation
    function animateCounters() {
        const counters = document.querySelectorAll('.stat-number');
        
        counters.forEach(counter => {
            const target = counter.textContent.replace('+', '').replace('K', '000');
            let current = 0;
            const increment = target / 100;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    counter.textContent = counter.textContent.includes('+') ? target + '+' : 
                                          counter.textContent.includes('K') ? (target/1000).toFixed(1).replace('.0', '') + 'K' : 
                                          target;
                    clearInterval(timer);
                } else {
                    counter.textContent = Math.floor(current);
                }
            }, 20);
        });
    }
    
    // Trigger counter animation when stats come into view
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    const statsSection = document.querySelector('.quick-stats');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
});


