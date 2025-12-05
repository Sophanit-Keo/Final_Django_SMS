// Sidebar Navigation JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initializeSidebar();
    setActiveLink();
});

function setActiveLink() {
    // Get current page URL
    const currentUrl = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
    
    sidebarLinks.forEach(link => {
        // Remove any existing active class
        link.classList.remove('active');
        
        // Get the href attribute
        const href = link.getAttribute('href');
        
        // Skip logout/login links - they shouldn't get active state
        if (href && (href.includes('/logout') || href === '/')) {
            return;
        }
        
        // Check if this link matches the current URL
        if (href && currentUrl.includes(href)) {
            link.classList.add('active');
        }
    });
}

function initializeSidebar() {
    // Handle sidebar link clicks
    const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Don't prevent default for logout or external links
            if (this.getAttribute('href') === '#' || this.onclick) {
                return;
            }
            
            // Update active state immediately on click
            sidebarLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            
            // Add click animation
            this.classList.add('clicked');
            setTimeout(() => {
                this.classList.remove('clicked');
            }, 300);
        });
        
        // Add hover effect
        link.addEventListener('mouseenter', function() {
            this.classList.add('hover-active');
        });
        
        link.addEventListener('mouseleave', function() {
            this.classList.remove('hover-active');
        });
    });
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(e) {
        const sidebar = document.querySelector('.sidebar');
        const toggle = document.querySelector('.sidebar-toggle');
        
        if (window.innerWidth <= 768 && 
            sidebar && 
            !sidebar.contains(e.target) && 
            !toggle?.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    });
    
    // Handle window resize
    window.addEventListener('resize', function() {
        const sidebar = document.querySelector('.sidebar');
        const toggle = document.querySelector('.sidebar-toggle');
        
        if (window.innerWidth > 768) {
            sidebar?.classList.remove('active');
            if (toggle) toggle.style.display = 'none';
        } else {
            if (toggle) toggle.style.display = 'block';
        }
    });
}

// Navigation utilities
function navigateTo(path) {
    window.location.href = path;
}

function setActiveMenuItem(path) {
    const links = document.querySelectorAll('.sidebar-menu a');
    links.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === path) {
            link.classList.add('active');
        }
    });
}

// Make functions globally available
window.navigateTo = navigateTo;
window.setActiveMenuItem = setActiveMenuItem;