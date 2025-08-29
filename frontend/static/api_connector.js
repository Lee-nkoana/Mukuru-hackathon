async function apiRequest(endpoint, data) {
    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data),
        });
        return await response.json();

    } catch (error) {
        console.error("API error:", error);
        return { message: "Server error. Try again later." };
    }
}

async function registerUser(data) {
    return await apiRequest("/api/register", data);
}

async function loginUser(email, password) {
    return await apiRequest("/login", { email, password });
}