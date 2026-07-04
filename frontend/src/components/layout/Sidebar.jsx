import {
  LayoutDashboard,
  Sparkles,
  Boxes,
  ShoppingCart,
  BarChart3,
  IndianRupee,
  Bell,
  Settings,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const links = [
  {
    icon: LayoutDashboard,
    title: "Dashboard",
    path: "/",
  },
  {
    icon: Sparkles,
    title: "AI Operations",
    path: "/",
  },
  {
    icon: Boxes,
    title: "Inventory",
    path: "/inventory",
  },
  {
    icon: ShoppingCart,
    title: "Procurement",
    path: "/procurement",
  },
  {
    icon: BarChart3,
    title: "Analytics",
    path: "/analytics",
  },
  {
    icon: IndianRupee,
    title: "Finance",
    path: "/finance",
  },
  {
    icon: Bell,
    title: "Notifications",
    path: "/notifications",
  },
  {
    icon: Settings,
    title: "Settings",
    path: "/settings",
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-[#10111A] border-r border-white/10 flex flex-col">

      <div className="p-8">

        <div className="flex items-center gap-4">

          <div className="h-12 w-12 rounded-2xl bg-gradient-to-r from-violet-600 to-cyan-500 flex items-center justify-center font-bold text-xl">

            AI

          </div>

          <div>

            <h1 className="font-bold text-xl">
              AI COO
            </h1>

            <p className="text-sm text-gray-400">
              Business Operating System
            </p>

          </div>

        </div>

      </div>

      <div className="flex-1 px-4">

        {links.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.title}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-4 px-4 py-4 rounded-2xl mb-3 transition-all ${
                  isActive
                    ? "bg-gradient-to-r from-violet-600 to-cyan-500"
                    : "hover:bg-white/10"
                }`
              }
            >

              <Icon size={20} />

              {item.title}

            </NavLink>
          );

        })}

      </div>

      <div className="p-6">

        <div className="rounded-2xl bg-white/5 p-5">

          <div className="flex items-center gap-3">

            <div className="h-3 w-3 rounded-full bg-green-500 animate-pulse"></div>

            <span className="text-sm">

              AI Monitoring Active

            </span>

          </div>

        </div>

      </div>

    </aside>
  );
}