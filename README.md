# Sheffield-Council-School-CatchmentBot-llm-groq-llama3
An LLM-powered AI assistant for analyzing Sheffield City Council’s school catchment zones using geospatial data, Groq-accelerated LLaMA 3, LangChain agents, and a Streamlit dashboard.

# 🏫 CatchmentBot AI – Sheffield School Catchment Planning with Groq + LLaMA 3

CatchmentBot AI is an intelligent assistant that transforms how school catchment zones are analyzed and optimized. Using geospatial data from **Sheffield City Council**, combined with **Groq-accelerated LLaMA 3** and **LangChain Agents**, this system enables urban planners and decision-makers to audit school catchments through natural language queries.

> 🤖 Built for smart, transparent, and scalable education planning.

---

## 🎯 Key Features

- 🔍 **Fairness Audit**  
  Flags catchment zones that are unusually small or large using interquartile range (IQR) analysis.

- 📍 **Overlap Detection**  
  Detects and quantifies overlapping zones using polygon intersection logic.

- 🚸 **Transport Burden Classification**  
  Estimates travel burden based on radius derived from area and classifies zones as Low, Medium, or High.

- 🛠️ **Planning Scenario Generator**  
  Suggests actions like "Shrink", "Merge", or "Split" for problematic catchment zones.

- 💬 **LLM-Powered Q&A**  
  Users can ask natural language questions like:  
  - *"Which zones are oversized?"*  
  - *"Are there any overlaps?"*  
  - *"Recommend restructuring steps."*

---

## 📂 Dataset Summary

**File:** `cleaned_catchments.geojson`  
**Source:** Sheffield City Council open data (converted and cleaned)

| catchment                    | shape_Area  | geometry (truncated)                                 |
|-----------------------------|-------------|------------------------------------------------------|
| Abbey Lane Primary School   | 2812758.7   | POLYGON(432704.2591 382129.091, ..., ...)           |
| Nether Edge Primary School  | 880129.76   | POLYGON(434152.8749 385479.5649, ..., ...)          |
| Byron Wood Primary Academy  | 1319155.95  | POLYGON(435362.2371 387861.9843, ..., ...)          |

Each polygon defines the spatial boundary of a school’s catchment area, with length, area, and geometry fields.

---

## 🧰 Full Tech Stack

| Layer         | Tool/Library              | Purpose                                               |
|---------------|---------------------------|--------------------------------------------------------|
| 💬 LLM        | Groq + Meta LLaMA 3 70B   | Ultra-fast reasoning and response generation           |
| 🧠 Agents     | LangChain Agents          | Routing and executing tools based on user intent       |
| 🌍 Spatial    | GeoPandas                 | Geospatial data loading, area computation, intersection|
| 🧮 Utilities  | NumPy, dotenv             | Area math, radius derivation, config management        |
| 🌐 Interface  | Streamlit                 | Lightweight web-based front-end                        |

---

## 📁 File Structure

```bash
catchmentbot-ai/
│
├── app.py                      # Streamlit frontend interface
├── geo_loader.py               # Loads and summarizes geojson data
├── catchment_tools.py          # All LLM tool functions (audit, overlaps, etc.)
├── catchment_agent.py          # Initializes LangChain + Groq agent
├── cleaned_catchments.geojson  # Geospatial input dataset
├── .env.example                # Environment variable config template
├── requirements.txt            # All required Python libraries
└── README.md                   # Project overview and instructions

