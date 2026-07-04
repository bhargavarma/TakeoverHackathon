import useAnalytics from "../hooks/useAnalytics";

export default function Analytics() {

  const { analytics, loading } = useAnalytics();

  if (loading) return <h2>Loading...</h2>;

  return (

    <div>

      <h1 className="text-4xl font-bold mb-8">

        Business Analytics

      </h1>

      <div className="grid grid-cols-2 gap-6">

        <div className="rounded-3xl bg-white/5 p-8">

          <h2>Total Revenue</h2>

          <h1 className="text-5xl mt-5">

            ₹{analytics.total_revenue}

          </h1>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <h2>Total Orders</h2>

          <h1 className="text-5xl mt-5">

            {analytics.total_orders}

          </h1>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <h2>Total Profit</h2>

          <h1 className="text-5xl mt-5">

            ₹{analytics.total_profit}

          </h1>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <h2>Best Seller</h2>

          <h1 className="text-3xl mt-5">

            {analytics.best_selling_product.product}

          </h1>

        </div>

      </div>

    </div>

  );

}