import React, { useState } from 'react';

import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale);

// Example: y = 3x² + 2x + 1
function generatePolynomialData(fn, xRange = [-10, 10], step = 0.5) {
  const data = [];
  for (let x = xRange[0]; x <= xRange[1]; x += step) {
    const y = fn(x);
    data.push({ x, y });
  }
  return data;
}

const dataPoints = generatePolynomialData(x => 3 * x * x + 2 * x + 1);

const gdata = {
  datasets: [
    {
      label: 'y = 3x² + 2x + 1',
      data: dataPoints,
      borderColor: 'rgba(75,192,192,1)',
      fill: false,
      tension: 0.1,
      parsing: false,
    },
  ],
};

const options = {
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    x: {
      type: 'linear',
      position: 'bottom',
    },
  },
};

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
            <Line data={gdata} options={options} />;
        </div>
    );
}
function EqForm({onSubmit}){
    const [type, setType] = useState("equation");
    const [points, setPoints] = useState("");

    // Helper to call backend API
    async function callApi(payload) {
        // Replace with your backend endpoint
        const url = "/api/graph";
        try {
            await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });
        } catch (err) {
            // Handle error as needed
        }
    }

    // Handler for blur event
    const handleBlur = async (e) => {
        let payload = { type, color: e.target.form.color.value };
        if (type === "equation") {
            payload.eq = e.target.form.eq.value;
        } else {
            let pts = [];
            try {
                pts = JSON.parse(points);
            } catch {
                pts = points
                    .split("\n")
                    .map(line => line.trim())
                    .filter(Boolean)
                    .map(line => {
                        const [x, y] = line.split(",").map(Number);
                        return { x, y };
                    });
            }
            payload.points = pts;
        }
        await callApi(payload);
    };

    return (
        <form
            onSubmit={e => {
                e.preventDefault();
                const color = e.target.color.value;
                if (type === "equation") {
                    const eq = e.target.eq.value;
                    onSubmit({ type, eq, color });
                } else {
                    let pts = [];
                    try {
                        pts = JSON.parse(points);
                    } catch {
                        pts = points
                            .split("\n")
                            .map(line => line.trim())
                            .filter(Boolean)
                            .map(line => {
                                const [x, y] = line.split(",").map(Number);
                                return { x, y };
                            });
                    }
                    onSubmit({ type, points: pts, color });
                }
            }}
            style={{
                display: "flex",
                flexDirection: "column",
                gap: 0,
                alignItems: "flex-start",
                justifyContent: "flex-start"
            }}
        >
            <div style={{ display: "flex", flexDirection: "column", gap: 8, width: "100%" }}>
                <label style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", width: "100%" }}>
                    Type:
                    <select value={type} onChange={e => setType(e.target.value)} name="type" style={{ width: "100%" }}>
                        <option value="equation">Equation</option>
                        <option value="point">Point</option>
                    </select>
                </label>
                {type === "equation" ? (
                    <label style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", width: "70%" }}>
                        Eq:
                        <input
                            type="text"
                            name="eq"
                            placeholder="e.g. 3*x^2 + 2*x + 1"
                            required
                            style={{ width: "100%" }}
                            onBlur={handleBlur}
                        />
                    </label>
                ) : (
                    <label style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", width: "70%" }}>
                        Points:
                        <textarea
                            name="points"
                            placeholder='e.g. [{"x":1,"y":2},{"x":2,"y":4}] or one "x,y" per line'
                            rows={4}
                            value={points}
                            onChange={e => setPoints(e.target.value)}
                            required
                            style={{ width: "100%" }}
                            onBlur={handleBlur}
                        />
                    </label>
                )}
                <label style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", width: "30%", gap: 4 }}>
                    Color:
                    <input
                        type="color"
                        name="color"
                        defaultValue="#4bc0c0"
                        style={{ width: 32, height: 32, border: "none", background: "none", padding: 0 }}
                        aria-label="Pick a color for the graph"
                    />
                </label>
            </div>
        </form>
    )
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
            <EqForm onSubmit={(e) => {}}/>
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