import { Outlet } from "react-router-dom";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function Layout() {
  return (
    <div className="min-h-screen bg-[#09090F] text-white flex">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Topbar />

        <main className="flex-1 p-8 overflow-auto">

          <Outlet />

        </main>

      </div>

    </div>
  );
}