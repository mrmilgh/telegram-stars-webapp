document.getElementById("buyButton").addEventListener("click", function () {
    const tg = window.Telegram?.WebApp;
    if (!tg) {
        alert("WebApp API در دسترس نیست.");
        return;
    }

    const userId = tg.initDataUnsafe?.user?.id || null;

    fetch("https://your-backend.com/api/stars/buy", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user_id: userId,
            credits: 10
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success && data.redirect_url) {
            window.location.href = data.redirect_url;
        } else {
            alert("❌ خطا در خرید: " + (data.error || "پاسخ نامعتبر"));
        }
    })
    .catch(err => {
        console.error("Fetch Error:", err);
        alert("❌ خطا در ارتباط با سرور");
    });
});
