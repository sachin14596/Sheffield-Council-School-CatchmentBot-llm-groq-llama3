from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Import your tools
from catchment_tools import audit_fairness, find_overlaps, transport_load, scenario_suggest

load_dotenv()

# Initialize LLM (Groq)
llm = ChatGroq(model="llama3-70b-8192", temperature=0.3)

# Define tools
tools = [
    Tool(name="audit_fairness", func=audit_fairness, description="Analyze fairness of zones based on size"),
    Tool(name="find_overlaps", func=find_overlaps, description="Find overlapping catchment zones"),
    Tool(name="transport_load", func=transport_load, description="Estimate transport burden based on zone size"),
    Tool(name="scenario_suggest", func=scenario_suggest, description="Suggest possible planning scenarios for catchment zones")
]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Function to run the agent
def run_catchment_agent(question: str):
    return agent.run(question)
