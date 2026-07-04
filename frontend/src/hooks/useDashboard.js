import { useEffect, useState } from "react";
import api from "../services/api";

export default function useDashboard() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const response = await api.post("/chat", {
          message: "business summary",
        });

        setData(response.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  return {
    loading,
    data,
  };
}