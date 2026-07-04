import { Bell, Search, UserCircle2 } from "lucide-react";

export default function Topbar() {
  return (
    <header className="h-24 border-b border-white/10 bg-[#09090F]/70 backdrop-blur-xl px-10 flex items-center justify-between">

      <div>

        <h1 className="text-3xl font-bold">

          Good Morning 👋

        </h1>

        <p className="text-gray-400">

          Your AI COO is monitoring your business.

        </p>

      </div>

      <div className="flex items-center gap-5">

        <button className="h-11 w-11 rounded-xl bg-white/5 hover:bg-white/10 flex items-center justify-center">

          <Search size={18} />

        </button>

        <button className="h-11 w-11 rounded-xl bg-white/5 hover:bg-white/10 flex items-center justify-center">

          <Bell size={18} />

        </button>

        <UserCircle2 size={42} />

      </div>

    </header>
  );
}