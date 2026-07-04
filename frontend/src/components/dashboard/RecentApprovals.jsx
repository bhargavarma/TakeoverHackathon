import { useEffect, useState } from "react";
import { getPurchaseOrders } from "../../services/dashboardService";

export default function RecentApprovals() {

  const [orders, setOrders] = useState([]);

  useEffect(() => {
    loadOrders();
  }, []);

  async function loadOrders() {
    try {
      const data = await getPurchaseOrders();
      setOrders(data);
    } catch {
      console.log("Couldn't load purchase orders");
    }
  }

  return (
    <div className="rounded-3xl bg-white/5 border border-white/10 p-8">

      <h2 className="text-2xl font-bold mb-8">
        Pending Approvals
      </h2>

      <div className="space-y-5">

        {orders.map((item) => (

          <div
            key={item.id}
            className="rounded-2xl bg-white/5 p-5 flex justify-between"
          >

            <div>

              <h3 className="font-semibold">
                {item.item}
              </h3>

              <p className="text-gray-400">
                {item.status}
              </p>

            </div>

            <button
              onClick={() => alert("Approve functionality coming next")}
              className="rounded-xl bg-violet-600 px-5"
            >
              Review
            </button>

          </div>

        ))}

      </div>

    </div>
  );
}