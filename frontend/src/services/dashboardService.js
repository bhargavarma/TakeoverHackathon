import API from "./authService";

export const getInventory = async () => {
  const res = await API.get("/inventory");
  return res.data;
};

export const runReview = async () => {
  const res = await API.post("/review/run");
  return res.data;
};

export const getPurchaseOrders = async () => {
  const res = await API.get("/purchase-orders");
  return res.data;
};