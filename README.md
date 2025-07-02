# creditrust-complaint-insights-chatbot

**Intelligent Complaint Analysis for Financial Services**  
_Building a RAG-Powered Chatbot to Turn Customer Feedback into Actionable Insights_

---

## 📌 Overview

CrediTrust Financial is a mobile-first digital finance company serving over **500,000 users** across East Africa. With offerings in:

- 💳 Credit Cards  
- 🧾 Personal Loans  
- 🛒 Buy Now, Pay Later (BNPL)  
- 🏦 Savings Accounts  
- 💸 Money Transfers  

...the company receives thousands of customer complaints monthly. These complaints are a goldmine of insights — if only they could be efficiently analyzed.

### 🚀 Project Goal

This project delivers an **internal AI assistant** that allows team members to ask plain-English questions like:

> “Why are people unhappy with BNPL lately?”

And instantly get back grounded, contextual answers generated from **real complaint narratives** using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 💡 Why This Matters

Internal teams at CrediTrust face serious pain points:

- **Support** teams are buried under complaint volume  
- **Product Managers** waste hours searching for patterns  
- **Compliance** is reactive, not proactive  
- **Executives** lack visibility into real customer pain points  

This tool addresses these issues by letting anyone in the company — not just data analysts — query complaint data in seconds.

---

## ⚙️ How It Works

### 🔍 **RAG Architecture**

1. **Preprocessing**
   - Clean and filter CFPB complaint narratives
   - Focus on 5 core financial product types
2. **Embedding**
   - Split long text into chunks
   - Embed using `sentence-transformers/all-MiniLM-L6-v2`
3. **Indexing**
   - Store embeddings in a FAISS vector database
   - Preserve metadata like product and company
4. **Retrieval + Generation**
   - Embed user query → Retrieve top-k relevant chunks
   - Send context to an LLM via a custom prompt
   - Return a concise, evidence-backed answer
5. **Interface**
   - Built with **Streamlit**
   - Shows answer + retrieved sources for transparency

---

## 📊 Dataset

- **Source:** Consumer Financial Protection Bureau (CFPB) Public Complaints Dataset  
- **Focus Fields:**
  - `consumer_complaint_narrative`
  - `product`, `company`
  - `issue`, `submitted_via`, `date`

---

## 📁 Project Structure



---

## 📈 KPIs for Success

- ⏱️ **Reduce issue detection time** from days to minutes  
- 🧑‍💼 **Empower non-technical teams** to self-serve answers  
- 🧭 **Proactive issue detection** across products

---

## 🧪 Example Questions

| Question | Answered By |
|---------|-------------|
| Why do BNPL users complain the most? | Complaint narratives |
| What issues are most common in savings accounts? | Text chunks + LLM |
| Are there signs of fraud in credit card complaints? | Retrieved context |
| How do personal loan complaints vary by company? | Metadata filtering |

---

## 🖥️ Running the App

### 1. Install Dependencies
```bash
pip install -r requirements.txt


## 🤝 Contributing
Want to improve chunking strategies, try out new LLMs, or enhance UI trust features? Pull requests are welcome.

---

Would you like:
- A downloadable `.md` file of this?
- Help converting this into a `README.pdf` or HTML landing page?
- A badge set (e.g. for Streamlit, Python version, Hugging Face, etc.)?

