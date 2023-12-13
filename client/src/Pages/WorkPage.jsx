import React, { useState } from "react";

const WorkPage = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleGenerate = () => {
    // Logic for generating something using inputValue
    console.log(`Generating with input: ${inputValue}`);
  };

  const handleLogout = () => {
    // Logic for logging out
    console.log("Logging out...");
  };

  return (
    <div>
      <header style={{ display: "flex", justifyContent: "flex-end", padding: "1em", backgroundColor: "skyblue" }}>
        <button onClick={handleLogout} className="btn btn-primary">Logout</button>
      </header>
      
      <main style={{ display: "flex", flexDirection: "column", alignItems: "center", marginTop: "2em" }}>
        <input type="text" value={inputValue} onChange={handleInputChange} />
        <button onClick={handleGenerate} className="btn btn-primary">Generate</button>
      </main>
    </div>
  );
};

export default WorkPage;
