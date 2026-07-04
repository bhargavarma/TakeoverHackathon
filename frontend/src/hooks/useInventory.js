import { useEffect, useState } from "react";
import api from "../services/api";

export default function useInventory() {
  const [inventory, setInventory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadInventory() {
      try {
        const response = await api.post("/chat", {
          message: "show inventory",
        });

        setInventory(
          response.data.results.inventory.result
        );
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    loadInventory();
  }, []);

  return {
    inventory,
    loading,
  };
}