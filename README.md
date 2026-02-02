# 🌍 Time Agent – Agentic AI for Real-Time City Time

An **agentic AI system** that tells the **current local time of any city in the world** using a **tool-based architecture**, without relying on paid LLM APIs or hitting quota limits.

This project demonstrates **real agent design**, not just API calling.

---

## 🚀 Features

- 🌐 Get current time for **any city worldwide**
- 🧠 Intelligent **input normalization**
  - `newyork` → `New York`
  - Country names like `Japan` → default city (`Tokyo`)
- ⚡ **No API keys required**
- 💸 **100% free** (no billing, no quotas)
- 🔧 Tool-based agent architecture
- 🖥️ Works via **CLI**
- 🌐 Works via **Web UI (ADK)**

---

## 🧠 Why This Project?

Many “AI agents” unnecessarily use LLMs for deterministic tasks, causing:
- ❌ API quota issues (429 errors)
- ❌ Higher costs
- ❌ Slower responses

This project follows **industry best practices**:
- Use **tools** for deterministic data
- Use **LLMs only when reasoning is needed** (optional, future-ready)
- Build agents that are **scalable, reliable, and testable**

---

User Input
↓
City / Country Extraction
↓
Input Normalization
↓
Geocoding (OpenStreetMap)
↓
Offline Timezone Resolution (timezonefinder)
↓
Current Time Fetch (WorldTimeAPI)
↓
Agent Response

my_agent/
│
├── init.py
├── main.py # CLI runner
├── agent.py # Core agent logic & tools
├── city_timezone.py # Static cache (optional)
└── root_agent.py # ADK web agent


---

## 🛠️ Requirements

### System
- Python **3.9+**
- Linux / macOS / Windows / Google Cloud Shell

### Python Dependencies
Install all required packages:

bash
pip install requests timezonefinder google-adk 


Example
User: tell me time of pune
Agent: Current time in Pune is 05:47 PM

User: tell me time of newyork
Agent: Current time in New York is 07:26 AM

User: tell me time of japan
Agent: Current time in Tokyo is 09:56 PM

Exit with:
exit

🎯 Key Learnings & Concepts Demonstrated

Agentic AI design

Tool selection & orchestration

Input normalization & ambiguity handling

Offline timezone resolution

Robust error handling

CLI → Web agent conversion (ADK)

🔮 Future Enhancements

🤖 Optional LLM integration for intent parsing

🌍 Country disambiguation for multi-timezone regions

💾 Persistent caching (city → timezone)



_Upcomming commit will be having the web-based agentic AI which will behave like normal AI agents _
Yet its **hallucinating** the data and more precisely facing **API key expiry problem**.

