# 🤖 AgentInsight – Self-Evaluation Agent built with Agentforce (Salesforce Hackathon Demo)

AgentInsight is an autonomous agent created with Salesforce Agentforce that evaluates and scores the reasoning quality of other agents. It provides a trusted, internal mechanism to validate how clearly, safely, and effectively AI agents respond within business workflows.

## 🧠 Why?

As AI agents become more autonomous, it becomes critical to ensure the **trustworthiness and self-awareness** of their actions. AgentInsight was created to bring human-style quality control and introspection to AI-generated answers inside Salesforce.

## 💡 What It Does

- Agent receives a business-related prompt (e.g., customer question)
- Another Agentforce agent responds
- AgentInsight reviews the answer and scores it based on logic, confidence, and self-awareness
- All scores are logged in Salesforce and visualized using interactive dashboards

## 🛠️ Built With

Python 3.10, Plotly, Pandas, Salesforce Platform, Agentforce, Apex (mockup), HTML5, CSV

## 🔄 Potential Use Cases

- Internal agent QA reviews
- AI safety monitoring
- Evaluation of multi-agent collaboration in customer support

## 🔐 Limitations

This is a **functional prototype** with mock logic for Apex actions. With full API and Salesforce org integration, AgentInsight could become a true agent introspection framework.

## 📥 Output

- Evaluation scores stored in CSV
- Visuals generated with Plotly
- Ready for Lightning dashboard or Slack integration