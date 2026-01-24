

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS Animation
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        offset: 100
    });

    

    // ===== Smooth Scroll for Navigation Links =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    navbarCollapse.classList.remove('show');
                }
            }
        });
    });

    // ===== Counter Animation =====
    function animateCounter(counter) {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString();
            }
        };

        updateCounter();
    }

    // Intersection Observer for Counter Animation
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = entry.target.querySelectorAll('.counter');
                counters.forEach(counter => animateCounter(counter));
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    // Observe hero stats and donor stats
    document.querySelectorAll('.hero-stats, .donors-stats, .stat-item').forEach(section => {
        counterObserver.observe(section);
    });

    // ===== Payment Modal Functionality =====
    const paymentModal = document.getElementById('paymentModal');
    const amountBtns = document.querySelectorAll('.amount-btn');
    const customAmountInput = document.getElementById('customDonationAmount');
    const donateAmountBtn = document.getElementById('donateAmountBtn');
    const modalCauseName = document.getElementById('modalCauseName');
    
    let selectedAmount = 1000;

    // Set cause name when opening modal
    document.querySelectorAll('.btn-donate-card').forEach(btn => {
        btn.addEventListener('click', function() {
            const causeName = this.getAttribute('data-cause');
            const defaultAmount = this.getAttribute('data-amount');
            
            modalCauseName.textContent = causeName;
            selectedAmount = parseInt(defaultAmount);
            updateDonateButton();
            
            // Reset amount buttons
            amountBtns.forEach(b => b.classList.remove('active'));
            amountBtns.forEach(b => {
                if (parseInt(b.getAttribute('data-amount')) === selectedAmount) {
                    b.classList.add('active');
                }
            });
            customAmountInput.value = '';
        });
    });

    // Amount button selection
    amountBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            amountBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selectedAmount = parseInt(this.getAttribute('data-amount'));
            customAmountInput.value = '';
            updateDonateButton();
        });
    });

    // Custom amount input
    if (customAmountInput) {
        customAmountInput.addEventListener('input', function() {
            if (this.value) {
                amountBtns.forEach(b => b.classList.remove('active'));
                selectedAmount = parseInt(this.value) || 0;
                updateDonateButton();
            }
        });
    }

    function updateDonateButton() {
        if (donateAmountBtn) {
            donateAmountBtn.textContent = selectedAmount.toLocaleString('en-IN');
        }
    }

    // ===== Card Number Formatting =====
    const cardNumberInput = document.getElementById('cardNumber');
    if (cardNumberInput) {
        cardNumberInput.addEventListener('input', function() {
            let value = this.value.replace(/\s/g, '').replace(/\D/g, '');
            let formatted = value.match(/.{1,4}/g)?.join(' ') || '';
            this.value = formatted;
        });
    }

    // ===== Expiry Date Formatting =====
    const expiryInput = document.getElementById('expiryDate');
    if (expiryInput) {
        expiryInput.addEventListener('input', function() {
            let value = this.value.replace(/\D/g, '');
            if (value.length >= 2) {
                value = value.substring(0, 2) + '/' + value.substring(2);
            }
            this.value = value;
        });
    }

    // ===== Online Payment Form Submission =====
    const onlinePaymentForm = document.getElementById('onlinePaymentForm');
    if (onlinePaymentForm) {
        onlinePaymentForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validate amount
            if (selectedAmount <= 0) {
                alert('Please select or enter a valid donation amount.');
                return;
            }

            // Simulate payment processing
            const submitBtn = this.querySelector('.btn-donate-submit');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
            submitBtn.disabled = true;

            setTimeout(() => {
                // Hide payment modal
                const paymentModalInstance = bootstrap.Modal.getInstance(paymentModal);
                paymentModalInstance.hide();

                // Generate transaction ID
                const transactionId = 'TXN' + Date.now().toString().slice(-10);

                // Show success modal
                document.getElementById('successAmount').textContent = '₹' + selectedAmount.toLocaleString('en-IN');
                document.getElementById('transactionId').textContent = transactionId;

                const successModal = new bootstrap.Modal(document.getElementById('successModal'));
                successModal.show();

                // Reset form
                onlinePaymentForm.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                selectedAmount = 1000;
                updateDonateButton();
                amountBtns.forEach(b => b.classList.remove('active'));
                amountBtns[2].classList.add('active');
            }, 2000);
        });
    }

    // ===== Copy to Clipboard Functionality =====
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const textToCopy = this.getAttribute('data-copy');
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalHTML = this.innerHTML;
                this.innerHTML = '<i class="bi bi-check"></i> Copied!';
                this.classList.add('btn-success');
                this.classList.remove('btn-outline-primary', 'btn-primary');
                
                setTimeout(() => {
                    this.innerHTML = originalHTML;
                    this.classList.remove('btn-success');
                    this.classList.add('btn-outline-primary');
                }, 2000);
            });
        });
    });

    // ===== Video Modal Functionality =====
    const videoModal = document.getElementById('videoModal');
    const videoFrame = document.getElementById('videoFrame');

    document.querySelectorAll('.video-thumbnail').forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const videoUrl = this.getAttribute('data-video');
            videoFrame.src = videoUrl + '?autoplay=1';
            const modal = new bootstrap.Modal(videoModal);
            modal.show();
        });
    });

    // Stop video when modal closes
    videoModal.addEventListener('hidden.bs.modal', function() {
        videoFrame.src = '';
    });

    // ===== Contact Form Submission =====
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending...';
            submitBtn.disabled = true;

            setTimeout(() => {
                alert('Thank you for your message! We will get back to you soon.');
                contactForm.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 1500);
        });
    }

    // ===== Newsletter Form Submission =====
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';
            submitBtn.disabled = true;

            setTimeout(() => {
                alert('Thank you for subscribing! You will receive updates at ' + emailInput.value);
                newsletterForm.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 1000);
        });
    }

    // ===== Donors Marquee Animation =====
    const donorsTrack = document.querySelector('.donors-track');
    if (donorsTrack) {
        // Clone donor cards for infinite scroll
        const donorCards = donorsTrack.innerHTML;
        donorsTrack.innerHTML = donorCards + donorCards;
    }

    // ===== Back to Top Button =====
    const backToTopBtn = document.createElement('button');
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.innerHTML = '<i class="bi bi-arrow-up"></i>';
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 500) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ===== Form Input Validation Styling =====
    const formInputs = document.querySelectorAll('.form-control, .form-select');
    formInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && this.checkValidity()) {
                this.style.borderColor = '#2EC4B6';
            } else if (this.value && !this.checkValidity()) {
                this.style.borderColor = '#e74c3c';
            }
        });

        input.addEventListener('focus', function() {
            this.style.borderColor = '#FF6B35';
        });
    });

    // ===== Phone Number Formatting =====
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(phoneInput => {
        phoneInput.addEventListener('input', function() {
            let value = this.value.replace(/\D/g, '');
            if (value.length > 10) {
                value = value.substring(0, 10);
            }
            if (value.length >= 6) {
                value = value.substring(0, 5) + ' ' + value.substring(5);
            }
            this.value = value;
        });
    });

    // ===== Lazy Loading for Images =====
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));

    // ===== Parallax Effect for Hero =====
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroVideo = document.querySelector('.hero-video');
        if (heroVideo && scrolled < window.innerHeight) {
            heroVideo.style.transform = 'translateY(' + scrolled * 0.5 + 'px)';
        }
    });

    // ===== Active Nav Link on Scroll =====
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link:not(.btn-donate-nav)');

    function highlightNavLink() {
        const scrollPos = window.scrollY + 150;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + sectionId) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', highlightNavLink);

    // ===== Typing Effect for Hero (Optional) =====
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.textContent = '';
        
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    }

    // ===== Add animation class when elements come into view =====
    const animateOnScroll = document.querySelectorAll('.cause-card, .seva-card, .video-card');
    
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    animateOnScroll.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.5s ease';
        scrollObserver.observe(el);
    });

    // ===== Handle Payment Tab Change =====
    const paymentTabs = document.querySelectorAll('#paymentTabs .nav-link');
    paymentTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Add any specific logic for payment tab changes
            console.log('Payment method changed to:', this.textContent.trim());
        });
    });

    // ===== Progress Bar Animation =====
    const progressBars = document.querySelectorAll('.progress-bar');
    const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const width = entry.target.style.width;
                entry.target.style.width = '0';
                setTimeout(() => {
                    entry.target.style.width = width;
                    entry.target.style.transition = 'width 1.5s ease';
                }, 100);
                progressObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => progressObserver.observe(bar));

    // ===== Dynamic Year in Footer =====
    const yearSpan = document.querySelector('.footer-bottom p');
    if (yearSpan) {
        yearSpan.innerHTML = yearSpan.innerHTML.replace('2024', new Date().getFullYear());
    }

    // ===== Preloader (Optional) =====
    window.addEventListener('load', function() {
        const loader = document.querySelector('.page-loader');
        if (loader) {
            loader.classList.add('hidden');
            setTimeout(() => loader.remove(), 500);
        }
    });

    // ===== Initialize Tooltips =====
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    console.log('Samajseva Foundation - Donate Page Initialized Successfully!');
});

// ===== Service Worker Registration (for PWA) =====
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // navigator.serviceWorker.register('/sw.js')
        //     .then(registration => console.log('SW registered'))
        //     .catch(error => console.log('SW registration failed'));
    });
}