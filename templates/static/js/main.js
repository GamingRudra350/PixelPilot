document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({
        duration: 1000,     // Animation duration
        once: true,         // Run animation only once
        offset: 100,        // Trigger when 100px in viewport
    });

    console.log('%cPixelPilot Animations Loaded!', 'color: #3b82f6; font-weight: bold;');
});
.hero-bg h1, .hero-bg p, .hero-bg a {
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.text-blue-100 {
    color: #dbeafe;
}