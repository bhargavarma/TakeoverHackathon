import { useEffect, useState } from "react";
import api from "../services/api";

export default function useDashboard() {

  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    load();
  }, []);

  async function load() {
    try {
      const res = await api.get("/dashboard");
      setData(res.data);
    } catch (e) {
      console.log(e);
    } finally {
      setLoading(false);
    }
  }

  return {
    loading,
    data,
  };
}