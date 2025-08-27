# 📘 Custom Web Search Tool

## 🚀 Overview  
This project implements a **Custom Web Search Tool** using the **Tavily API**, integrated with the **OpenAI Agents SDK**.  
The tool allows an AI Agent to fetch real-time web results and use them for answering user queries.  
It also supports **session-based memory** so the agent can remember previous conversation context.  

---

## 🎯 Objectives  
- Explore Tavily API documentation.  
- Implement a simple search tool that fetches results from Tavily.  
- Integrate the tool with an AI Agent.  
- Ensure the tool can be called by the agent to answer user queries with context.  

---

## ⚙️ How It Works  
1. **User enters a query** → handled by `main.py`.  
2. **Agent checks if web search is needed** → triggers `web_search_tool`.  
3. **Tavily API fetches results** → structured as `url, title, content`.  
4. **Agent summarizes & returns** → user gets an easy-to-read answer.  
5. **SQLiteSession stores context** → agent remembers previous conversations.  

---

## 🧪 Testing Queries  

1. **Who is Lionel Messi?**  
2. **What is his age?**  (tests memory & context)  
3. **Tell me about the latest iPhone features.**  
4. **Give me the top articles on Pakistan cricket in the last week.**  
5. **Get the latest population statistics of New York City.**  
6. **Find articles on renewable energy and provide URLs.**  

---

## 📸 Sample: Logs / Demonstration  

### Figure 1: Messi Query  
![Log Image](/Logs/Log1.PNG)

> **Description:** Shows the bot fetching biographical details about Lionel Messi using the `web_search_tool`.  

### Figure 2: Contextual Follow-up  
![Log Image](/Logs/Log2.PNG)

> **Description:** Demonstrates session-based memory, where the bot understands "his" refers to Lionel Messi from the previous query.  

### Figure 3: iPhone Features  
![Log Image](/Logs/Log3.PNG)

> **Description:** Shows the bot retrieving and summarizing the latest iPhone features from real-time sources.  

### Figure 4: Pakistan Cricket Articles  
![Log Image](/Logs/Log4.PNG)

> **Description:** Displays multiple cricket-related articles fetched via Tavily API.  

### Figure 5: NYC Population Statistics  
![Log Image](/Logs/Log5.PNG)

> **Description:** Shows real-time population statistics retrieved from authoritative sources.  

### Figure 6: Renewable Energy Articles  
![Log Image](/Logs/Log6.PNG)  

> **Description:** Provides multiple articles on renewable energy with direct URLs.  

---

## ✅ Conclusion  
This project successfully:  
- Implements a custom Tavily-powered search tool.  
- Integrates it with an AI Agent using OpenAI Agents SDK.  
- Provides real-time, contextual, and memory-enabled answers.  

