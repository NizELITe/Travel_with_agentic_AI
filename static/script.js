// static/script.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("query-form");
    const input = document.getElementById("query");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const query = input.value.trim();
        if (!query) return;

        resultDiv.innerHTML = "<p>🔍 Processing your request...</p>";

        try {
            const response = await fetch("/query", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query }),
            });

            const data = await response.json();

            if (data.error) {
                resultDiv.innerHTML = `<p style="color:red;">⚠️ ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <h3>📌 Full State</h3>
                    <pre>${JSON.stringify(data.state, null, 2)}</pre>
                    
                    <h3>🏨 Hotel Result</h3>
                    <pre>${JSON.stringify(data.hotel_result, null, 2) || "None"}</pre>
                    
                    <h3>✈️ Flight Result</h3>
                    <pre>${JSON.stringify(data.flight_result, null, 2) || "None"}</pre>
                `;
            }
        } catch (err) {
            resultDiv.innerHTML = `<p style="color:red;">❌ Request failed: ${err}</p>`;
        }
    });
});
