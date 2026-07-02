import { useState } from "react";
import "./App.css";
import { sendMessage } from "./services/api";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "👋 Hello! Ask me anything about your business.",
    },
  ]);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = {
      sender: "user",
      text: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;
    setMessage("");

    try {
      const response = await sendMessage(currentMessage);

      const aiMessage = {
        sender: "ai",
        text: JSON.stringify(response, null, 2),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "❌ Could not connect to backend.",
        },
      ]);
    }
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>AI COO</h2>

        <nav>
          <button>🏠 Dashboard</button>
          <button>📦 Inventory</button>
          <button>📈 Analytics</button>
          <button>💰 Finance</button>
          <button>🛒 Procurement</button>
          <button>🔔 Notifications</button>
        </nav>
      </aside>

      <main className="main">
        <header className="header">
          <h1>AI Business Operations Agent</h1>
        </header>

        <section className="cards">
          <div className="card">
            <h3>Revenue</h3>
            <h2>₹9,830</h2>
          </div>

          <div className="card">
            <h3>Profit</h3>
            <h2>₹2,430</h2>
          </div>

          <div className="card">
            <h3>Low Stock</h3>
            <h2>3</h2>
          </div>

          <div className="card">
            <h3>Pending Orders</h3>
            <h2>1</h2>
          </div>
        </section>

        <section className="chat">
          <div className="messages">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={msg.sender === "user" ? "user" : "ai"}
              >
                <pre>{msg.text}</pre>
              </div>
            ))}
          </div>

          <div className="inputArea">
            <input
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Ask your AI COO..."
              onKeyDown={(e) => {
                if (e.key === "Enter") handleSend();
              }}
            />

            <button onClick={handleSend}>Send</button>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;