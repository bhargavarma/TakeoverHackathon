import useInventory from "../hooks/useInventory";

export default function Inventory() {

  const { inventory, loading } = useInventory();

  if (loading) {
    return (
      <div className="text-xl">
        Loading Inventory...
      </div>
    );
  }

  return (
    <div>

      <div className="flex items-center justify-between mb-8">

        <h1 className="text-4xl font-bold">
          Inventory
        </h1>

      </div>

      <div className="grid grid-cols-3 gap-6">

        {inventory.map((item) => (

          <div
            key={item.name}
            className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-6"
          >

            <h2 className="text-2xl font-semibold">

              {item.name}

            </h2>

            <div className="mt-6 space-y-2">

              <p>

                Stock :
                <strong>
                  {" "}
                  {item.stock}
                </strong>

              </p>

              <p>

                Minimum :
                <strong>
                  {" "}
                  {item.minimum_stock}
                </strong>

              </p>

              <p>

                Supplier :
                <strong>
                  {" "}
                  {item.supplier}
                </strong>

              </p>

            </div>

            <div className="mt-6">

              {item.stock <= item.minimum_stock ? (

                <span className="rounded-full bg-red-500 px-4 py-2">

                  Low Stock

                </span>

              ) : (

                <span className="rounded-full bg-green-600 px-4 py-2">

                  Healthy

                </span>

              )}

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}