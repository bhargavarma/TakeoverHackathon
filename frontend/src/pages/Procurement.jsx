import { Check, X } from "lucide-react";
import useProcurement from "../hooks/useProcurement";

export default function Procurement() {

  const { loading, orders } = useProcurement();

  if (loading)
    return <h2>Loading Procurement...</h2>;

  return (
    <div>

      <h1 className="text-4xl font-bold mb-8">

        AI Purchase Recommendations

      </h1>

      <div className="grid grid-cols-2 gap-6">

        {orders.map((order, index) => (

          <div
            key={index}
            className="rounded-3xl bg-white/5 border border-white/10 p-7"
          >

            <h2 className="text-2xl font-bold">

              {order.product_name}

            </h2>

            <div className="mt-5 space-y-3">

              <p>

                Current Stock :
                <strong>
                  {" "}
                  {order.current_stock}
                </strong>

              </p>

              <p>

                Suggested Qty :
                <strong>
                  {" "}
                  {order.recommended_quantity}
                </strong>

              </p>

              <p>

                Supplier :
                <strong>
                  {" "}
                  {order.best_supplier}
                </strong>

              </p>

              <p>

                Estimated Cost :
                <strong>
                  {" "}
                  ₹{order.estimated_cost}
                </strong>

              </p>

            </div>

            <div className="flex gap-4 mt-8">

              <button
                className="flex-1 rounded-xl bg-green-600 hover:bg-green-700 py-3 flex justify-center items-center gap-2"
              >

                <Check size={18} />

                Approve

              </button>

              <button
                className="flex-1 rounded-xl bg-red-600 hover:bg-red-700 py-3 flex justify-center items-center gap-2"
              >

                <X size={18} />

                Reject

              </button>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}