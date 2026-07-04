import { useEffect, useState } from "react";
import api from "../services/api";

export default function useNotifications() {
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const res = await api.post("/chat", {
          message: "show latest notifications",
        });

        setNotifications(
          res.data.results.notifications?.notifications || []
        );
      } catch (err) {
        console.log(err);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  return {
    notifications,
    loading,
  };
}