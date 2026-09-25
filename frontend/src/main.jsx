import React from "react";
import { createRoot } from "react-dom/client";
import Register from "../../server/frontend/src/components/Register/Register.jsx";
import "./style.css";
function App() {
  return <main><h1>Cars Dealership</h1><p>Dealer evaluation application</p><Register /></main>;
}
createRoot(document.getElementById("root")).render(<App />);
