import { Check, X } from "lucide-react";
import useProcurement from "../hooks/useProcurement";

export default function Procurement() {

  const {
    loading,
    orders,
    approve,
    reject,
  } = useProcurement();

  if (loading)
    return (
      <div className="text-2xl">
        Loading Purchase Orders...
      </div>
    );

  return (

    <div>

      <h1 className="text-4xl font-bold mb-8">

        Purchase Orders

      </h1>

      <div className="grid xl:grid-cols-2 gap-6">

        {orders.map((order)=>(

          <div
            key={order.id}
            className="rounded-3xl border border-white/10 bg-white/5 p-7"
          >

            <h2 className="text-2xl font-bold">

              {order.product_name}

            </h2>

            <div className="mt-6 space-y-3">

              <p>

                Supplier :

                <strong>

                  {" "}

                  {order.supplier}

                </strong>

              </p>

              <p>

                Quantity :

                <strong>

                  {" "}

                  {order.quantity}

                </strong>

              </p>

              <p>

                Cost :

                <strong>

                  {" "}

                  ₹{order.estimated_cost}

                </strong>

              </p>

              <p>

                Status :

                <strong>

                  {" "}

                  {order.status}

                </strong>

              </p>

            </div>

            {order.status === "PENDING" && (

              <div className="flex gap-4 mt-8">

                <button
                  onClick={()=>approve(order.id)}
                  className="flex-1 rounded-xl bg-green-600 py-3 flex justify-center items-center gap-2"
                >

                  <Check size={18}/>

                  Approve

                </button>

                <button
                  onClick={()=>reject(order.id)}
                  className="flex-1 rounded-xl bg-red-600 py-3 flex justify-center items-center gap-2"
                >

                  <X size={18}/>

                  Reject

                </button>

              </div>

            )}

          </div>

        ))}

      </div>

    </div>

  );

}