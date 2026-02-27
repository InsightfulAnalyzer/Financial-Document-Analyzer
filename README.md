📊 Financial Document Analyzer (Refactored & Production-Ready Version)
📝 Project Overview

The Financial Document Analyzer is a multi-agent AI system built using CrewAI and served through a FastAPI backend.

The application allows users to upload financial documents (such as annual or quarterly reports) and receive structured insights including:

Document validation

Financial analysis

Risk assessment

Investment recommendations

The system simulates a team of financial experts — each agent has a defined responsibility, and tasks are executed sequentially to ensure logical information flow.

This version of the project represents a fully debugged, stabilized, and refactored implementation after resolving major dependency conflicts, runtime errors, architectural issues, and security flaws.

🐛 Major Issues Identified & How They Were Resolved

The original implementation contained multiple breaking issues at environment, framework, and code levels. Below is a summary of improvements.

1️⃣ Environment & Dependency Stabilization

The initial setup suffered from severe package conflicts and framework incompatibilities.

✔ Dependency Conflicts Resolved

Multiple version mismatches were identified involving:

onnxruntime

pydantic

click

openai

packaging

langchain

chromadb

These conflicts prevented the environment from building correctly.

✔ Framework Version Upgrade

The earlier CrewAI version caused internal incompatibilities.
The project was migrated to a stable CrewAI release, eliminating deep dependency issues and resolving import failures.

✔ Removal of crewai-tools

A critical incompatibility existed between crewai and crewai-tools.
Instead of forcing unstable combinations:

crewai-tools was completely removed.

Required tools were reimplemented manually inside tools.py.

This made the project:

More stable

Easier to maintain

Less dependent on third-party version chains

✔ Clean & Pinned Requirements

The requirements.txt file was cleaned and stabilized to prevent cascading dependency failures in future setups.

2️⃣ Code & Runtime Fixes

Once the environment was stable, multiple runtime errors were corrected.

✔ Import Fixes

Corrected invalid import paths after framework upgrades.

✔ LLM Initialization Error

Fixed a NameError where the llm variable was referenced before being properly initialized.

✔ Tool Refactoring

Custom tools were rewritten to properly inherit from BaseTool and follow correct structure compatible with CrewAI’s execution pipeline.

✔ FastAPI Stability

Resolved:

Multipart upload dependency issues

File handling cleanup logic

Sequential task execution stability

✔ Model Update

Deprecated model references were replaced with supported, current OpenAI models.

3️⃣ Prompt Engineering Overhaul

The original prompts were intentionally unprofessional and logically inconsistent.

This version includes:

Professional agent roles

Clear goals and responsibilities

Structured task descriptions

Logical data flow between agents

The execution pipeline now follows:

Document Verifier → Validates document type

Financial Analyst → Extracts insights

Risk Assessor → Evaluates exposure

Investment Advisor → Provides recommendations

Each task receives contextual input from the previous step to maintain consistency.

🛠 Setup & Installation

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2️⃣ Create & Activate Virtual Environment
python -m venv venv

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

The requirements file is fully stabilized to avoid dependency conflicts.

4️⃣ Configure Environment Variables

Create a .env file in the project root.

Add:

OPENAI_API_KEY=your_openai_api_key_here

⚠️ Never commit the .env file. It is excluded using .gitignore.

🚀 Running the Application

Start the server:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000
📄 Using the Analyzer

Open browser:

http://127.0.0.1:8000/docs

Expand POST /analyze

Click Try it out

Upload a PDF financial document

Click Execute

You will receive:

Structured financial analysis

Risk insights

Investment perspective

Agent activity is visible in the terminal logs.

🔐 API Key & Billing Information

This project uses the OpenAI API.

Requirements:

Valid OpenAI API key

Active billing enabled

Sufficient quota available

If billing is not configured, the API will return:

429 insufficient_quota

Ensure your OpenAI account has available credits.

🏗 Project Architecture
main.py      → FastAPI application & endpoint
agents.py    → Agent definitions (roles & LLM setup)
task.py      → Sequential task pipeline
tools.py     → Custom financial document tools
requirements.txt → Stabilized dependencies

The system uses a sequential CrewAI pipeline, ensuring structured data flow between agents.

📌 Key Improvements in This Version

Stable dependency environment

Removed unnecessary external tooling

Secure API key handling

Clean Git history

Professional prompt engineering

Structured multi-agent workflow

Improved FastAPI file handling

💡 Future Enhancements

Local LLM support (Ollama integration)

Model abstraction layer for provider switching

Advanced financial ratio extraction

Structured JSON output mode

Deployment via Docker