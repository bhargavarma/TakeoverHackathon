import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function login(email, password) {
  const response = await API.post("/auth/login", {
    email,
    password,
  });

  localStorage.setItem(
    "token",
    response.data.access_token
  );

  return response.data;
}

export function logout() {
  localStorage.removeItem("token");
}

export function isAuthenticated() {
  return localStorage.getItem("token") !== null;
}

export default API;