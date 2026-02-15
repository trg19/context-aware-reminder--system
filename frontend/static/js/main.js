// Function for Login (FR-1b)
async function loginUser() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert("Please fill in all fields");
        return;
    }

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            alert("Login Successful!");
            window.location.href = "/"; // Redirect to Dashboard (index.html)
        } else {
            alert("Login Failed: " + data.message);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Could not connect to server.");
    }
}

// Function for Registration (FR-1a)
async function registerUser() {
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fullName, email, password })
    });

    if (response.ok) {
        alert("Account Created! Please login.");
        window.location.href = "/login";
    } else {
        const data = await response.json();
        alert("Error: " + data.error);
    }
}