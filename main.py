# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException # type: ignore
import os
import uuid

from crewai import Crew, Process # type: ignore
from agents import (
    financial_analyst,
    verifier,
    investment_advisor,
    risk_assessor
)
from task import (
    verification,
    analyze_financial_document,
    investment_analysis,
    risk_assessment
)

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    financial_crew = Crew(
        agents=[
            verifier,
            financial_analyst,
            investment_advisor,
            risk_assessor
        ],
        tasks=[
            verification,
            analyze_financial_document,
            investment_analysis,
            risk_assessment
        ],
        process=Process.sequential,
    )

    result = financial_crew.kickoff(
        inputs={
            "query": query,
            "file_path": file_path
        }
    )
    return result


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Provide financial analysis and investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)