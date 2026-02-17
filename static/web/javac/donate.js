// donate.js (FULL REPLACE)
// - Submit works (POST goes to Django)
// - Payment modal closes safely
// - Success modal auto-opens after redirect (?success=1&amount=...&txn=...)
// - Scroll/backdrop hard fix

document.addEventListener("DOMContentLoaded", () => {

  /* =======================
     AOS INIT
  ======================= */
  if (window.AOS) AOS.init({ duration: 800, once: true });

  /* =======================
     COUNTER ANIMATION
  ======================= */
  const counters = document.querySelectorAll(".counter");
  if (counters.length) {
    const counterObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = Number(el.dataset.target || 0);
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
     HELPERS
  ======================= */
  const paymentModalEl = document.getElementById("paymentModal");
  const causeSelect = document.getElementById("causeSelect");
  const modalCauseName = document.getElementById("modalCauseName");

  const amountInput = document.getElementById("amountInput");
  const cardInput = document.getElementById("cardNumber");
  const expiryInput = document.getElementById("expiryDate");
  const cvvInput = document.getElementById("cvv");

  // ✅ find the payment form safely (id बदलला तरी चालेल)
  const paymentForm =
    document.getElementById("donationForm") ||
    document.getElementById("contactForm") ||
    document.getElementById("successAlert") ||
    document.querySelector('form[action*="donation_s"]') ||
    document.querySelector('form[action*="message_donate"]') ||
    null;

  const getModalInstance = () => {
    if (!paymentModalEl || !window.bootstrap) return null;
    return bootstrap.Modal.getInstance(paymentModalEl) || new bootstrap.Modal(paymentModalEl);
  };

  const setAmount = (v) => {
    const amt = Number(v) || 0;
    if (amountInput) amountInput.value = amt ? amt : "";
  };

  /* =======================
     OPEN PAYMENT MODAL FROM CARDS
  ======================= */
  document.querySelectorAll(".btn-donate-card").forEach(btn => {
    btn.addEventListener("click", () => {
      const cause = btn.dataset.cause || "";
      const amt = btn.dataset.amount || "";

      if (modalCauseName) modalCauseName.innerText = cause;
      if (causeSelect) causeSelect.value = cause;

      setAmount(amt);

      // highlight active amount btn
      document.querySelectorAll(".amount-btn").forEach(b => {
        b.classList.toggle("active", b.dataset.amount === String(amt));
      });
    });
  });

  // amount buttons inside modal
  document.querySelectorAll(".amount-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".amount-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      setAmount(btn.dataset.amount);
    });
  });

  /* =======================
     LIVE INPUT VALIDATION (nice UX)
  ======================= */
  if (cardInput) {
    cardInput.type = "text";
    cardInput.maxLength = 14;
    cardInput.inputMode = "numeric";
    cardInput.addEventListener("input", () => {
      cardInput.value = cardInput.value.replace(/\D/g, "").slice(0, 14);
    });
  }

  if (expiryInput) {
    expiryInput.type = "text";
    expiryInput.maxLength = 5;
    expiryInput.inputMode = "numeric";
    expiryInput.addEventListener("input", () => {
      let v = expiryInput.value.replace(/\D/g, "").slice(0, 4);
      if (v.length >= 3) v = v.slice(0, 2) + "/" + v.slice(2);
      expiryInput.value = v.slice(0, 5);
    });
  }

  if (cvvInput) {
    cvvInput.type = "password";
    cvvInput.maxLength = 4;
    cvvInput.inputMode = "numeric";
    cvvInput.addEventListener("input", () => {
      cvvInput.value = cvvInput.value.replace(/\D/g, "").slice(0, 4);
    });
  }

  /* =======================
     SUBMIT
     ✅ Invalid -> preventDefault
     ✅ Valid -> DO NOT preventDefault (POST goes)
  ======================= */
  if (paymentForm) {
    paymentForm.addEventListener("submit", (e) => {
      const cause = (causeSelect?.value || "").trim();
      const card = (cardInput?.value || "").replace(/\D/g, "");
      const expiry = (expiryInput?.value || "").trim();
      const cvv = (cvvInput?.value || "").replace(/\D/g, "");
      const amt = (amountInput?.value || "").trim();

      // cause
      if (!cause) {
        alert("Please select a cause.");
        e.preventDefault();
        return;
      }

      // card 14 digits
      if (!/^\d{14}$/.test(card)) {
        alert("Card number must be exactly 14 digits.");
        e.preventDefault();
        return;
      }

      // expiry MM/YY
      if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(expiry)) {
        alert("Expiry must be MM/YY (e.g. 06/28).");
        e.preventDefault();
        return;
      }

      // cvv 3/4
      if (!/^\d{3,4}$/.test(cvv)) {
        alert("CVV must be 3 or 4 digits.");
        e.preventDefault();
        return;
      }

      // amount
      if (!amt || Number(amt) <= 0) {
        alert("Enter a valid amount.");
        e.preventDefault();
        return;
      }

      // ✅ VALID:
      // payment modal close (optional)
      const modal = getModalInstance();
      if (modal) modal.hide();

      // safety unlock
      unlockScrollHard();

      // ✅ DO NOT preventDefault => form POST goes to Django
    });
  }

  /* =======================
     VIDEO MODAL (जर असेल)
  ======================= */
  const videoModal = document.getElementById("videoModal");
  const videoFrame = document.getElementById("videoFrame");

  if (videoModal && videoFrame && window.bootstrap) {
    document.querySelectorAll(".video-thumbnail").forEach(v => {
      v.addEventListener("click", () => {
        videoFrame.src = (v.dataset.video || "") + "?autoplay=1&mute=1&rel=0";
        new bootstrap.Modal(videoModal).show();
      });
    });

    videoModal.addEventListener("hidden.bs.modal", () => {
      videoFrame.src = "";
    });
  }
});

/* =======================
   SUCCESS MODAL AFTER REDIRECT
   ?success=1&amount=...&txn=...
======================= */
(function () {
  const params = new URLSearchParams(window.location.search);

  if (params.get("success") === "1") {
    const amt = params.get("amount") || "";
    const txn = params.get("txn") || "";

    const successAmount = document.getElementById("successAmount");   // <strong id="successAmount">
    const transactionId = document.getElementById("transactionId");   // <strong id="transactionId">
    const successModalEl = document.getElementById("successModal");   // modal id

    // ✅ तुमचं HTML: successAmount मध्ये ₹ आधीच आहे, पण safe ठेवतो
    if (successAmount) {
      // HTML मध्ये "₹" बाहेर असू शकतो किंवा आत; त्यामुळे content set करताना फक्त amount टाकतो
      // जर तुझ्या HTML मध्ये <strong id="successAmount">₹1,000</strong> असेल तर हे replace होईल.
      successAmount.innerText = "₹" + amt;
    }

    if (transactionId) transactionId.innerText = txn;

    if (successModalEl && window.bootstrap) {
      new bootstrap.Modal(successModalEl).show();
    }

    // ✅ URL clean (refresh ला परत modal नको)
    params.delete("success");
    params.delete("amount");
    params.delete("txn");
    const newUrl = window.location.pathname + (params.toString() ? "?" + params.toString() : "");
    window.history.replaceState({}, "", newUrl);
  }
})();

/* =======================
   SCROLL UNLOCK FIX (hard)
======================= */
function unlockScrollHard() {
  document.body.classList.remove("modal-open");
  document.body.style.overflow = "";
  document.body.style.paddingRight = "";

  // backdrop काढ
  document.querySelectorAll(".modal-backdrop").forEach(b => b.remove());

  // ✅ IMPORTANT: successModal ला touch करू नको
  document.querySelectorAll(".modal.show").forEach(m => {
    if (m.id === "successModal") return; // 👈 THIS LINE

    m.classList.remove("show");
    m.setAttribute("aria-hidden", "true");
    m.style.display = "none";
  });

  document.documentElement.style.overflow = "";
}

