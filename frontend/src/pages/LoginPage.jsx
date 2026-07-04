import { useState } from "react";
import { login } from "../services/authService";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
  try {
    console.log("Trying login...");

    const data = await login(email.trim(), password);

    console.log(data);

    window.location.replace("/");
  } catch (error) {
    console.error(error);

    if (error.response) {
      alert(error.response.data.detail);
    } else {
      alert("Unable to connect to backend.");
    }
  }
};

  return (
    <div className="min-h-screen bg-[#07070d] flex items-center justify-center">

      <div className="w-[420px] rounded-3xl bg-[#12121a] p-10 border border-zinc-800">

        <h1 className="text-4xl font-bold text-white mb-2">
          AI COO
        </h1>

        <p className="text-zinc-400 mb-8">
          Business Operating System
        </p>

        <input
          className="w-full rounded-xl bg-zinc-900 border border-zinc-700 px-4 py-3 text-white mb-4"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          className="w-full rounded-xl bg-zinc-900 border border-zinc-700 px-4 py-3 text-white mb-6"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full py-3 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-500 text-white font-semibold"
        >
          Login
        </button>

      </div>

    </div>
  );
}