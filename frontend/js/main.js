const form = document.querySelector("#uploadForm");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    result.textContent = "Submitting...";

    const response = await fetch("/api/upload", {
        method: "POST",
        body: new FormData(form),
    });

    const data = await response.json();
    if (!response.ok) {
        result.textContent = data.error || "Submission failed.";
        return;
    }

    result.textContent = `Saved. Wear level: ${data.record.damage_level}`;
    form.reset();
});
