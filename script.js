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
        'history-1': 'https://images.unsplash.com/photo-1524069290683-0457abfe42c3?q=80&w=2070&auto=format&fit=crop',
        'history-2': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=2070&auto=format&fit=crop',
        'history-3': 'https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=2070&auto=format&fit=crop'
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
});
