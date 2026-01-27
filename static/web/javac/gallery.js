// Counter Animation for Stats
        const counters = document.querySelectorAll('.counter');
        const speed = 200;

        const animateCounter = () => {
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const increment = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + increment);
                    setTimeout(() => animateCounter(), 10);
                } else {
                    counter.innerText = target.toLocaleString();
                }
            });
        };

        // Intersection Observer for counter animation
        const statsSection = document.querySelector('.stats-section');
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        if (statsSection) {
            statsObserver.observe(statsSection);
        }

        // Smooth Scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Filter functionality
        const filterButtons = document.querySelectorAll('.filter-btn');
        const galleryItems = document.querySelectorAll('.gallery-item');

        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                button.classList.add('active');

                const filterValue = button.getAttribute('data-filter');

                galleryItems.forEach(item => {
                    if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                        item.style.display = 'block';
                        item.style.animation = 'fadeIn 0.5s';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });

        // Modal functionality for viewing full images
        const galleryCards = document.querySelectorAll('.gallery-card');
        const modal = new bootstrap.Modal(document.getElementById('imageModal'));
        const modalImage = document.getElementById('modalImage');
        const modalTitle = document.getElementById('modalTitle');
        const modalDescription = document.getElementById('modalDescription');

        galleryCards.forEach(card => {
            card.addEventListener('click', () => {
                const img = card.querySelector('img');
                if (img) {
                    const title = card.querySelector('.gallery-card-title').textContent;
                    const description = card.querySelector('.gallery-card-text').textContent;

                    modalImage.src = img.src;
                    modalImage.alt = img.alt;
                    modalTitle.textContent = title;
                    modalDescription.textContent = description;

                    modal.show();
                }
            });
        });

        // Donation Function
        function donate(amount) {
            alert(`Thank you for your generous donation of $${amount}!\n\nYou will be redirected to our secure payment gateway.`);
            // Here you would redirect to actual payment gateway
            // window.location.href = 'payment-gateway-url';
        }

        // Donation Form Submission
        const donationForm = document.getElementById('donationForm');
        donationForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you for your donation! Our team will contact you shortly to process your contribution.');
            donationForm.reset();
        });

        // Scroll reveal animation for gallery items
        window.addEventListener('load', () => {
            galleryItems.forEach((item, index) => {
                setTimeout(() => {
                    item.style.animation = 'fadeIn 0.5s forwards';
                }, index * 100);
            });
        });

        // Lazy loading for video iframes
        const videoCards = document.querySelectorAll('.video-card');
        const videoObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const iframe = entry.target.querySelector('iframe');
                    if (iframe && !iframe.src) {
                        iframe.src = iframe.getAttribute('data-src');
                    }
                }
            });
        }, { threshold: 0.1 });

        videoCards.forEach(card => {
            videoObserver.observe(card);
        });