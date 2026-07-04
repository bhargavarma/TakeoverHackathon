import { useMemo, useState } from "react";
import useInventory from "../hooks/useInventory";
import { Search, Boxes } from "lucide-react";

export default function Inventory() {

  const { inventory, loading } = useInventory();

  const [search, setSearch] = useState("");

  const filteredInventory = useMemo(() => {

    return inventory.filter((item) =>
      item.name.toLowerCase().includes(search.toLowerCase())
    );

  }, [inventory, search]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-[70vh]">

        <div className="text-center">

          <div className="w-16 h-16 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin mx-auto"></div>

          <h2 className="mt-6 text-2xl font-bold">
            Loading Inventory...
          </h2>

        </div>

      </div>
    );
  }

  return (

    <div>

      <div className="flex justify-between items-center mb-10">

        <div>

          <h1 className="text-4xl font-bold">
            Inventory
          </h1>

          <p className="text-zinc-400 mt-2">
            Live Inventory from AI COO
          </p>

        </div>

        <div className="relative">

          <Search
            className="absolute left-4 top-4 text-zinc-500"
            size={20}
          />

          <input
            placeholder="Search products..."
            value={search}
            onChange={(e)=>setSearch(e.target.value)}
            className="pl-12 pr-5 py-3 rounded-xl bg-zinc-900 border border-zinc-700 outline-none w-80"
          />

        </div>

      </div>

      <div className="overflow-hidden rounded-3xl border border-zinc-800">

        <table className="w-full">

          <thead className="bg-zinc-900">

            <tr>

              <th className="text-left p-5">Product</th>

              <th className="text-left">Category</th>

              <th className="text-left">Supplier</th>

              <th className="text-center">Stock</th>

              <th className="text-center">Minimum</th>

              <th className="text-center">Status</th>

            </tr>

          </thead>

          <tbody>

            {filteredInventory.map((item)=>(

              <tr
                key={item.id}
                className="border-t border-zinc-800 hover:bg-white/5 transition"
              >

                <td className="p-5 flex items-center gap-3">

                  <Boxes size={18}/>

                  {item.name}

                </td>

                <td>{item.category}</td>

                <td>{item.supplier}</td>

                <td className="text-center font-bold">
                  {item.stock}
                </td>

                <td className="text-center">
                  {item.minimum_stock}
                </td>

                <td className="text-center">

                  {item.stock <= item.minimum_stock ? (

                    <span className="bg-red-500 px-4 py-2 rounded-full text-sm">

                      Low Stock

                    </span>

                  ) : (

                    <span className="bg-green-600 px-4 py-2 rounded-full text-sm">

                      Healthy

                    </span>

                  )}

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>

  );

}