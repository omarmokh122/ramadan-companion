"use client";

import { useEffect, useState } from "react";

export default function Dashboard() {
    const [daily, setDaily] = useState(null);

    useEffect(() => {
        fetch("https://ramadan-companion-production.up.railway.app/daily/10")
            .then((res) => res.json())
            .then(setDaily);
    }, []);

    if (!daily) return <p className="text-white">Loading...</p>;

    return (
        <main className="min-h-screen bg-black text-white px-6 py-10">
            <h1 className="text-3xl font-bold mb-6">🌙 يومك في رمضان</h1>

            <div className="space-y-6">
                <div className="bg-zinc-900 p-6 rounded-xl">
                    <h3 className="font-semibold mb-2">✨ رسالة اليوم</h3>
                    <p>{daily.message}</p>
                </div>

                <div className="bg-zinc-900 p-6 rounded-xl">
                    <h3 className="font-semibold mb-2">🤲 دعاء اليوم</h3>
                    <p>{daily.duaa}</p>
                </div>

                <div className="bg-zinc-900 p-6 rounded-xl">
                    <h3 className="font-semibold mb-2">📖 ورد القرآن</h3>
                    <p>{daily.quran}</p>
                </div>

                <a
                    href="/assistant"
                    className="inline-block bg-emerald-500 text-black px-6 py-3 rounded-xl"
                >
                    تحدث مع المساعد الذكي
                </a>
            </div>
        </main>
    );
}
