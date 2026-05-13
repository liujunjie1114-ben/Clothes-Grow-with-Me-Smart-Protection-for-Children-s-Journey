document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("[data-user-form]");
    if (!form) {
        return;
    }

    form.addEventListener("submit", () => {
        const button = form.querySelector("button[type='submit']");
        if (button) {
            button.disabled = true;
            button.textContent = "Submitting...";
        }
    });
});
