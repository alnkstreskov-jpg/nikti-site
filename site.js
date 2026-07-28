(function (window, document, tagName, source, functionName, script, firstScript) {
    window[functionName] = window[functionName] || function () {
        (window[functionName].a = window[functionName].a || []).push(arguments);
    };
    window[functionName].l = Date.now();
    for (var index = 0; index < document.scripts.length; index += 1) {
        if (document.scripts[index].src === source) return;
    }
    script = document.createElement(tagName);
    firstScript = document.getElementsByTagName(tagName)[0];
    script.async = true;
    script.src = source;
    firstScript.parentNode.insertBefore(script, firstScript);
})(window, document, "script", "https://mc.yandex.ru/metrika/tag.js?id=110602002", "ym");

window.ym(110602002, "init", {
    accurateTrackBounce: true,
    clickmap: true,
    referrer: document.referrer,
    ssr: true,
    trackLinks: true,
    url: window.location.href,
    webvisor: true
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-goal]").forEach(function (element) {
        element.addEventListener("click", function () {
            window.ym(110602002, "reachGoal", element.dataset.goal);
        });
    });
});
