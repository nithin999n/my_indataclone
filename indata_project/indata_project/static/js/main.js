function openSidebar() {
    document.getElementById('sidebarMenu').classList.add('active');
    document.getElementById('sidebarOverlay').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeSidebar() {
    document.getElementById('sidebarMenu').classList.remove('active');
    document.getElementById('sidebarOverlay').classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openSearch() {
    document.getElementById('searchModal').classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
        const searchInput = document.querySelector('#searchModal input');
        if (searchInput) {
            searchInput.focus();
        }
    }, 300);
}

function closeSearch() {
    document.getElementById('searchModal').classList.remove('active');
    document.body.style.overflow = 'auto';
}
