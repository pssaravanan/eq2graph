import React, { useState } from "react";

// Dummy Graph Component
function Graph({ data }) {
    return (
        <div style={{
            background: "#f0f4fa",
            borderRadius: 8,
            height: "100%",
            display: "flex",
            alignItems: "center",
            justifyContent: "center"
        }}>
            <div>
                <h3>Graph Output</h3>
                <pre>{JSON.stringify(data, null, 2)}</pre>
            </div>
        </div>
    );
}

// Playground Component
function Playground({ onRun }) {
    const [input, setInput] = useState("");

    const handleRun = () => {
        // Simulate parsing input to data
        let data;
        try {
            data = JSON.parse(input);
        } catch {
            data = { error: "Invalid JSON" };
        }
        onRun(data);
    };

    return (
        <div style={{
            background: "#fff",
            borderRadius: 8,
            padding: 16,
            height: "100%",
            boxSizing: "border-box",
            display: "flex",
            flexDirection: "column",
            class: 'text-3xl font-bold underline'
        }}>
            <h3>Playground</h3>
            <textarea
                style={{ flex: 1, marginBottom: 8, resize: "none" }}
                value={input}
                onChange={e => setInput(e.target.value)}
                placeholder='Enter JSON data for the graph...'
            />
            <button onClick={handleRun} style={{ alignSelf: "flex-end" }}>
                Run
            </button>
        </div>
    );
}

// Main App Layout
export default function EQGraph() {
    const [graphData, setGraphData] = useState({});

    return (
        <div style={{
            position: "fixed",
            inset: 0,
            display: "flex",
            height: "100vh",
            width: "100vw",
            background: "#e9eef6",
            padding: 32,
            boxSizing: "border-box"
        }}>
            <div style={{ flex: 1, marginRight: 16, minWidth: 0 }}>
                <Playground onRun={setGraphData} />
            </div>
            <div style={{ flex: 2, minWidth: 0 }}>
                <Graph data={graphData} />
            </div>
        </div>
    );
}