
document.addEventListener('DOMContentLoaded', function () {

  // ====== Event Modal Data ======
  const eventData = {
    'medical-camp': {
      title: 'Free Medical Camp',
      category: 'Health',
      date: 'November 25, 2026',
      time: '9:00 AM - 4:00 PM',
      location: 'Central Park, Downtown',
      capacity: '200 participants',
      image: 'https://images.unsplash.com/photo-1516549655669-df6654e435de?auto=format&fit=crop&w=800&q=80',
      description:
        'Join us for a day of free medical services including health checkups, consultations, and basic screenings. Our team of volunteer doctors and nurses will provide essential healthcare services to underserved communities.',
      expectations: [
        'Free health checkups and consultations',
        'Blood pressure and sugar level tests',
        'Basic medical screenings',
        'Health education sessions',
        'Free medication for common ailments',
      ],
      audience:
        'This event is open to all community members, with priority given to low-income families and individuals without access to regular healthcare.',
      note: 'Please bring any existing medical records. No registration fee required.',
    },

    'digital-workshop': {
      title: 'Digital Literacy Workshop',
      category: 'Education',
      date: 'December 02, 2026',
      time: '10:00 AM - 2:00 PM',
      location: 'Community Center',
      capacity: '50 participants',
      image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=800&q=80',
      description:
        'Learn essential digital skills in this hands-on workshop designed for beginners. Perfect for seniors and underprivileged youth.',
      expectations: [
        'Basic computer operation',
        'Internet browsing and safety',
        'Email communication',
        'MS Office basics',
        'Smartphone usage tips',
      ],
      audience:
        'Open to all ages, especially recommended for seniors and individuals with limited digital experience.',
      note: 'Computers will be provided. Bring your own device if preferred.',
    },

    'cleanup-drive': {
      title: 'City Cleanup Drive',
      category: 'Environment',
      date: 'December 10, 2026',
      time: '8:00 AM - 12:00 PM',
      location: 'Riverside Park',
      capacity: '100 volunteers',
      image: 'https://images.unsplash.com/photo-1520975958225-65f2b23f79a3?auto=format&fit=crop&w=800&q=80',
      description:
        'Join our community cleanup initiative to make our city cleaner and greener. Together we can make a difference!',
      expectations: [
        'Park and riverbank cleanup',
        'Waste segregation training',
        'Recycling education',
        'Team coordination',
        'Refreshments provided',
      ],
      audience:
        'All ages welcome. Families encouraged. Children under 16 must be accompanied by an adult.',
      note: 'Gloves and cleanup equipment will be provided. Wear comfortable clothes and closed shoes.',
    },

    'winter-relief': {
      title: 'Winter Relief Distribution',
      category: 'Relief',
      date: 'December 15, 2026',
      time: '11:00 AM - 3:00 PM',
      location: 'Downtown Shelter',
      capacity: '75 volunteers',
      image: 'https://images.unsplash.com/photo-1541976844346-f18aeac57b06?auto=format&fit=crop&w=800&q=80',
      description:
        'Help us distribute winter essentials to homeless and low-income families during the cold season.',
      expectations: [
        'Sorting and organizing donations',
        'Distribution of winter clothes',
        'Blankets & sleeping bags',
        'Hot meal service support',
        'Community engagement',
      ],
      audience:
        'Volunteers of all ages. Physical ability to lift and distribute items is helpful.',
      note: 'We welcome donations of winter clothing, blankets, and non-perishable food items.',
    },

    'stem-workshop': {
      title: 'STEM Workshop for Girls',
      category: 'Education',
      date: 'December 18, 2026',
      time: '1:00 PM - 5:00 PM',
      location: 'Innovation Hub',
      capacity: '60 participants',
      image: 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=800&q=80',
      description:
        'A fun STEM workshop to encourage young girls to explore science, coding, and creative problem solving.',
      expectations: [
        'Hands-on science experiments',
        'Basic coding activities',
        'Team challenges',
        'Mentor guidance',
        'Certificates',
      ],
      audience:
        'Girls aged 10–18 and guardians. Limited seats available.',
      note: 'Bring notebook and water bottle.',
    },

    'mental-health': {
      title: 'Mental Health Awareness Seminar',
      category: 'Health',
      date: 'December 22, 2026',
      time: '6:00 PM - 8:00 PM',
      location: 'Convention Center',
      capacity: '150 participants',
      image: 'https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=800&q=80',
      description:
        'An awareness seminar promoting mental wellbeing, coping strategies and access to community support.',
      expectations: [
        'Expert talks',
        'Q&A session',
        'Self-care toolkit',
        'Community support resources',
        'Networking',
      ],
      audience:
        'Open to all community members, students and working professionals.',
      note: 'Please arrive 15 minutes early for registration.',
    },
  };

  // ====== Modal Setup ======
  const eventModal = document.getElementById('eventModal');
  if (eventModal) {
    eventModal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      const eventId = button?.getAttribute('data-event');
      const info = eventData[eventId] || eventData['medical-camp'];

      document.getElementById('eventModalLabel').textContent = info.title;
      document.getElementById('modalEventTitle').textContent = info.title;
      document.getElementById('modalCategory').textContent = info.category;
      document.getElementById('modalDate').textContent = info.date;
      document.getElementById('modalTime').textContent = info.time;
      document.getElementById('modalLocation').textContent = info.location;
      document.getElementById('modalCapacity').textContent = info.capacity;
      document.getElementById('modalDescription').textContent = info.description;
      document.getElementById('modalNote').textContent = info.note;
      document.getElementById('modalAudience').textContent = info.audience;

      const img = document.getElementById('modalImage');
      if (img) img.src = info.image;

      const list = document.getElementById('modalExpectations');
      list.innerHTML = '';
      info.expectations.forEach((x) => {
        const li = document.createElement('li');
        li.textContent = x;
        list.appendChild(li);
      });
    });
  }

  // Register button
  const registerModalBtn = document.getElementById('registerModalBtn');
  if (registerModalBtn) {
    registerModalBtn.addEventListener('click', function () {
      const title = document.getElementById('modalEventTitle').textContent;
      alert(`Thank you for your interest in "${title}"! Our team will contact you with registration details shortly.`);
      const modal = bootstrap.Modal.getInstance(eventModal);
      modal?.hide();
    });
  }

  // ====== Auto Fill Category Tabs (So tabs empty नाही राहणार) ======
  const cards = Array.from(document.querySelectorAll('#all .event-card'));
  const targets = {
    health: document.getElementById('healthEvents'),
    education: document.getElementById('educationEvents'),
    relief: document.getElementById('reliefEvents'),
    environment: document.getElementById('environmentEvents'),
  };

  function cloneCardTo(category) {
    const wrap = targets[category];
    if (!wrap) return;

    const matched = cards.filter(c => c.getAttribute('data-category') === category);
    matched.forEach(card => {
      const col = card.closest('.col-md-6') || card.parentElement;
      const clonedCol = col.cloneNode(true);
      wrap.appendChild(clonedCol);
    });
  }

  ['health', 'education', 'relief', 'environment'].forEach(cloneCardTo);

  // ====== Scroll animation observer ======
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) e.target.classList.add('animate-on-scroll');
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.event-card, .process-step, .impact-stat, .gallery-item').forEach((el) => {
    observer.observe(el);
  });

  // ====== ✅ FIXED Counter Animation (Supports: 5,200+ | $85K | 1,250+ | 15K | 5.2K) ======
  function animateCounters() {
    const counters = document.querySelectorAll('.stat-number, .impact-number');

    counters.forEach((el) => {
      const original = el.textContent.trim();
      const hasPlus = original.includes('+');
      const hasDollar = original.includes('$');

      // clean (remove , + $)
      let cleaned = original.replace(/,/g, '').replace(/\+/g, '').replace(/\$/g, '').trim();

      // suffix
      let multiplier = 1;
      if (cleaned.toUpperCase().endsWith('K')) {
        multiplier = 1000;
        cleaned = cleaned.slice(0, -1);
      } else if (cleaned.toUpperCase().endsWith('M')) {
        multiplier = 1000000;
        cleaned = cleaned.slice(0, -1);
      }

      const target = parseFloat(cleaned);
      if (isNaN(target)) return;

      const finalValue = target * multiplier;

      const duration = 1200;
      const steps = 80;
      const stepTime = Math.max(10, Math.floor(duration / steps));
      const increment = finalValue / steps;

      let current = 0;

      const timer = setInterval(() => {
        current += increment;

        if (current >= finalValue) {
          clearInterval(timer);

          // ✅ End output: if original had K, keep K style for Funds like $85K
          if (multiplier === 1000 && target >= 10) {
            el.textContent = `${hasDollar ? '$' : ''}${target}${'K'}${hasPlus ? '+' : ''}`;
          } else {
            el.textContent = formatNumber(finalValue, { hasDollar, hasPlus, isRunning: false });
          }
        } else {
          el.textContent = formatNumber(current, { hasDollar, hasPlus, isRunning: true });
        }
      }, stepTime);
    });

    function formatNumber(value, opts) {
      const { hasDollar, hasPlus, isRunning } = opts;
      const num = Math.floor(value);
      const withCommas = num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      const plus = (!isRunning && hasPlus) ? '+' : '';
      return `${hasDollar ? '$' : ''}${withCommas}${plus}`;
    }
  }

  // Trigger counters when quick-stats OR impact-stats comes into view
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        animateCounters();
        statsObserver.disconnect();
      }
    });
  }, { threshold: 0.4 });

  document.querySelectorAll('.quick-stats, .impact-stats').forEach((sec) => {
    statsObserver.observe(sec);
  });

});