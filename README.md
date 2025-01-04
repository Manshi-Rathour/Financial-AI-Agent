# Financial-AI-Analyst

Welcome to the **Financial AI Analyst**! This repository contains tools and applications that leverage AI agents for financial analysis and web search. The project includes two main components:

1. **`financial_agent.py`**: A Streamlit-based interactive application for querying financial data and news.
2. **`playground.py`**: A chatbot playground powered by the Phidata platform for experimenting with financial and web search AI agents.

## Features

### `financial_agent.py`
- A Streamlit application for financial analysis.
- Combines **Web Search Agent** and **Finance AI Agent** for robust query handling.
- Provides:
  - Real-time stock prices
  - Analyst recommendations
  - Company financial fundamentals
  - Latest financial news
- Responses are enriched with formatted text, including tables for structured data.
- Uses the **Groq** model and tools such as **DuckDuckGo** and **YFinance** for comprehensive responses.
- Clean, user-friendly interface for financial queries.

### `playground.py`
- A chatbot playground for interacting with AI agents.
- Includes:
  - **Finance AI Agent** for financial queries.
  - **Web Search Agent** for general web searches.
- Built with the Phidata platform, using the **Groq** model for intelligent, tool-empowered responses.
- Deployable as a standalone application via `phi.playground`.


## Prerequisites
- **Git:** <a href="https://git-scm.com/" target="_blank">Download and Install Git</a>
- **Groq:** <a href="https://groq.com/" target="_blank">Get free API key after login</a>
- **Phidata:** <a href="https://www.phidata.com/" target="_blank">Get free API key after login</a>
- **OpenAI:** <a href="https://openai.com/" target="_blank">OpenAI API key</a> (needed because Groq model internally uses this)

## Installation
To utilize Financial AI Analyst locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Manshi-Rathour/Financial-AI-Analyst
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd Financial-AI-Analyst
   ```
   
3. **Set Up a Virtual Environment**:
   Create and activate a virtual environment for dependency management:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   Install the necessary packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure API Keys**:
   Set up your API keys in a `.env` file. Create a `.env` file in the root directory and add the following line:
   ```env
   PHI_API_KEY="your-phidata-api-key"
   GROQ_API_KEY="your-groq-api-key"
   OPENAI_API_KEY="your-openai-api-key"
   ```

6. **Run the Application**:
- For Streamlit App:
   ```bash
   streamlit run financial_agent.py
   ```
- For Chatbot Playground:
   ```bash
   python playground.py
   ```
