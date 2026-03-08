document.addEventListener("DOMContentLoaded", function () {

    function applyScrollHint(container) {
        if (container.dataset.scrollHinted) return;
        container.dataset.scrollHinted = "true";

        const distance = 200;
        const duration = 1200;
        let start = null;

        function ease(t) {
            // ease-out cubic
            return 1 - Math.pow(1 - t, 3);
        }

        function step(timestamp) {
            if (!start) start = timestamp;
            var progress = Math.min((timestamp - start) / duration, 1);
            container.scrollLeft = distance * ease(progress);
            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }

        requestAnimationFrame(step);
    }

    // Observe when .myProjectsDiv enters the viewport
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                setTimeout(function () { applyScrollHint(entry.target); }, 1500);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    // The div may not exist yet (Dash renders dynamically), so poll for it
    var interval = setInterval(function () {
        var el = document.querySelector(".myProjectsDiv");
        if (el) {
            clearInterval(interval);
            observer.observe(el);
        }
    }, 500);
});
