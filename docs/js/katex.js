document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\(", right: "\\)", display: false},
            {left: "\\[", right: "\\]", display: true}
        ],
        throwOnError: false
    });
});

// Fix per l'accessibilità della ricerca
document.addEventListener("DOMContentLoaded", function() {
    var searchDialog = document.querySelector('.md-search[role="dialog"]');
    if (searchDialog) {
        searchDialog.setAttribute('aria-label', 'Ricerca');
    }
});