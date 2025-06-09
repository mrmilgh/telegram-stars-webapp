function buyStars(credits) {
    const tg = window.Telegram?.WebApp;
    if (!tg) {
        alert("WebApp API در دسترس نیست.");
        return;
    }

    const userId = tg.initDataUnsafe?.user?.id || null;
    const initData = tg.initData || null;

    if (!userId || !initData) {
        alert("اطلاعات کاربر یا توکن امنیتی WebApp ناقص است.");
        return;
    }

    // نمایش بارگذاری
    tg.MainButton.setText("در حال پردازش...").show().disable();

    fetch("https://your-backend.com/api/stars/buy", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user_id: userId,
            credits: credits,
            init_data: initData
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success && data.message) {
            alert("✅ " + data.message);
        } else {
            alert("❌ خطا در خرید: " + (data.error || "پاسخ نامعتبر"));
        }
    })
    .catch(err => {
        console.error("Fetch Error:", err);
        alert("❌ خطا در ارتباط با سرور");
    })
    .finally(() => {
        tg.MainButton.hide().enable();
    });
}
