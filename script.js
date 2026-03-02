document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Trigger when 15% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add the visible class when it enters the viewport
                entry.target.classList.add('is-visible');

                // Optional: Stop observing once animated if we only want it to happen once
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select all elements with the fade-up or fade-in classes
    const animatedElements = document.querySelectorAll('.fade-up, .fade-in');

    // Add them to the observer
    animatedElements.forEach(el => observer.observe(el));

    /* =========================================
       History Section Scroll-Triggered Image Swap
       ========================================= */
    const historyBlocks = document.querySelectorAll('.history-block');
    const stickyImage = document.getElementById('history-sticky-img');

    // Define the images corresponding to each block ID
    const historyImages = {
        'history-1': './assets/scroll1.jpg',
        'history-2': './assets/scroll2.jpg',
        'history-3': './assets/scroll3.jpg'
    };

    if (historyBlocks.length > 0 && stickyImage) {
        // Observer for the scroll spy
        const scrollSpyOptions = {
            root: null,
            // Offset logic: triggers when element reaches about middle of screen
            rootMargin: '-40% 0px -40% 0px',
            threshold: 0
        };

        const scrollSpyObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    const newSrc = historyImages[id];

                    // Only swap if the source actually changes to prevent unnecessary re-renders
                    if (newSrc && stickyImage.src !== newSrc) {
                        // Create a cross-fade effect
                        stickyImage.style.opacity = '0';

                        setTimeout(() => {
                            stickyImage.src = newSrc;
                            // Wait for image to load before fading back in
                            stickyImage.onload = () => {
                                stickyImage.style.opacity = '1';
                            };
                        }, 300); // Wait for fade out transition (sync with CSS)
                    }
                }
            });
        }, scrollSpyOptions);

        historyBlocks.forEach(block => scrollSpyObserver.observe(block));
    }

    /* =========================================
       Multi-Step Form Logic
       ========================================= */
    const multiStepForm = document.getElementById('multi-step-form');
    if (multiStepForm) {
        const steps = Array.from(multiStepForm.querySelectorAll('.form-step'));
        const nextBtns = multiStepForm.querySelectorAll('.btn-next');
        const prevBtns = multiStepForm.querySelectorAll('.btn-prev');
        const currentStepEl = document.getElementById('current-step');
        const progressFill = document.getElementById('progress-fill');

        let currentStepNum = 1;

        function updateFormSteps() {
            // Update active step class
            steps.forEach(step => {
                if (parseInt(step.dataset.step) === currentStepNum) {
                    step.classList.add('form-step-active');
                } else {
                    step.classList.remove('form-step-active');
                }
            });

            // Update Progress texts & bar
            currentStepEl.textContent = currentStepNum;
            const progressPercentage = ((currentStepNum) / steps.length) * 100;
            progressFill.style.width = `${progressPercentage}%`;
        }

        // Next Button Logic
        nextBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Basic validation: Check if required fields in current step are filled
                const currentStepElement = multiStepForm.querySelector(`.form-step[data-step="${currentStepNum}"]`);
                const inputs = currentStepElement.querySelectorAll('input[required], select[required]');

                let allValid = true;
                inputs.forEach(input => {
                    if (!input.checkValidity()) {
                        input.reportValidity(); // Shows native tooltip
                        allValid = false;
                    }
                });

                if (allValid && currentStepNum < steps.length) {
                    currentStepNum++;
                    updateFormSteps();
                }
            });
        });

        // Prev Button Logic
        prevBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                if (currentStepNum > 1) {
                    currentStepNum--;
                    updateFormSteps();
                }
            });
        });

        // Prevent Enter from submitting early and causing hidden validation errors
        multiStepForm.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                const currentStepElement = multiStepForm.querySelector(`.form-step[data-step="${currentStepNum}"]`);
                const nextBtn = currentStepElement.querySelector('.btn-next');
                if (nextBtn) {
                    nextBtn.click();
                } else if (currentStepNum === steps.length) {
                    const submitBtn = currentStepElement.querySelector('[type="submit"]');
                    if (submitBtn) {
                        submitBtn.click();
                    }
                }
            }
        });

        // Prevent Default Submit for demo
        multiStepForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Just simulate success here
            const formCardRight = multiStepForm.parentElement;
            formCardRight.innerHTML = `
                <div style="text-align: center; padding: 2rem; animation: fadeIn 0.5s ease;">
                    <div style="width: 60px; height: 60px; background-color: var(--clr-brand-orange-main); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto;">
                        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    </div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; color: #111; margin-bottom: 0.5rem;">Merci beaucoup !</h3>
                    <p style="color: var(--clr-text-mid); line-height: 1.5;">Votre demande a été envoyée avec succès.<br>Notre équipe vous recontactera sous peu.</p>
                </div>
            `;
        });
    }
});
