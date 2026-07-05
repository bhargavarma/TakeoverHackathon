import { useEffect, useState } from "react";
import api from "../services/api";

export default function useProcurement() {

  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  async function loadOrders() {

    try {

      const res = await api.get("/purchase-orders");

      setOrders(res.data);

    } catch (err) {

      console.error(err);

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    loadOrders();

  }, []);

  async function approve(id) {

    await api.post(`/purchase-orders/${id}/approve`);

    loadOrders();

  }

  async function reject(id) {

    await api.post(`/purchase-orders/${id}/reject`);

    loadOrders();

  }

  return {

    loading,
    orders,
    approve,
    reject,
    refresh: loadOrders,

  };

}