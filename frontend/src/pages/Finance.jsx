import useFinance from "../hooks/useFinance";

export default function Finance() {

  const { finance, loading } = useFinance();

  if (loading) return <h2>Loading...</h2>;

  return (

    <div>

      <h1 className="text-4xl font-bold mb-8">

        Finance Dashboard

      </h1>

      <div className="grid grid-cols-4 gap-6">

        <div className="rounded-3xl bg-white/5 p-8">

          <p>Revenue</p>

          <h2 className="text-4xl mt-4">

            ₹{finance.total_revenue}

          </h2>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <p>Expense</p>

          <h2 className="text-4xl mt-4">

            ₹{finance.total_expense}

          </h2>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <p>Profit</p>

          <h2 className="text-4xl mt-4">

            ₹{finance.total_profit}

          </h2>

        </div>

        <div className="rounded-3xl bg-white/5 p-8">

          <p>Margin</p>

          <h2 className="text-4xl mt-4">

            {finance.profit_margin}%

          </h2>

        </div>

      </div>

    </div>

  );

}