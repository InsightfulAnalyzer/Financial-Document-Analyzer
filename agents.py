## Importing libraries and files
import os
# agents.py

from dotenv import load_dotenv # type: ignore
load_dotenv()

from crewai import Agent, LLM # type: ignore
from tools import ReadFinancialDocumentTool


# Initialize LLM
llm = LLM(
    model="ollama/llama3",
    temperature=0.3,
)

# Financial Analyst
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide structured financial analysis based on user query and financial documents.",
    backstory="Experienced CFA professional with expertise in equity research and financial modeling.",
    verbose=True,
    memory=True,
    tools=[ReadFinancialDocumentTool()],
    llm=llm
)

# Verifier
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the uploaded document is a valid financial report.",
    backstory="Compliance specialist ensuring documents are financial in nature.",
    verbose=True,
    memory=True,
    tools=[ReadFinancialDocumentTool()],
    llm=llm
)

# Investment Advisor
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide buy/hold/sell recommendation based on financial analysis.",
    backstory="Portfolio manager with expertise in equity valuation and capital markets.",
    verbose=True,
    memory=True,
    tools=[ReadFinancialDocumentTool()],
    llm=llm
)

# Risk Assessor
risk_assessor = Agent(
    role="Risk Assessment Expert",
    goal="Evaluate financial and market risks based on document insights.",
    backstory="Risk management professional specializing in financial risk analysis.",
    verbose=True,
    memory=True,
    tools=[ReadFinancialDocumentTool()],
    llm=llm
)