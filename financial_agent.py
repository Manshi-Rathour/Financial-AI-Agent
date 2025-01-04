import streamlit as st
import openai
import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

# Combining both the agents
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

# Streamlit UI

st.set_page_config(
    page_title="Financial AI Analyst",
    page_icon="📈",
)

st.title("Financial AI Analyst 📈")
st.markdown('<p style="color: yellow;">Ask me anything about stocks, financial news, or analyst recommendations!</p>', unsafe_allow_html=True)

# User input
user_input = st.text_input("Enter your query:", "")

# Response display
if user_input:
    with st.spinner('Processing your request...'):
        try:
            # Get response from the multi-agent system
            response_generator = multi_ai_agent.run(user_input, stream=True)

            # Initialize response string
            response = ""

            for part in response_generator:
                # Check if part has text content
                if isinstance(part, str):
                    response += part
                elif hasattr(part, 'content'):
                    response += part.content  # Ensure content is added if available

            print("Accumulated Response:", response)

            # If the response is empty, handle that case
            if not response:
                st.write("No meaningful response received. Please check the query or the agent configuration.")
            else:
                # Ensure the response is a string and render it in Streamlit
                st.markdown(response)  # Use st.markdown for formatted text

        except Exception as e:
            st.error(f"Error occurred: {e}")
