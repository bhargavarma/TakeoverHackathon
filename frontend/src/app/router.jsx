import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "../components/layout/Layout";

import Dashboard from "../pages/Dashboard";
import Inventory from "../pages/Inventory";
import Procurement from "../pages/Procurement";
import Analytics from "../pages/Analytics";
import Finance from "../pages/Finance";
import Notifications from "../pages/Notifications";
import Settings from "../pages/Settings";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="/inventory" element={<Inventory />} />
          <Route path="/procurement" element={<Procurement />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/finance" element={<Finance />} />
          <Route path="/notifications" element={<Notifications />} />
          <Route path="/settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}