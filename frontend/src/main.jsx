import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import EQGraph from './EQGraph.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <EQGraph />
  </StrictMode>,
)
