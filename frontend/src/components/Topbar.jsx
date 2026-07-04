import { Search, Bell, CircleUserRound } from "lucide-react";

export default function Topbar() {
  return (
    <header className="h-20 border-b border-zinc-800 px-8 flex items-center justify-between">

      <div>

        <h1 className="text-3xl font-bold">
          Good Morning 👋
        </h1>

        <p className="text-zinc-400">
          AI COO is managing your business.
        </p>

      </div>

      <div className="flex gap-5">

        <Search className="cursor-pointer" />

        <Bell className="cursor-pointer" />

        <CircleUserRound className="cursor-pointer" />

      </div>

    </header>
  );
}