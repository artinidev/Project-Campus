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
        'history-1': './assets/scroll-actual-1.jpg',
        'history-2': './assets/scroll-actual-2.jpg',
        'history-3': './assets/scroll-actual-3.jpg'
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

    /* =========================================
       Custom Select Dropdown Logic
       ========================================= */
    const customSelects = document.querySelectorAll('.campus-form-card select');

    customSelects.forEach(selectElement => {
        // Hide the original select
        selectElement.style.display = 'none';

        // Create custom wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'custom-select-wrapper';

        // Insert wrapper right after the select element in the DOM
        selectElement.parentNode.insertBefore(wrapper, selectElement.nextSibling);

        // Move the hidden select inside the wrapper
        wrapper.appendChild(selectElement);

        // Create trigger button (the part you click to open)
        const trigger = document.createElement('div');
        trigger.className = 'custom-select-trigger';

        // Find the selected option to display initially
        const selectedOption = selectElement.options[selectElement.selectedIndex];
        trigger.innerHTML = `<span>${selectedOption.text}</span><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>`;
        wrapper.appendChild(trigger);

        // Create the dropdown menu container
        const optionsContainer = document.createElement('div');
        optionsContainer.className = 'custom-select-options';

        // Generate options from the native select
        Array.from(selectElement.children).forEach(child => {
            if (child.tagName === 'OPTGROUP') {
                // Handle OptGroups
                const optGroupLabel = document.createElement('div');
                optGroupLabel.className = 'custom-optgroup-label';
                optGroupLabel.textContent = child.label;
                optionsContainer.appendChild(optGroupLabel);

                // Add the options within the optgroup
                Array.from(child.children).forEach(option => {
                    createCustomOption(option, optionsContainer, selectElement, trigger);
                });
            } else if (child.tagName === 'OPTION') {
                // Handle direct Options (ignore the disabled generic placeholder for the dropdown list, but keep it for logic if needed)
                if (!child.disabled) {
                    createCustomOption(child, optionsContainer, selectElement, trigger);
                }
            }
        });

        wrapper.appendChild(optionsContainer);

        // Trigger Click Event (Toggle Open/Close)
        trigger.addEventListener('click', function (e) {
            e.stopPropagation();

            // Close any other open dropdowns first
            document.querySelectorAll('.custom-select-wrapper.open').forEach(openWrapper => {
                if (openWrapper !== wrapper) {
                    openWrapper.classList.remove('open');
                }
            });

            wrapper.classList.toggle('open');

            // Re-evaluate required validation state to clear native error if any (handled later on submit, but good for UX)
        });
    });

    // Helper function to create individual options
    function createCustomOption(optionElement, container, nativeSelect, trigger) {
        const customOption = document.createElement('div');
        customOption.className = 'custom-option';
        customOption.dataset.value = optionElement.value;
        customOption.textContent = optionElement.text;

        // Add checkmark icon (initially hidden)
        const checkIcon = document.createElement('span');
        checkIcon.className = 'custom-option-check';
        checkIcon.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
        customOption.prepend(checkIcon);

        customOption.addEventListener('click', function (e) {
            e.stopPropagation();

            // Update native select value
            nativeSelect.value = this.dataset.value;

            // Trigger change event on native select so validation/other scripts catch it
            nativeSelect.dispatchEvent(new Event('change'));

            // Update trigger text
            trigger.querySelector('span').textContent = this.textContent;

            // Remove selected class from all siblings
            const siblings = container.querySelectorAll('.custom-option');
            siblings.forEach(sib => sib.classList.remove('selected'));

            // Add selected class to this one
            this.classList.add('selected');

            // Close dropdown
            trigger.parentElement.classList.remove('open');

            // Remove 'unselected' styling if present (custom logic to make it look active)
            trigger.classList.add('has-value');
        });

        container.appendChild(customOption);
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', function () {
        document.querySelectorAll('.custom-select-wrapper.open').forEach(wrapper => {
            wrapper.classList.remove('open');
        });
    });

    /* =========================================
       FAQ Accordion Logic
       ========================================= */
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const currentItem = question.closest('.faq-item');
            const isActive = currentItem.classList.contains('active');

            // Close all other FAQ items for a cleaner accordion effect (optional, but good UX)
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });

            // If it wasn't active before, open it now
            if (!isActive) {
                currentItem.classList.add('active');
            }
        });
    });

    /* =========================================
       Fast Beautiful Smooth Scrolling
       ========================================= */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();

                // Calculate distances
                const headerOffset = document.querySelector('.hero-nav') ? document.querySelector('.hero-nav').offsetHeight : 0;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - headerOffset;
                const startPosition = window.scrollY;
                const distance = targetPosition - startPosition;
                const duration = 600; // 600ms makes it fast but gives it enough time to feel smooth
                let start = null;

                // Easing function for a beautiful smooth stop (easeOutQuart)
                const easeOutQuart = time => 1 - Math.pow(1 - time, 4);

                function step(timestamp) {
                    if (!start) start = timestamp;
                    const progress = timestamp - start;
                    const percentage = Math.min(progress / duration, 1);

                    window.scrollTo(0, startPosition + distance * easeOutQuart(percentage));

                    if (progress < duration) {
                        window.requestAnimationFrame(step);
                    } else {
                        // Ensure we absolutely hit the target at the end, and update URL
                        window.scrollTo(0, targetPosition);
                        // Optional: Update history without jumping
                        // history.pushState(null, null, targetId);
                    }
                }

                window.requestAnimationFrame(step);
            }
        });
    });
});
