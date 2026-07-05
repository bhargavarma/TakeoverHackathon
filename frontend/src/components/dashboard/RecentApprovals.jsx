import { useEffect, useState } from "react";
import api from "../../services/api";
import { useNavigate } from "react-router-dom";

export default function RecentApprovals() {

  const [orders, setOrders] = useState([]);

  const navigate = useNavigate();

  async function loadOrders() {

    try {

      const res = await api.get("/purchase-orders");

      setOrders(
        res.data.filter(
          (o) => o.status === "PENDING"
        )
      );

    } catch (err) {

      console.log(err);

    }

  }

  useEffect(() => {

    loadOrders();

  }, []);

  return (

    <div className="rounded-3xl bg-white/5 border border-white/10 p-8">

      <h2 className="text-2xl font-bold mb-8">

        Pending Approvals

      </h2>

      <div className="space-y-5">

        {orders.length === 0 ? (

          <p className="text-zinc-400">

            No Pending Orders

          </p>

        ) : (

          orders.map((item)=>(

            <div
              key={item.id}
              className="rounded-2xl bg-white/5 p-5 flex justify-between items-center"
            >

              <div>

                <h3 className="font-semibold">

                  {item.product_name}

                </h3>

                <p className="text-gray-400">

                  {item.supplier}

                </p>

              </div>

              <button
                onClick={()=>navigate("/procurement")}
                className="rounded-xl bg-violet-600 px-5 py-2"
              >

                Review

              </button>

            </div>

          ))

        )}

      </div>

    </div>

  );

}