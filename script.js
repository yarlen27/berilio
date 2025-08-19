document.addEventListener('DOMContentLoaded', function() {
    // Simple navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.08)';
            navbar.classList.add('scrolled');
        } else {
            navbar.style.boxShadow = 'none';
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });

    // Smooth scroll for internal links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple button hover effects
    const buttons = document.querySelectorAll('button, .nav-btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-1px)';
        });
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Feature cards entrance animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Animate feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });

    // Demo button handler
    const demoButtons = document.querySelectorAll('[href="#demo"], .btn-primary, .btn-cta');
    demoButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.textContent.toLowerCase().includes('demo') || 
                this.textContent.toLowerCase().includes('probar') ||
                this.textContent.toLowerCase().includes('comenzar')) {
                e.preventDefault();
                
                // Simple modal or alert for demo
                const userEmail = prompt('¿Cuál es tu email corporativo? Te contactaremos para agendar una demo de Cobalto SIG.');
                
                if (userEmail && userEmail.includes('@')) {
                    alert('¡Gracias! Te contactaremos pronto para agendar tu demo personalizada.');
                    // Here you would normally send to your backend
                    console.log('Demo request:', userEmail);
                }
            }
        });
    });

    // Simple form validation for future use
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Performance optimization: lazy load images when needed
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    const src = img.getAttribute('data-src');
                    if (src) {
                        img.src = src;
                        img.removeAttribute('data-src');
                        observer.unobserve(img);
                    }
                }
            });
        });

        // Observe lazy images (for future use)
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // Simple analytics tracking (placeholder)
    function trackEvent(action, category = 'engagement') {
        console.log(`Analytics: ${category} - ${action}`);
        // Here you would send to your analytics service
    }

    // Track button clicks
    document.addEventListener('click', function(e) {
        if (e.target.matches('button') || e.target.matches('.btn-primary') || e.target.matches('.btn-secondary')) {
            trackEvent(`click-${e.target.textContent.toLowerCase().replace(/\s+/g, '-')}`);
        }
    });
});