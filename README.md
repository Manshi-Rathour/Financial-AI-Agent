# Financial-AI-Agent

## Installation
To utilize Financial AI Agent locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Manshi-Rathour/Financial-AI-Agent
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd Financial-AI-Agent
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
   To run the Streamlit app, use the following command:
   ```bash
   streamlit run financial_agent.py
   ```
