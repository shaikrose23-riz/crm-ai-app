import React, { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");   
  const [formData, setFormData] = useState({   
    hcp_name: "",
    date: "",
    sentiment: "",
    notes: ""
  });

  const sendMessage = async () => {
    try {

          console.log("Sending:", message);

      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: message
      });

      console.log("Response:", res.data);

      setFormData(res.data);

    } catch (error) {
      console.error("API Error:", error);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      
      {/* LEFT SIDE FORM */}
      <div style={{ width: "50%", padding: "20px" }}>
        <h2>Interaction Form</h2>

        <input placeholder="HCP Name" value={formData.hcp_name} readOnly /><br/><br/>
        <input placeholder="Date" value={formData.date} readOnly /><br/><br/>
        <input placeholder="Sentiment" value={formData.sentiment} readOnly /><br/><br/>
        <textarea placeholder="Notes" value={formData.notes} readOnly />

      </div>

      {/* RIGHT SIDE CHAT */}
      <div style={{ width: "50%", padding: "20px" }}>
        <h2>AI Assistant</h2>

        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type message..."
        />

        <button onClick={sendMessage}>Send</button>
      </div>

    </div>
  );
}

export default App;