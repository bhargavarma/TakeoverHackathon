import GlassCard from "../ui/GlassCard";

import {
  IndianRupee,
  TrendingUp,
  ShoppingCart,
  Boxes,
} from "lucide-react";

export default function StatsGrid({ data }) {

  if (!data) {
    return null;
  }

  return (

    <div className="grid lg:grid-cols-4 gap-6">

      <GlassCard
        icon={<IndianRupee size={30} />}
        title="Revenue"
        value={`₹${data.revenue.toLocaleString()}`}
      />

      <GlassCard
        icon={<TrendingUp size={30} />}
        title="Profit"
        value={`₹${data.profit.toLocaleString()}`}
      />

      <GlassCard
        icon={<Boxes size={30} />}
        title="Inventory"
        value={data.inventory}
      />

      <GlassCard
        icon={<ShoppingCart size={30} />}
        title="Orders"
        value={data.orders}
      />

    </div>

  );
}