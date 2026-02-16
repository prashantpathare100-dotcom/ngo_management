document.addEventListener("DOMContentLoaded", () => {

  /* =======================
     AOS INIT
  ======================= */
  if (window.AOS) {
    AOS.init({ duration: 800, once: true });
  }

  /* =======================
     COUNTER ANIMATION
  ======================= */
  const counters = document.querySelectorAll(".counter");

  if (counters.length) {
    const counterObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = +el.dataset.target;
        let count = 0;
        const step = target / 100;

        const run = () => {
          count += step;
          el.innerText = Math.min(target, Math.floor(count));
          if (count < target) requestAnimationFrame(run);
        };
        run();
        counterObs.unobserve(el);
      });
    }, { threshold: 0.5 });

    counters.forEach(c => counterObs.observe(c));
  }

  /* =======================
     DONATION MODAL LOGIC
  ======================= */
  let amount = 1000;

  const donateAmountBtn = document.getElementById("donateAmountBtn");
  const modalCauseName = document.getElementById("modalCauseName");
  const paymentModalEl = document.getElementById("paymentModal");
  const successModalEl = document.getElementById("successModal");
  const successAmount = document.getElementById("successAmount");
  const transactionId = document.getElementById("transactionId");

  // Donate buttons on cards
  document.querySelectorAll(".btn-donate-card").forEach(btn => {
    btn.addEventListener("click", () => {
      modalCauseName.innerText = btn.dataset.cause;
      amount = Number(btn.dataset.amount) || 0;
      donateAmountBtn.innerText = amount.toLocaleString("en-IN");
    });
  });

  // Amount buttons inside modal
  document.querySelectorAll(".amount-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".amount-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      amount = Number(btn.dataset.amount);
      donateAmountBtn.innerText = amount.toLocaleString("en-IN");
    });
  });

  /* =======================
     PAYMENT SUBMIT → SUCCESS MODAL
  ======================= */
  const paymentForm = document.getElementById("successAlert");

  if (paymentForm) {
    paymentForm.addEventListener("submit", e => {
      e.preventDefault();

      const paymentModal =
        bootstrap.Modal.getInstance(paymentModalEl) ||
        new bootstrap.Modal(paymentModalEl);

      // Close payment modal properly
      paymentModal.hide();

      // After it fully closes → open success modal
      paymentModalEl.addEventListener("hidden.bs.modal", () => {
        successAmount.innerText = "₹" + amount.toLocaleString("en-IN");
        transactionId.innerText = "TXN" + Date.now();

        new bootstrap.Modal(successModalEl).show();
        paymentForm.reset();
      }, { once: true });
    });
  }

  /* =======================
     COPY BUTTONS
  ======================= */
  document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      navigator.clipboard.writeText(btn.dataset.copy);
      const old = btn.innerHTML;
      btn.innerText = "Copied!";
      setTimeout(() => (btn.innerHTML = old), 1500);
    });
  });

  /* =======================
     VIDEO MODAL
  ======================= */
  const videoModal = document.getElementById("videoModal");
  const videoFrame = document.getElementById("videoFrame");

  document.querySelectorAll(".video-thumbnail").forEach(v => {
    v.addEventListener("click", () => {
      videoFrame.src = v.dataset.video + "?autoplay=1&mute=1&rel=0";
      new bootstrap.Modal(videoModal).show();
    });
  });

  videoModal.addEventListener("hidden.bs.modal", () => {
    videoFrame.src = "";
  });

  /* =======================
     CLEAN LEFTOVER BACKDROPS (safety)
  ======================= */
  document.addEventListener("hidden.bs.modal", () => {
    document.querySelectorAll(".modal-backdrop").forEach(b => b.remove());
    document.body.classList.remove("modal-open");
  });

});
document.addEventListener("DOMContentLoaded", () => {

  /* =======================
     AOS INIT
  ======================= */
  if (window.AOS) {
    AOS.init({ duration: 800, once: true });
  }

  /* =======================
     COUNTER ANIMATION
  ======================= */
  const counters = document.querySelectorAll(".counter");

  if (counters.length) {
    const counterObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = +el.dataset.target;
        let count = 0;
        const step = target / 100;

        const run = () => {
          count += step;
          el.innerText = Math.min(target, Math.floor(count));
          if (count < target) requestAnimationFrame(run);
        };
        run();
        counterObs.unobserve(el);
      });
    }, { threshold: 0.5 });

    counters.forEach(c => counterObs.observe(c));
  }

  /* =======================
     DONATION MODAL LOGIC
  ======================= */
  let amount = 1000;

  const donateAmountBtn = document.getElementById("donateAmountBtn");
  const modalCauseName = document.getElementById("modalCauseName");
  const paymentModalEl = document.getElementById("paymentModal");
  const successModalEl = document.getElementById("successModal");
  const successAmount = document.getElementById("successAmount");
  const transactionId = document.getElementById("transactionId");

  // Donate buttons on cards
  document.querySelectorAll(".btn-donate-card").forEach(btn => {
    btn.addEventListener("click", () => {
      modalCauseName.innerText = btn.dataset.cause;
      amount = Number(btn.dataset.amount) || 0;
      donateAmountBtn.innerText = amount.toLocaleString("en-IN");
    });
  });

  // Amount buttons inside modal
  document.querySelectorAll(".amount-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".amount-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      amount = Number(btn.dataset.amount);
      donateAmountBtn.innerText = amount.toLocaleString("en-IN");
    });
  });

  /* =======================
     PAYMENT SUBMIT → SUCCESS MODAL
  ======================= */
  const paymentForm = document.getElementById("successAlert");

  if (paymentForm) {
    paymentForm.addEventListener("submit", e => {
      e.preventDefault();

      const paymentModal =
        bootstrap.Modal.getInstance(paymentModalEl) ||
        new bootstrap.Modal(paymentModalEl);

      // Close payment modal properly
      paymentModal.hide();

      // After it fully closes → open success modal
      paymentModalEl.addEventListener("hidden.bs.modal", () => {
        successAmount.innerText = "₹" + amount.toLocaleString("en-IN");
        transactionId.innerText = "TXN" + Date.now();

        new bootstrap.Modal(successModalEl).show();
        paymentForm.reset();
      }, { once: true });
    });
  }

  /* =======================
     COPY BUTTONS
  ======================= */
  document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      navigator.clipboard.writeText(btn.dataset.copy);
      const old = btn.innerHTML;
      btn.innerText = "Copied!";
      setTimeout(() => (btn.innerHTML = old), 1500);
    });
  });

  /* =======================
     VIDEO MODAL
  ======================= */
  const videoModal = document.getElementById("videoModal");
  const videoFrame = document.getElementById("videoFrame");

  document.querySelectorAll(".video-thumbnail").forEach(v => {
    v.addEventListener("click", () => {
      videoFrame.src = v.dataset.video + "?autoplay=1&mute=1&rel=0";
      new bootstrap.Modal(videoModal).show();
    });
  });

  videoModal.addEventListener("hidden.bs.modal", () => {
    videoFrame.src = "";
  });

  /* =======================
     CLEAN LEFTOVER BACKDROPS (safety)
  ======================= */
  document.addEventListener("hidden.bs.modal", () => {
    document.querySelectorAll(".modal-backdrop").forEach(b => b.remove());
    document.body.classList.remove("modal-open");
  });

});