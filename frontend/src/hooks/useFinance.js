import { useEffect, useState } from "react";
import api from "../services/api";

export default function useFinance() {

  const [finance, setFinance] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function load() {

      const res = await api.post("/chat", {

        message: "finance summary",

      });

      setFinance(res.data.results.finance.metrics);

      setLoading(false);

    }

    load();

  }, []);

  return {

    finance,

    loading,

  };

}