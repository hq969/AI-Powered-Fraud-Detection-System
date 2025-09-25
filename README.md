# AI-Powered Fraud Detection System 🛡️

An **intelligent, real-time fraud detection system** that uses **LangGraph, LangChain agents, Kafka/AWS Kinesis, AWS Redshift, and Python** to detect, explain, and log anomalies in transactions.

---

## 🚀 Features

* **Real-Time Fraud Detection:** Streams transactions via **Kafka or AWS Kinesis**
* **Multi-Agent Processing:**

  * **Agent A:** Rule-based checks
  * **Agent B:** LLM-generated explanations in natural language
  * **Agent C:** Logs results into **Redshift** for analytics dashboards
* **Orchestration:** **LangGraph** manages agent workflows
* **Scalable & Cloud-Ready:** Designed for production on **AWS**
* **Analytics Integration:** Provides dashboards for monitoring fraud patterns

---

## 📂 Project Structure

```
fraud_detection/
├── agents/
│   ├── agent_a.py      # Rule-based fraud detection
│   ├── agent_b.py      # LLM explanations
│   └── agent_c.py      # Logging to Redshift
├── orchestrator/
│   └── langgraph_flow.py
├── streams/
│   └── kafka_consumer.py
├── utils/
│   └── redshift_client.py
├── run_agents.py
├── requirements.txt
└── .env.example
```

---

## 🏗 Architecture

```mermaid
flowchart LR
    T[Transaction Stream - Kafka/Kinesis] --> A[Agent A - Rule-Based Checks]
    A --> B[Agent B - LLM Explains Anomalies]
    B --> C[Agent C - Logs to Redshift]
    C --> D[Analytics Dashboards]
    subgraph Orchestration
        LangGraph manages A --> B --> C flow
    end
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/hq969/ai-powered-fraud-detection-system.git
cd ai-powered-fraud-detection-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` → `.env` and add your keys:

```
OPENAI_API_KEY=your_openai_api_key
REDSHIFT_HOST=your_redshift_host
REDSHIFT_PORT=5439
REDSHIFT_DB=your_db
REDSHIFT_USER=your_user
REDSHIFT_PASSWORD=your_password
KAFKA_BROKER_URL=localhost:9092
```

### 4. Run Locally

```bash
python run_agents.py
```

---

## 💡 Benefits

* Detects fraud in **real-time**, improving financial security
* Generates **human-readable explanations** for anomalies
* Logs results to **Redshift**, enabling dashboard analytics
* Easily extendable to new agents or streaming sources

---

## 👨‍💻 Author

Built by **Harsh Sonkar** ⚡

---
