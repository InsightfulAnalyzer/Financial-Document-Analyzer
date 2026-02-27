import os
from typing import Type

from crewai.tools import BaseTool  # type: ignore
from pydantic import BaseModel, Field  # type: ignore

try:
    from pypdf import PdfReader  # type: ignore
except ImportError:
    from PyPDF2 import PdfReader  # type: ignore


class ReadFinancialDocumentInput(BaseModel):
    path: str = Field(
        default="data/sample.pdf",
        description="Absolute or relative path to the financial PDF document.",
    )


class ReadFinancialDocumentTool(BaseTool):
    name: str = "read_financial_document"
    description: str = "Read and return text content from a financial PDF document."
    args_schema: Type[BaseModel] = ReadFinancialDocumentInput

    def _run(self, path: str = "data/sample.pdf") -> str:
        if not path:
            return "No file path provided."

        if not os.path.exists(path):
            return f"File not found: {path}"

        reader = PdfReader(path)
        pages = []
        for page in reader.pages:
            text = page.extract_text() or ""
            cleaned = " ".join(text.split())
            if cleaned:
                pages.append(cleaned)

        if not pages:
            return "No readable text found in the provided PDF."

        return "\n".join(pages)


class InvestmentTool(BaseTool):
    name: str = "analyze_investment"
    description: str = "Provide a basic investment perspective from extracted financial text."

    def _run(self, financial_document_data: str) -> str:
        processed_data = " ".join((financial_document_data or "").split())
        if not processed_data:
            return "No financial data provided for investment analysis."
        return "Investment analysis functionality to be implemented."


class RiskTool(BaseTool):
    name: str = "create_risk_assessment"
    description: str = "Provide a basic risk assessment from extracted financial text."

    def _run(self, financial_document_data: str) -> str:
        if not (financial_document_data or "").strip():
            return "No financial data provided for risk assessment."
        return "Risk assessment functionality to be implemented."
