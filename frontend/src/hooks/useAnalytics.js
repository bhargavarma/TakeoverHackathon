import { useEffect, useState } from "react";
import api from "../services/api";

export default function useAnalytics() {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const res = await api.post("/chat", {
          message: "analytics summary",
        });

        setAnalytics(
          res.data.results.analytics.summary
        );
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  return {
    analytics,
    loading,
  };
}