"use client";

import { useState } from "react";

export default function Assistant() {
    const user = JSON.parse(localStorage.getItem("user"));
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState("");

    async function askAI() {
        const res = await fetch("https://ramadan-companion-production.up.railway.app/assistant", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                user_id: user.id,
                message,
                day: 12,
            }),
        });

        const data = await res.json();
        setResponse(data.response);
    }

    return (
        <main className="min-h-screen bg-black text-white px-6 py-10">
            <h1 className="text-2xl font-bold mb-4">🤖 المساعد الرمضاني</h1>

            <textarea
                className="w-full p-4 rounded bg-zinc-800 mb-4"
                placeholder="اكتب ما تشعر به..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />

            <button
                onClick={askAI}
                className="bg-emerald-500 text-black px-6 py-3 rounded"
            >
                اسأل
            </button>

            {response && (
                <div className="bg-zinc-900 p-6 rounded-xl mt-6">
                    <p>{response}</p>
                </div>
            )}
        </main>
    );
}
