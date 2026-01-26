document.addEventListener('DOMContentLoaded', function () {

    /* ===== AOS Init ===== */
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }

    /* ===== Smooth Scroll ===== */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (!target) return;

            e.preventDefault();
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });

            // Close mobile navbar if open
            const navbarCollapse = document.querySelector('.navbar-collapse.show');
            if (navbarCollapse) {
                const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                if (bsCollapse) {
                    bsCollapse.hide();
                }
            }
        });
    });

    /* ===== Counter Animation ===== */
    function animateCounter(counter) {
        const target = parseInt(counter.dataset.target) || 0;
        if (target <= 0) return;
        
        let current = 0;
        const duration = 1500; // 1.5 seconds
        const stepTime = 20; // 20ms per frame
        const totalSteps = duration / stepTime;
        const increment = target / totalSteps;
        let step = 0;

        const timer = setInterval(() => {
            step++;
            current += increment;
            if (step >= totalSteps) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current).toLocaleString();
        }, stepTime);
    }

    // Initialize counter animation when in viewport
    const initCounterAnimation = () => {
        const counters = document.querySelectorAll('.counter');
        if (!counters.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    if (!counter.classList.contains('animated')) {
                        counter.classList.add('animated');
                        animateCounter(counter);
                    }
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            observer.observe(counter);
        });
    };

    initCounterAnimation();

    /* ===== Payment Modal Functionality ===== */
    const paymentModal = document.getElementById('paymentModal');
    const donateAmountBtn = document.getElementById('donateAmountBtn');
    const modalCauseName = document.getElementById('modalCauseName');
    const amountBtns = document.querySelectorAll('.amount-btn');
    const customAmountInput = document.getElementById('customDonationAmount');

    let selectedAmount = 1000;

    function updateDonateButton() {
        if (donateAmountBtn) {
            donateAmountBtn.textContent = selectedAmount.toLocaleString('en-IN');
        }
    }

    // Donate card button click
    document.querySelectorAll('.btn-donate-card').forEach(btn => {
        btn.addEventListener('click', function() {
            const cause = this.getAttribute('data-cause') || '';
            const amount = parseInt(this.getAttribute('data-amount')) || 1000;
            
            if (modalCauseName) {
                modalCauseName.textContent = cause;
            }
            
            selectedAmount = amount;
            updateDonateButton();

            // Update amount buttons
            amountBtns.forEach(btn => {
                btn.classList.remove('active');
                if (parseInt(btn.getAttribute('data-amount')) === selectedAmount) {
                    btn.classList.add('active');
                }
            });
            
            if (customAmountInput) {
                customAmountInput.value = '';
            }
        });
    });

    // Amount button click
    amountBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            amountBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selectedAmount = parseInt(this.getAttribute('data-amount')) || 0;
            
            if (customAmountInput) {
                customAmountInput.value = '';
            }
            updateDonateButton();
        });
    });

    // Custom amount input
    if (customAmountInput) {
        customAmountInput.addEventListener('input', function() {
            amountBtns.forEach(b => b.classList.remove('active'));
            selectedAmount = parseInt(this.value) || 0;
            updateDonateButton();
        });
    }

    /* ===== Online Payment Submit ===== */
    const onlinePaymentForm = document.getElementById('onlinePaymentForm');
    if (onlinePaymentForm) {
        onlinePaymentForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (selectedAmount <= 0) {
                alert('कृपया वैध रक्कम प्रविष्ट करा');
                return;
            }

            const submitBtn = this.querySelector('.btn-donate-submit');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'प्रक्रिया करत आहे...';
            submitBtn.disabled = true;

            // Simulate payment processing
            setTimeout(() => {
                // Close payment modal
                const modal = bootstrap.Modal.getInstance(paymentModal);
                if (modal) {
                    modal.hide();
                }

                // Update success modal
                const successAmount = document.getElementById('successAmount');
                const transactionId = document.getElementById('transactionId');
                
                if (successAmount) {
                    successAmount.textContent = '₹' + selectedAmount.toLocaleString('en-IN');
                }
                
                if (transactionId) {
                    transactionId.textContent = 'TXN' + Date.now();
                }

                // Show success modal
                const successModal = new bootstrap.Modal(document.getElementById('successModal'));
                successModal.show();

                // Reset form
                this.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                
                // Reset amount selection
                selectedAmount = 1000;
                updateDonateButton();
                amountBtns.forEach(b => {
                    b.classList.remove('active');
                    if (parseInt(b.getAttribute('data-amount')) === 1000) {
                        b.classList.add('active');
                    }
                });
                
            }, 1500);
        });
    }

    /* ===== Video Modal ===== */
    const videoModal = document.getElementById('videoModal');
    const videoFrame = document.getElementById('videoFrame');

    document.querySelectorAll('.video-thumbnail').forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const videoUrl = this.getAttribute('data-video');
            if (!videoUrl || !videoFrame) return;

            videoFrame.src = videoUrl + '?autoplay=1&rel=0';
            const videoModalInstance = new bootstrap.Modal(videoModal);
            videoModalInstance.show();
        });
    });

    if (videoModal) {
        videoModal.addEventListener('hidden.bs.modal', function() {
            if (videoFrame) {
                videoFrame.src = '';
            }
        });
    }

    /* ===== Copy to Clipboard ===== */
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const text = this.getAttribute('data-copy');
            if (!text) return;

            navigator.clipboard.writeText(text).then(() => {
                const originalHTML = this.innerHTML;
                this.innerHTML = '<i class="bi bi-check"></i> Copied';
                this.classList.add('btn-success');
                this.classList.remove('btn-outline-primary');

                setTimeout(() => {
                    this.innerHTML = originalHTML;
                    this.classList.remove('btn-success');
                    this.classList.add('btn-outline-primary');
                }, 2000);
            }).catch(err => {
                console.error('Copy failed:', err);
                alert('कॉपी करण्यात अडचण आली. कृपया मॅन्युअली कॉपी करा.');
            });
        });
    });

    /* ===== Back To Top Button ===== */
    const backToTopBtn = document.createElement('button');
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.innerHTML = '<i class="bi bi-chevron-up"></i>';
    backToTopBtn.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    /* ===== Contact Form ===== */
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'पाठवत आहे...';
            submitBtn.disabled = true;

            // Simulate form submission
            setTimeout(() => {
                alert('तुमचा संदेश यशस्वीरित्या पाठवला गेला आहे! आम्ही लवकरच तुमच्याशी संपर्क साधू.');
                this.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 1000);
        });
    }

    /* ===== Newsletter Form ===== */
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            
            if (!emailInput.value) {
                alert('कृपया ईमेल पत्ता प्रविष्ट करा');
                return;
            }

            const btn = this.querySelector('button');
            const originalText = btn.innerHTML;
            btn.innerHTML = 'सबस्क्राइब करत आहे...';
            btn.disabled = true;

            setTimeout(() => {
                alert('तुमची सदस्यता यशस्वीरित्या घेतली गेली आहे! धन्यवाद.');
                emailInput.value = '';
                btn.innerHTML = originalText;
                btn.disabled = false;
            }, 800);
        });
    }

    /* ===== Footer Year Update ===== */
    const currentYear = new Date().getFullYear();
    document.querySelectorAll('.current-year').forEach(el => {
        el.textContent = currentYear;
    });

    /* ===== Donors Marquee Animation ===== */
    const donorsTrack = document.querySelector('.donors-track');
    if (donorsTrack) {
        let scrollPosition = 0;
        const scrollSpeed = 0.5;
        
        function animateMarquee() {
            scrollPosition -= scrollSpeed;
            donorsTrack.style.transform = `translateX(${scrollPosition}px)`;
            
            // Reset position when scrolled completely
            if (Math.abs(scrollPosition) >= donorsTrack.scrollWidth / 2) {
                scrollPosition = 0;
            }
            
            requestAnimationFrame(animateMarquee);
        }
        
        animateMarquee();
    }

    console.log('Donate Page JS Loaded Successfully ✅');
});

/* ===== Service Worker Registration ===== */
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Uncomment and update path if you have service worker
        // navigator.serviceWorker.register('/service-worker.js');
    });
}