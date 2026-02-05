export default function Home() {
    return (
        <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-6">
            <h1 className="text-4xl md:text-5xl font-bold mb-4 text-center">
                رفيقك الذكي في رمضان 🌙
            </h1>

            <p className="text-gray-300 max-w-xl text-center mb-8">
                منصة ذكية ترافقك يوميًا في رمضان بالذكر، الدعاء،
                وتنظيم الوقت — بأسلوب هادئ وإنساني.
            </p>

            <a
                href="/register"
                className="bg-emerald-500 hover:bg-emerald-600 text-black font-semibold px-6 py-3 rounded-xl transition"
            >
                ابدأ الآن
            </a>
        </main>
    );
}
