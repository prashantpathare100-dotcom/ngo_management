document.addEventListener("DOMContentLoaded", () => {

  /* AOS */
  AOS.init({ duration: 800, once: true });

  /* Counter */
  const counters = document.querySelectorAll(".counter");
  const counterObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target, target = +el.dataset.target;
      let i = 0, step = target / 100;
      const run = () => {
        i += step;
        el.innerText = Math.min(target, Math.floor(i));
        if (i < target) requestAnimationFrame(run);
      };
      run(); counterObs.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(c => counterObs.observe(c));

  /* Donate Modal */
  let amount = 1000;
  const amtTxt = donateAmountBtn;
  document.querySelectorAll(".btn-donate-card").forEach(b => {
    b.onclick = () => {
      modalCauseName.innerText = b.dataset.cause;
      amount = +b.dataset.amount;
      amtTxt.innerText = amount;
    };
  });

  document.querySelectorAll(".amount-btn").forEach(b => {
    b.onclick = () => {
      document.querySelectorAll(".amount-btn").forEach(x => x.classList.remove("active"));
      b.classList.add("active");
      amount = +b.dataset.amount;
      amtTxt.innerText = amount;
    };
  });

  customDonationAmount?.addEventListener("input", e => {
    amount = +e.target.value || 0;
    amtTxt.innerText = amount;
  });

  /* Payment Submit (Demo) */
  onlinePaymentForm?.addEventListener("submit", e => {
    e.preventDefault();
    paymentModal.classList.remove("show");
    successAmount.innerText = "₹" + amount;
    transactionId.innerText = "TXN" + Date.now();
    new bootstrap.Modal(successModal).show();
    e.target.reset();
  });

  /* Copy Button */
  document.querySelectorAll(".copy-btn").forEach(b => {
    b.onclick = () => {
      navigator.clipboard.writeText(b.dataset.copy);
      b.innerText = "Copied!";
      setTimeout(() => b.innerHTML = '<i class="bi bi-clipboard"></i>', 1500);
    };
  });

  /* Video Modal */
  document.querySelectorAll(".video-thumbnail").forEach(v => {
    v.onclick = () => {
      videoFrame.src = v.dataset.video + "?autoplay=1";
      new bootstrap.Modal(videoModal).show();
    };
  });
  videoModal?.addEventListener("hidden.bs.modal", () => videoFrame.src = "");

  /* Progress Bars */
  document.querySelectorAll(".progress-bar").forEach(bar => {
    bar.style.width = "0";
    setTimeout(() => bar.style.width = bar.dataset.width || "70%", 300);
  });

  /* Contact + Newsletter */
  contactForm?.addEventListener("submit", e => {
    e.preventDefault(); alert("Message sent!");
    e.target.reset();
  });

  newsletterForm?.addEventListener("submit", e => {
    e.preventDefault(); alert("Subscribed!");
    e.target.reset();
  });

  console.log("Donate Page Ready ✔");
});