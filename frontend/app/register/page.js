"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Register() {
    const router = useRouter();
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [goal, setGoal] = useState("عبادة");

    async function handleSubmit(e) {
        e.preventDefault();

        const res = await fetch("http://127.0.0.1:8000/users", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, email, goal }),
        });

        const data = await res.json();
        localStorage.setItem("user", JSON.stringify(data));
        router.push("/dashboard");
    }

    return (
        <main className="min-h-screen bg-black text-white flex items-center justify-center">
            <form
                onSubmit={handleSubmit}
                className="bg-zinc-900 p-8 rounded-xl w-full max-w-md"
            >
                <h2 className="text-2xl font-bold mb-6 text-center">
                    إنشاء حساب رمضاني 🌙
                </h2>

                <input
                    placeholder="الاسم"
                    className="w-full p-3 mb-4 rounded bg-zinc-800"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />

                <input
                    placeholder="البريد الإلكتروني"
                    className="w-full p-3 mb-4 rounded bg-zinc-800"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <select
                    className="w-full p-3 mb-6 rounded bg-zinc-800"
                    value={goal}
                    onChange={(e) => setGoal(e.target.value)}
                >
                    <option value="عبادة">التركيز على العبادة</option>
                    <option value="تنظيم وقت">تنظيم الوقت</option>
                    <option value="الاثنين">الاثنين معًا</option>
                </select>

                <button className="w-full bg-emerald-500 text-black py-3 rounded font-semibold">
                    دخول رمضان
                </button>
            </form>
        </main>
    );
}
