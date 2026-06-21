function animateCounter(el, target, suffix = '', duration = 2000) {
    const start = 0;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(eased * target);
        el.textContent = current.toLocaleString() + suffix;
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            el.textContent = target.toLocaleString() + suffix;
        }
    }
    requestAnimationFrame(update);
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize custom glassmorphic dropdowns
    initCustomDropdowns();

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
                const inputs = currentStepElement.querySelectorAll('input[required], select[required], textarea[required]');

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
       Custom Select Dropdown Logic & Dynamic Population
       ========================================= */
    const LANG = document.documentElement.lang === 'en' ? 'en' : 'fr';

    const TRANSLATIONS = {
        fr: {
            rentreeLabel: "Choisir votre rentrée <span class=\"text-brand-orange\">*</span>",
            rentreePlaceholder: "Sélectionnez votre rentrée",
            programmeLabel: "Choisir votre programme <span class=\"text-brand-orange\">*</span>",
            programmePlaceholder: "Sélectionnez un programme",
            rentrees: {
                septembre: "Rentrée de septembre",
                fevrier: "Rentrée de février",
                internationaux: "Candidats internationaux"
            },
            programmes: {
                septembre: [
                    { value: "bts", text: "Admission BTS" },
                    { value: "bachelor", text: "Admission Bachelor" },
                    { value: "bba", text: "Admission BBA" },
                    { value: "msc", text: "Admission MSc" }
                ],
                fevrier: [
                    { value: "bachelor", text: "Admission Bachelor" },
                    { value: "bba", text: "Admission BBA" },
                    { value: "msc", text: "Admission MSc" }
                ],
                internationaux: [
                    { value: "bachelor", text: "Admission Internationale Bachelor" },
                    { value: "bba", text: "Admission Internationale BBA" },
                    { value: "msc", text: "Admission Internationale MSc" }
                ]
            }
        },
        en: {
            rentreeLabel: "Choose your intake <span class=\"text-brand-orange\">*</span>",
            rentreePlaceholder: "Select your intake",
            programmeLabel: "Choose your program <span class=\"text-brand-orange\">*</span>",
            programmePlaceholder: "Select a program",
            rentrees: {
                septembre: "September Intake",
                fevrier: "February Intake",
                internationaux: "International Candidates"
            },
            programmes: {
                septembre: [
                    { value: "bts", text: "BTS Admission" },
                    { value: "bachelor", text: "Bachelor Admission" },
                    { value: "bba", text: "BBA Admission" },
                    { value: "msc", text: "MSc Admission" }
                ],
                fevrier: [
                    { value: "bachelor", text: "Bachelor Admission" },
                    { value: "bba", text: "BBA Admission" },
                    { value: "msc", text: "MSc Admission" }
                ],
                internationaux: [
                    { value: "bachelor", text: "International Admission Bachelor" },
                    { value: "bba", text: "International Admission BBA" },
                    { value: "msc", text: "International Admission MSc" }
                ]
            }
        }
    };

    function detectContext() {
        // 1. Check URL query parameters
        const urlParams = new URLSearchParams(window.location.search);
        let rentree = urlParams.get('rentree');
        let program = urlParams.get('program') || urlParams.get('objectif');

        // 2. Check current page pathname
        const path = window.location.pathname.toLowerCase();
        if (path.includes('admissions-bts')) {
            return { rentree: 'septembre', program: 'bts' };
        }
        if (path.includes('admissions-bachelor')) {
            return { rentree: rentree || 'septembre', program: 'bachelor' };
        }
        if (path.includes('admissions-bba')) {
            return { rentree: rentree || 'septembre', program: 'bba' };
        }
        if (path.includes('admissions-msc')) {
            return { rentree: rentree || 'septembre', program: 'msc' };
        }
        if (path.includes('admissions-international')) {
            return { rentree: 'internationaux', program: program || 'bachelor' };
        }

        // 3. Check document referrer
        try {
            if (document.referrer) {
                const ref = document.referrer.toLowerCase();
                const refUrl = new URL(document.referrer);
                const refParams = new URLSearchParams(refUrl.search);
                const refRentree = refParams.get('rentree');
                const refProgram = refParams.get('program') || refParams.get('objectif');

                if (ref.includes('admissions-bts')) {
                    return { rentree: 'septembre', program: 'bts' };
                }
                if (ref.includes('admissions-bachelor')) {
                    return { rentree: refRentree || 'septembre', program: 'bachelor' };
                }
                if (ref.includes('admissions-bba')) {
                    return { rentree: refRentree || 'septembre', program: 'bba' };
                }
                if (ref.includes('admissions-msc')) {
                    return { rentree: refRentree || 'septembre', program: 'msc' };
                }
                if (ref.includes('admissions-international')) {
                    return { rentree: 'internationaux', program: refProgram || 'bachelor' };
                }
            }
        } catch (e) {
            console.error("Error parsing referrer URL:", e);
        }

        // If rentree or program is set via URL params of current page, use it
        if (rentree || program) {
            const cleanRentree = rentree === 'fevrier' || rentree === 'internationaux' ? rentree : 'septembre';
            return { rentree: cleanRentree, program: program };
        }

        return null;
    }

    // Dynamic label and option population on native selects
    const rentreeSelect = document.querySelector('.campus-form-card select[id="niveau"]');
    const objectifSelect = document.querySelector('.campus-form-card select[id="objectif"]');

    const isLandingPage = window.location.pathname === '/' || window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('index-en.html') || window.location.pathname === '' || window.location.pathname.includes('partenariats');

    if (!isLandingPage) {
        if (rentreeSelect) {
            // Set label dynamically
            const labelNiveau = document.querySelector('label[for="niveau"]');
            if (labelNiveau) {
                labelNiveau.innerHTML = TRANSLATIONS[LANG].rentreeLabel;
            }

            // Re-populate Rentree dropdown options
            const placeholder = rentreeSelect.options[0];
            rentreeSelect.innerHTML = '';
            if (placeholder) {
                placeholder.textContent = TRANSLATIONS[LANG].rentreePlaceholder;
                rentreeSelect.appendChild(placeholder);
            }

            Object.entries(TRANSLATIONS[LANG].rentrees).forEach(([val, text]) => {
                const opt = document.createElement('option');
                opt.value = val;
                opt.textContent = text;
                rentreeSelect.appendChild(opt);
            });
        }

        if (objectifSelect) {
            // Set label dynamically
            const labelObjectif = document.querySelector('label[for="objectif"]');
            if (labelObjectif) {
                labelObjectif.innerHTML = TRANSLATIONS[LANG].programmeLabel;
            }

            // Prepare Programme dropdown with placeholder
            const placeholder = objectifSelect.options[0];
            objectifSelect.innerHTML = '';
            if (placeholder) {
                placeholder.textContent = TRANSLATIONS[LANG].programmePlaceholder;
                objectifSelect.appendChild(placeholder);
            }
        }

        // Auto-select program if context exists
        const context = detectContext();
        if (context && rentreeSelect && objectifSelect) {
            rentreeSelect.value = context.rentree;

            // Populate valid programs for this rentree
            const validPrograms = TRANSLATIONS[LANG].programmes[context.rentree] || [];
            validPrograms.forEach(prog => {
                const opt = document.createElement('option');
                opt.value = prog.value;
                opt.textContent = prog.text;
                if (prog.value === context.program) {
                    opt.selected = true;
                }
                objectifSelect.appendChild(opt);
            });
        }

        // Handle rentree selection change event
        if (rentreeSelect && objectifSelect) {
            rentreeSelect.addEventListener('change', function () {
                const rentreeVal = this.value;
                const currentProgramVal = objectifSelect.value;
                const validPrograms = TRANSLATIONS[LANG].programmes[rentreeVal] || [];
                const isStillValid = validPrograms.some(prog => prog.value === currentProgramVal);

                // Re-populate the native program select
                const placeholder = objectifSelect.options[0];
                objectifSelect.innerHTML = '';
                if (placeholder) {
                    placeholder.textContent = TRANSLATIONS[LANG].programmePlaceholder;
                    objectifSelect.appendChild(placeholder);
                }

                validPrograms.forEach(prog => {
                    const opt = document.createElement('option');
                    opt.value = prog.value;
                    opt.textContent = prog.text;
                    if (isStillValid && prog.value === currentProgramVal) {
                        opt.selected = true;
                    }
                    objectifSelect.appendChild(opt);
                });

                if (!isStillValid) {
                    objectifSelect.value = '';
                }

                // Sync custom select options
                refreshCustomSelect(objectifSelect);
            });
        }
    }

    function refreshCustomSelect(selectElement) {
        const wrapper = selectElement.closest('.custom-select-wrapper');
        if (!wrapper) return;

        const trigger = wrapper.querySelector('.custom-select-trigger');
        const optionsContainer = wrapper.querySelector('.custom-select-options');
        if (!trigger || !optionsContainer) return;

        optionsContainer.innerHTML = '';

        // Generate options from the native select
        Array.from(selectElement.children).forEach(child => {
            if (child.tagName === 'OPTGROUP') {
                const optGroupLabel = document.createElement('div');
                optGroupLabel.className = 'custom-optgroup-label';
                optGroupLabel.textContent = child.label;
                optionsContainer.appendChild(optGroupLabel);

                Array.from(child.children).forEach(option => {
                    createCustomOption(option, optionsContainer, selectElement, trigger);
                });
            } else if (child.tagName === 'OPTION') {
                if (!child.disabled) {
                    createCustomOption(child, optionsContainer, selectElement, trigger);
                }
            }
        });

        // Update trigger text
        const selectedOption = selectElement.options[selectElement.selectedIndex];
        if (selectedOption) {
            trigger.querySelector('span').textContent = selectedOption.text;
            if (selectedOption.value !== "") {
                trigger.classList.add('has-value');
            } else {
                trigger.classList.remove('has-value');
            }
        }
    }

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

        // Pre-select if selected in native select
        if (optionElement.selected) {
            customOption.classList.add('selected');
            trigger.classList.add('has-value');
        }

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

    /* =========================================
       Progressive Scroll Timeline Formations
       ========================================= */
    const timeline = document.querySelector('.story-timeline');
    const timelineFill = document.getElementById('timeline-fill');

    if (timeline && timelineFill) {
        const steps = timeline.querySelectorAll('.story-step');

        window.addEventListener('scroll', () => {
            // Get position of the timeline relative to viewport
            const rect = timeline.getBoundingClientRect();
            // Trigger point at exactly 50% of the viewport height (center of the screen)
            const triggerPoint = window.innerHeight * 0.5;

            let percentage = 0;

            if (rect.top <= triggerPoint) {
                // How far we scrolled past the trigger point
                const scrolledPast = triggerPoint - rect.top;
                // Full line length logic
                const totalScrollLength = rect.height - 100;

                percentage = (scrolledPast / totalScrollLength) * 100;

                // Determine step visibility strictly tied to the central line position
                steps.forEach(step => {
                    const stepRect = step.getBoundingClientRect();
                    // If the step's center crosses the trigger point + slight offset
                    if (stepRect.top + (stepRect.height / 2) - 40 <= triggerPoint) {
                        step.classList.add('active-step');
                    } else {
                        // Un-reveal if scrolling back up
                        step.classList.remove('active-step');
                    }
                });
            } else {
                steps.forEach(step => step.classList.remove('active-step'));
            }

            // Clamp percentage between 0 and 100
            percentage = Math.max(0, Math.min(percentage, 100));
            timelineFill.style.height = `${percentage}%`;
        });

        // Trigger once on load to establish initial state
        window.dispatchEvent(new Event('scroll'));
    }

    /* =========================================
       Sticky Header Background Toggle
       ========================================= */
    const siteHeader = document.querySelector('.site-header');
    if (siteHeader) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                siteHeader.classList.add('scrolled');
            } else {
                siteHeader.classList.remove('scrolled');
            }
        });
        // Check initial state
        if (window.scrollY > 50) {
            siteHeader.classList.add('scrolled');
        }
    }

    /* =========================================
       Animated Counter for Hero Gadgets
       ========================================= */
    const gadgetNumbers = document.querySelectorAll('.gadget-number');
    if (gadgetNumbers.length > 0) {
        let countersAnimated = false;
        const counterObserver = new IntersectionObserver((entries) => {
            if (!countersAnimated && entries.some(e => e.isIntersecting)) {
                countersAnimated = true;
                gadgetNumbers.forEach(el => {
                    const target = parseInt(el.dataset.target);
                    const suffix = el.parentElement.dataset.suffix || '';
                    animateCounter(el, target, suffix);
                });
                counterObserver.disconnect();
            }
        }, { threshold: 0.3 });
        counterObserver.observe(document.querySelector('.hero-gadgets'));
    }

    /* =========================================
       Generic Stats Counter Animation
       ========================================= */
    const animCounters = document.querySelectorAll('.stat-number-anim');
    if (animCounters.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseInt(el.dataset.target) || 0;
                    const suffix = el.dataset.suffix || '';
                    animateCounter(el, target, suffix);
                    statsObserver.unobserve(el);
                }
            });
        }, { threshold: 0.2 });
        animCounters.forEach(el => statsObserver.observe(el));
    }

    /* ==========================================================================
       Hero Search Gadget Redirection & Filtering Logic
       ========================================================================== */
    const searchGadgetBtn = document.getElementById('btn-search-gadget');
    if (searchGadgetBtn) {
        searchGadgetBtn.addEventListener('click', () => {
            const programSelect = document.getElementById('gadget-program');
            const specSelect = document.getElementById('gadget-specialization');
            const campusSelect = document.getElementById('gadget-campus');

            const programVal = programSelect ? programSelect.value : '';
            const specVal = specSelect ? specSelect.value : '';
            const campusVal = campusSelect ? campusSelect.value : '';

            // Check if we are on the programmes page
            const isProgrammesPage = window.location.pathname.includes('programmes');

            if (isProgrammesPage) {
                // Update URL search query parameters dynamically in-place
                const url = new URL(window.location);
                if (programVal) url.searchParams.set('level', programVal); else url.searchParams.delete('level');
                if (specVal) url.searchParams.set('specialization', specVal); else url.searchParams.delete('specialization');
                if (campusVal) url.searchParams.set('campus', campusVal); else url.searchParams.delete('campus');

                window.history.pushState({}, '', url);
                filterProgramsFromURL(true); // Smooth scroll to results
            } else {
                // Determine if we are on the English site or French site
                const isEnglish = window.location.pathname.includes('-en.html');
                const targetPage = isEnglish ? 'programmes-en.html' : 'programmes.html';

                // Construct query parameters
                const params = new URLSearchParams();
                if (programVal) params.set('level', programVal);
                if (specVal) params.set('specialization', specVal);
                if (campusVal) params.set('campus', campusVal);

                const queryString = params.toString();
                const redirectUrl = targetPage + (queryString ? '?' + queryString : '');

                window.location.href = redirectUrl;
            }
        });
    }

    /* ==========================================================================
       Programmes Page Card Filtering & status bar controls
       ========================================================================== */
    const programCards = document.querySelectorAll('.program-card-detail');
    const filterStatusBar = document.getElementById('filter-status-bar');
    const filterStatusTags = document.getElementById('filter-status-tags');
    const filterClearBtn = document.getElementById('filter-clear-btn');

    if (programCards.length > 0) {
        // Run filtering logic on page load with scrolling disabled initially
        filterProgramsFromURL(false);

        // Bind clear filters button
        if (filterClearBtn) {
            filterClearBtn.addEventListener('click', () => {
                // Clear URL parameters without page reload
                const url = new URL(window.location);
                url.search = '';
                window.history.pushState({}, '', url);

                // Re-evaluate filters (which will now show everything)
                filterProgramsFromURL(false);
            });
        }

        // Bind tab switching buttons
        const tabButtons = document.querySelectorAll('.program-families-tabs .tab-btn');
        tabButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const familyVal = btn.dataset.family;
                const url = new URL(window.location);
                if (familyVal && familyVal !== 'all') {
                    url.searchParams.set('family', familyVal);
                } else {
                    url.searchParams.delete('family');
                }
                window.history.pushState({}, '', url);
                filterProgramsFromURL(false);
            });
        });

        // Live filter automatically on dropdown change
        const levelSelect = document.getElementById('gadget-program');
        const specSelect = document.getElementById('gadget-specialization');
        const campusSelect = document.getElementById('gadget-campus');

        const triggerLiveFilter = () => {
            const url = new URL(window.location);
            const levelVal = levelSelect ? levelSelect.value : '';
            const specVal = specSelect ? specSelect.value : '';
            const campusVal = campusSelect ? campusSelect.value : '';

            if (levelVal) url.searchParams.set('level', levelVal); else url.searchParams.delete('level');
            if (specVal) url.searchParams.set('specialization', specVal); else url.searchParams.delete('specialization');
            if (campusVal) url.searchParams.set('campus', campusVal); else url.searchParams.delete('campus');

            window.history.pushState({}, '', url);
            filterProgramsFromURL(false); // No scroll jump when selecting
        };

        if (levelSelect) levelSelect.addEventListener('change', triggerLiveFilter);
        if (specSelect) specSelect.addEventListener('change', triggerLiveFilter);
        if (campusSelect) campusSelect.addEventListener('change', triggerLiveFilter);
    }

    function filterProgramsFromURL(smoothScroll = true) {
        const urlParams = new URLSearchParams(window.location.search);
        const level = urlParams.get('level') || "";
        const specialization = urlParams.get('specialization') || "";
        const campus = urlParams.get('campus') || "";
        const family = urlParams.get('family') || "";

        const isEnglish = window.location.pathname.includes('-en.html');

        // Sync native select values to match the URL parameters
        const levelSelect = document.getElementById('gadget-program');
        const specSelect = document.getElementById('gadget-specialization');
        const campusSelect = document.getElementById('gadget-campus');

        if (levelSelect && levelSelect.value !== level) {
            levelSelect.value = level;
            levelSelect.dispatchEvent(new Event('change'));
        }
        if (specSelect && specSelect.value !== specialization) {
            specSelect.value = specialization;
            specSelect.dispatchEvent(new Event('change'));
        }
        if (campusSelect && campusSelect.value !== campus) {
            campusSelect.value = campus;
            campusSelect.dispatchEvent(new Event('change'));
        }

        // Sync tab buttons active state
        const tabButtons = document.querySelectorAll('.program-families-tabs .tab-btn');
        tabButtons.forEach(btn => {
            if (btn.dataset.family === (family || 'all')) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        let activeFiltersCount = 0;
        if (level) activeFiltersCount++;
        if (specialization) activeFiltersCount++;
        if (campus) activeFiltersCount++;
        if (family) activeFiltersCount++;

        // If no filters are active, show all cards and hide status bar
        if (activeFiltersCount === 0) {
            programCards.forEach(card => {
                card.classList.remove('card-hidden');
                card.classList.remove('card-highlighted');
            });
            if (filterStatusBar) filterStatusBar.style.display = 'none';
            return;
        }

        // Show status bar
        if (filterStatusBar) {
            filterStatusBar.style.display = 'flex';
            // Populate tags
            filterStatusTags.innerHTML = '';

            if (family) {
                const familyLabels = {
                    'fle': isEnglish ? 'French (FLE)' : 'Parcours FLE',
                    'english': isEnglish ? 'English Pathways' : 'Parcours anglais',
                    'bts': 'BTS',
                    'bachelor': isEnglish ? 'Bachelor & BBA' : 'Bachelor'
                };
                createFilterTag(
                    isEnglish ? `Family: ${familyLabels[family] || family}` : `Famille : ${familyLabels[family] || family}`,
                    'family'
                );
            }
            if (level) {
                createFilterTag(
                    isEnglish ? `Level: ${level}` : `Niveau : ${level}`,
                    'level'
                );
            }
            if (specialization) {
                const specLabel = getSpecializationLabel(specialization, isEnglish);
                createFilterTag(
                    isEnglish ? `Specialization: ${specLabel}` : `Spécialité : ${specLabel}`,
                    'specialization'
                );
            }
            if (campus) {
                const campusLabel = getCampusLabel(campus, isEnglish);
                createFilterTag(
                    isEnglish ? `Campus: ${campusLabel}` : `Campus : ${campusLabel}`,
                    'campus'
                );
            }
        }

        // Filter cards
        let firstMatchCard = null;

        programCards.forEach(card => {
            const cardLevel = card.dataset.level;
            const cardFamily = card.dataset.family || "";
            const cardSpecs = card.dataset.specializations ? card.dataset.specializations.split(',') : [];
            const cardCampuses = card.dataset.campuses ? card.dataset.campuses.split(',') : [];

            let matches = true;

            if (family && cardFamily !== family) {
                matches = false;
            }
            if (level && cardLevel !== level) {
                matches = false;
            }
            if (specialization && !cardSpecs.includes(specialization)) {
                matches = false;
            }
            if (campus && !cardCampuses.includes(campus)) {
                matches = false;
            }

            if (matches) {
                card.classList.remove('card-hidden');
                card.classList.add('card-highlighted');
                if (!firstMatchCard) firstMatchCard = card;
            } else {
                card.classList.add('card-hidden');
                card.classList.remove('card-highlighted');
            }
        });

        // Smooth scroll to the filtered grid if query parameters were present
        if (smoothScroll && firstMatchCard) {
            setTimeout(() => {
                const container = document.querySelector('.programmes-grid-container');
                if (container) {
                    const headerOffset = document.querySelector('.site-header') ? document.querySelector('.site-header').offsetHeight : 80;
                    const containerPosition = container.getBoundingClientRect().top + window.scrollY - headerOffset - 20;
                    window.scrollTo({
                        top: containerPosition,
                        behavior: 'smooth'
                    });
                }
            }, 300);
        }
    }

    function createFilterTag(text, paramName) {
        const tag = document.createElement('span');
        tag.className = 'filter-tag';
        tag.innerHTML = `${text} <button class="remove-tag" aria-label="Remove filter">&times;</button>`;

        // Remove individual tag event
        tag.querySelector('.remove-tag').addEventListener('click', () => {
            const url = new URL(window.location);
            url.searchParams.delete(paramName);
            window.history.pushState({}, '', url);
            filterProgramsFromURL(false);
        });

        filterStatusTags.appendChild(tag);
    }

    function getSpecializationLabel(value, isEnglish) {
        const labels = {
            'general': isEnglish ? 'General French' : 'Français Général',
            'business': isEnglish ? 'Business French' : 'Professionnel & Affaires',
            'exam': isEnglish ? 'Exam Preparation' : 'Préparation Examens',
            'eloquence': isEnglish ? 'Eloquence & Leadership' : 'Éloquence & Leadership'
        };
        return labels[value] || value;
    }

    function getCampusLabel(value, isEnglish) {
        const labels = {
            'paris': isEnglish ? 'Paris (Neuilly)' : 'Paris (Neuilly)',
            'online': isEnglish ? 'Online' : 'En Ligne'
        };
        return labels[value] || value;
    }

    /* ==========================================================================
       Custom Glassmorphic Dropdowns
       ========================================================================== */
    function initCustomDropdowns() {
        const selectWrappers = document.querySelectorAll('.hero-search-gadget .select-wrapper');
        if (selectWrappers.length === 0) return;
        const updateHeroDropdownState = () => {
            document.querySelectorAll('.hero-image-wrapper').forEach(hero => {
                const hasOpenDropdown = !!hero.querySelector('.hero-search-gadget .gadget-custom-select.open');
                hero.classList.toggle('dropdown-open', hasOpenDropdown);
            });
        };

        selectWrappers.forEach(wrapper => {
            const select = wrapper.querySelector('select');
            if (!select) return;

            // Hide original select visually but keep it accessible for standard functionality
            select.style.position = 'absolute';
            select.style.width = '1px';
            select.style.height = '1px';
            select.style.padding = '0';
            select.style.margin = '-1px';
            select.style.overflow = 'hidden';
            select.style.clip = 'rect(0, 0, 0, 0)';
            select.style.border = '0';
            select.style.opacity = '0';
            select.style.pointerEvents = 'none';

            // Create custom select container
            const customSelect = document.createElement('div');
            customSelect.className = 'gadget-custom-select';
            customSelect.setAttribute('tabindex', '0');

            // Trigger element
            const trigger = document.createElement('div');
            trigger.className = 'gadget-custom-trigger';
            const triggerText = document.createElement('span');

            // Get initial selected option text
            const selectedOption = select.options[select.selectedIndex];
            triggerText.textContent = selectedOption ? selectedOption.text : select.options[0].text;
            trigger.appendChild(triggerText);

            // Arrow svg
            const arrowSpan = document.createElement('span');
            arrowSpan.className = 'gadget-custom-arrow';
            arrowSpan.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>`;
            trigger.appendChild(arrowSpan);
            customSelect.appendChild(trigger);

            // Options container
            const optionsContainer = document.createElement('div');
            optionsContainer.className = 'gadget-custom-options';

            // Build options list
            Array.from(select.options).forEach(opt => {
                const optDiv = document.createElement('div');
                optDiv.className = 'gadget-custom-option';
                if (opt.selected) {
                    optDiv.classList.add('selected');
                }
                optDiv.textContent = opt.text;
                optDiv.setAttribute('data-value', opt.value);

                optDiv.addEventListener('click', (e) => {
                    e.stopPropagation();
                    // Set select value
                    select.value = opt.value;
                    // Trigger change event on select
                    select.dispatchEvent(new Event('change'));

                    // Update trigger text
                    triggerText.textContent = opt.text;

                    // Update selected class
                    customSelect.querySelectorAll('.gadget-custom-option').forEach(o => o.classList.remove('selected'));
                    optDiv.classList.add('selected');

                    // Close dropdown
                    customSelect.classList.remove('open');
                    updateHeroDropdownState();
                });

                optionsContainer.appendChild(optDiv);
            });

            customSelect.appendChild(optionsContainer);
            wrapper.appendChild(customSelect);

            // Listen to native select change events to sync custom dropdown visuals programmatically
            select.addEventListener('change', () => {
                const selectedOption = select.options[select.selectedIndex];
                triggerText.textContent = selectedOption ? selectedOption.text : select.options[0].text;
                customSelect.querySelectorAll('.gadget-custom-option').forEach(o => {
                    if (o.getAttribute('data-value') === select.value) {
                        o.classList.add('selected');
                    } else {
                        o.classList.remove('selected');
                    }
                });
            });

            // Toggle dropdown open on click
            trigger.addEventListener('click', (e) => {
                e.stopPropagation();
                // Close all other custom dropdowns
                document.querySelectorAll('.gadget-custom-select').forEach(cs => {
                    if (cs !== customSelect) {
                        cs.classList.remove('open');
                    }
                });
                customSelect.classList.toggle('open');
                updateHeroDropdownState();
            });

            // Handle keyboard accessibility
            customSelect.addEventListener('keydown', (e) => {
                const options = Array.from(customSelect.querySelectorAll('.gadget-custom-option'));
                const activeIndex = options.findIndex(o => o.classList.contains('selected'));

                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    if (!customSelect.classList.contains('open')) {
                        customSelect.classList.add('open');
                        updateHeroDropdownState();
                    } else {
                        const nextIndex = (activeIndex + 1) % options.length;
                        options[nextIndex].click();
                    }
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    if (!customSelect.classList.contains('open')) {
                        customSelect.classList.add('open');
                        updateHeroDropdownState();
                    } else {
                        const prevIndex = (activeIndex - 1 + options.length) % options.length;
                        options[prevIndex].click();
                    }
                } else if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    customSelect.classList.toggle('open');
                    updateHeroDropdownState();
                } else if (e.key === 'Escape') {
                    customSelect.classList.remove('open');
                    updateHeroDropdownState();
                }
            });
        });

        // Click outside to close all dropdowns
        document.addEventListener('click', () => {
            document.querySelectorAll('.gadget-custom-select').forEach(cs => {
                cs.classList.remove('open');
            });
            updateHeroDropdownState();
        });
    }

    /* =========================================
       Admissions Mega-Menu Interactive System
       ========================================= */
    const admissionsMega = document.querySelector('.admissions-mega');
    if (admissionsMega) {
        const colMain = admissionsMega.querySelector('.adm-col-main');
        const colSub = admissionsMega.querySelector('.adm-col-sub');
        const colLinks = admissionsMega.querySelector('.adm-col-links');
        const colPreview = admissionsMega.querySelector('.adm-col-preview');

        if (colMain && colSub && colLinks) {
            const catButtons = colMain.querySelectorAll('.adm-card-btn');
            const subButtons = colSub.querySelectorAll('.adm-card-btn');

            // 1. Column 1 (Categories) hover behavior
            catButtons.forEach(btn => {
                btn.addEventListener('mouseenter', () => {
                    const target = btn.getAttribute('data-target');

                    // Toggle Column 1 active state
                    catButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    // Show matching Column 2 sub-panel
                    const targetPanel = colSub.querySelector(`#sub-panel-${target}`);
                    if (targetPanel) {
                        colSub.querySelectorAll('.adm-sub-panel').forEach(p => p.classList.remove('active'));
                        targetPanel.classList.add('active');

                        // Auto-activate first item in Column 2 panel
                        const firstSubBtn = targetPanel.querySelector('.adm-card-btn');
                        if (firstSubBtn) {
                            // Trigger hover behavior for the first item
                            const subTarget = firstSubBtn.getAttribute('data-target');
                            targetPanel.querySelectorAll('.adm-card-btn').forEach(b => b.classList.remove('active'));
                            firstSubBtn.classList.add('active');

                            const targetLinksPanel = colLinks.querySelector(`#links-panel-${subTarget}`);
                            if (targetLinksPanel) {
                                colLinks.querySelectorAll('.adm-links-panel').forEach(p => p.classList.remove('active'));
                                targetLinksPanel.classList.add('active');
                            }

                            if (colPreview) {
                                const targetPreviewCard = colPreview.querySelector(`[data-preview="${subTarget}"]`);
                                if (targetPreviewCard) {
                                    colPreview.querySelectorAll('.adm-preview-card').forEach(p => p.classList.remove('active'));
                                    targetPreviewCard.classList.add('active');
                                }
                            }
                        }
                    }
                });
            });

            // 2. Column 2 (Sub-categories) hover behavior
            subButtons.forEach(subBtn => {
                subBtn.addEventListener('mouseenter', () => {
                    const subPanel = subBtn.closest('.adm-sub-panel');
                    const target = subBtn.getAttribute('data-target');

                    // Toggle Column 2 active state within its panel
                    if (subPanel) {
                        subPanel.querySelectorAll('.adm-card-btn').forEach(b => b.classList.remove('active'));
                    }
                    subBtn.classList.add('active');

                    // Show matching Column 3 links panel
                    const targetLinksPanel = colLinks.querySelector(`#links-panel-${target}`);
                    if (targetLinksPanel) {
                        colLinks.querySelectorAll('.adm-links-panel').forEach(p => p.classList.remove('active'));
                        targetLinksPanel.classList.add('active');
                    }

                    if (colPreview) {
                        const targetPreviewCard = colPreview.querySelector(`[data-preview="${target}"]`);
                        if (targetPreviewCard) {
                            colPreview.querySelectorAll('.adm-preview-card').forEach(p => p.classList.remove('active'));
                            targetPreviewCard.classList.add('active');
                        }
                    }
                });
            });
        }
    }

    // Initialize Quick Feedback Widget
    initFeedbackWidget();
});

/* ==========================================================================
   Quick Feedback Widget (Global Injection & Logic)
   ========================================================================== */
function initFeedbackWidget() {
    // 1. Inject HTML
    const feedbackHTML = `
        <div class="cs-feedback-container" id="cs-feedback-container">
            <div class="cs-feedback-modal" id="cs-feedback-modal" role="dialog" aria-label="Feedback form">
                <div class="cs-feedback-header">
                    <h3 class="cs-feedback-title">How was your experience today?</h3>
                    <button class="cs-feedback-close" id="cs-feedback-close" aria-label="Close feedback">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                </div>
                <div class="cs-feedback-body">
                    <div id="cs-feedback-success" class="cs-feedback-success" style="display: none;">
                        <svg class="cs-feedback-success-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                        <h4>Thank you for your feedback!</h4>
                        <p>We appreciate your input.</p>
                    </div>
                    
                    <form id="cs-feedback-form">
                        <div class="cs-feedback-emojis" id="cs-feedback-emojis">
                            <button type="button" class="cs-feedback-emoji" data-value="excellent" title="Excellent">😍</button>
                            <button type="button" class="cs-feedback-emoji" data-value="good" title="Good">🙂</button>
                            <button type="button" class="cs-feedback-emoji" data-value="average" title="Average">😐</button>
                            <button type="button" class="cs-feedback-emoji" data-value="poor" title="Poor">😕</button>
                            <button type="button" class="cs-feedback-emoji" data-value="very_poor" title="Very Poor">😡</button>
                        </div>

                        <div class="cs-feedback-details" id="cs-feedback-details">
                            <textarea id="cs-feedback-text" class="cs-feedback-input cs-feedback-textarea" placeholder="Tell us more... (Optional)" rows="3"></textarea>
                            <input type="email" id="cs-feedback-email" class="cs-feedback-input" placeholder="Your email if you'd like a response (Optional)">
                            <button type="submit" id="cs-feedback-submit" class="cs-feedback-submit">Send Feedback</button>
                        </div>
                    </form>
                </div>
            </div>

            <button class="cs-feedback-trigger" id="cs-feedback-trigger" aria-label="Open feedback form">
                <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            </button>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', feedbackHTML);

    // 2. DOM Elements
    const trigger = document.getElementById('cs-feedback-trigger');
    const modal = document.getElementById('cs-feedback-modal');
    const closeBtn = document.getElementById('cs-feedback-close');
    const emojis = document.querySelectorAll('.cs-feedback-emoji');
    const details = document.getElementById('cs-feedback-details');
    const form = document.getElementById('cs-feedback-form');
    const successView = document.getElementById('cs-feedback-success');
    const submitBtn = document.getElementById('cs-feedback-submit');

    let isOpen = false;
    let selectedReaction = null;
    let pulseInterval;

    // 3. Pulse Animation Loop
    function startPulseLoop() {
        pulseInterval = setInterval(() => {
            if (!isOpen) {
                trigger.classList.add('animate-pulse');
                setTimeout(() => {
                    trigger.classList.remove('animate-pulse');
                }, 2000);
            }
        }, 45000);
    }
    startPulseLoop();

    // 4. Handlers
    function openModal() {
        isOpen = true;
        trigger.classList.add('is-hidden');
        modal.classList.add('is-open');
        // Small delay to allow display:block to apply before animating opacity/transform
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                modal.classList.add('is-visible');
            });
        });
    }

    function closeModal() {
        isOpen = false;
        modal.classList.remove('is-visible');
        trigger.classList.remove('is-hidden');
        
        // Wait for animation to finish before hiding and resetting
        setTimeout(() => {
            modal.classList.remove('is-open');
            resetForm();
        }, 400); // Matches CSS transition duration
    }

    function resetForm() {
        selectedReaction = null;
        emojis.forEach(e => e.classList.remove('selected'));
        details.classList.remove('is-visible');
        form.reset();
        
        // Hide success view, show form again
        successView.style.display = 'none';
        successView.classList.remove('is-visible');
        form.style.display = 'block';
        submitBtn.disabled = false;
        submitBtn.textContent = 'Send Feedback';
    }

    trigger.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);

    // Emoji Selection
    emojis.forEach(emoji => {
        emoji.addEventListener('click', (e) => {
            selectedReaction = e.target.dataset.value;
            
            // Visual selection
            emojis.forEach(btn => btn.classList.remove('selected'));
            e.target.classList.add('selected');

            // Expand details
            details.classList.add('is-visible');
        });
    });

    // Form Submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!selectedReaction) return;

        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        // Simulate network request
        setTimeout(() => {
            form.style.display = 'none';
            successView.style.display = 'flex';
            
            // Trigger animation
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    successView.classList.add('is-visible');
                });
            });

            // Auto close after 3 seconds
            setTimeout(() => {
                closeModal();
            }, 3000);
            
        }, 800);
    });
}
