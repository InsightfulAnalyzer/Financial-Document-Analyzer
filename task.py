# task.py

from crewai import Task # type: ignore
from agents import (
    financial_analyst,
    verifier,
    investment_advisor,
    risk_assessor
)
from tools import ReadFinancialDocumentTool


verification = Task(
    description=(
        "Verify whether the document located at {file_path} is a financial document. "
        "Respond in context of the user request: {query}."
    ),
    expected_output="State whether document is financial with explanation.",
    agent=verifier,
    tools=[ReadFinancialDocumentTool()],
    async_execution=False
)


analyze_financial_document = Task(
    description=(
        "Analyze the financial document at {file_path}. "
        "Based on the user's query: {query}, extract key financial metrics "
        "such as revenue, profit, growth rate, and liabilities."
    ),
    expected_output="Provide structured financial analysis.",
    agent=financial_analyst,
    tools=[ReadFinancialDocumentTool()],
    async_execution=False
)


investment_analysis = Task(
    description=(
        "Based on financial insights from {file_path}, respond to: {query}. "
        "Provide investment recommendation with reasoning."
    ),
    expected_output="Provide Buy/Hold/Sell recommendation with justification.",
    agent=investment_advisor,
    tools=[ReadFinancialDocumentTool()],
    async_execution=False
)


risk_assessment = Task(
    description=(
        "Evaluate financial and market risks from {file_path}. "
        "Respond considering the user query: {query}."
    ),
    expected_output="Provide structured risk assessment.",
    agent=risk_assessor,
    tools=[ReadFinancialDocumentTool()],
    async_execution=False
)
