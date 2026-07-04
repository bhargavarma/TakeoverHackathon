import { useEffect, useState } from "react";
import api from "../services/api";

export default function useProcurement() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  async function loadOrders() {
    try {
      const response = await api.post("/chat", {
        message: "procurement recommendations",
      });

      setOrders(
        response.data.results.procurement.recommendations || []
      );
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadOrders();
  }, []);

  return {
    orders,
    loading,
    refresh: loadOrders,
  };
}