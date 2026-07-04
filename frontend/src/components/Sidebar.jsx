import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Boxes,
  ShoppingCart,
  BarChart3,
  IndianRupee,
  Bell,
  Settings,
} from "lucide-react";

const links = [
  { name: "Dashboard", path: "/", icon: LayoutDashboard },
  { name: "Inventory", path: "/inventory", icon: Boxes },
  { name: "Procurement", path: "/procurement", icon: ShoppingCart },
  { name: "Analytics", path: "/analytics", icon: BarChart3 },
  { name: "Finance", path: "/finance", icon: IndianRupee },
  { name: "Notifications", path: "/notifications", icon: Bell },
  { name: "Settings", path: "/settings", icon: Settings },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-[#111117] border-r border-zinc-800 p-6">

      <h1 className="text-3xl font-bold mb-10">
        AI COO
      </h1>

      <div className="space-y-3">

        {links.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 px-5 py-4 rounded-xl transition ${
                  isActive
                    ? "bg-gradient-to-r from-purple-600 to-cyan-500"
                    : "hover:bg-zinc-800"
                }`
              }
            >
              <Icon size={20} />
              {item.name}
            </NavLink>
          );
        })}

      </div>

    </aside>
  );
}