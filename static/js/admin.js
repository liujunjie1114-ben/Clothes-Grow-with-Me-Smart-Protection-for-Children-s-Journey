document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-status-form]").forEach((form) => {
        form.addEventListener("change", () => {
            form.submit();
        });
    });
});
