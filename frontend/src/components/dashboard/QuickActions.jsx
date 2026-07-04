import { Sparkles, Boxes, ShoppingCart } from "lucide-react";
import { runReview } from "../../services/dashboardService";
import { useNavigate } from "react-router-dom";

export default function QuickActions() {

  const navigate = useNavigate();

  async function handleReview() {
    try {
      const res = await runReview();
      alert(res.message);
    } catch {
      alert("Failed to run AI Review");
    }
  }

  return (
    <div className="rounded-3xl bg-white/5 border border-white/10 p-8">

      <h2 className="text-2xl font-bold mb-6">
        Quick Actions
      </h2>

      <div className="space-y-4">

        <button
          onClick={handleReview}
          className="w-full rounded-2xl bg-white/5 hover:bg-violet-600 transition p-5 flex items-center gap-4"
        >
          <Sparkles />
          Run Daily Review
        </button>

        <button
          onClick={() => navigate("/inventory")}
          className="w-full rounded-2xl bg-white/5 hover:bg-violet-600 transition p-5 flex items-center gap-4"
        >
          <Boxes />
          Inventory Scan
        </button>

        <button
          onClick={() => navigate("/procurement")}
          className="w-full rounded-2xl bg-white/5 hover:bg-violet-600 transition p-5 flex items-center gap-4"
        >
          <ShoppingCart />
          Generate PO
        </button>

      </div>

    </div>
  );
}