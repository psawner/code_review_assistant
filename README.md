# AI-Powered Code Review Assistant

An intelligent AI-driven code review system that automatically analyzes GitHub pull requests in real-time, detects security vulnerabilities, performance issues, bugs, and code smells, then posts actionable review comments directly on the PR.

---

# Problem Statement

Developers spend significant time manually reviewing pull requests, and critical issues like security vulnerabilities, performance bottlenecks, and logical bugs are often missed.

This project automates the code review workflow using AI + rule-based analysis to improve development speed, consistency, and code quality.

---

# Features

## Real-Time GitHub PR Review
- Automatically listens to GitHub Pull Request events using webhooks.
- Fetches real changed code from PRs.

## AI-Powered Analysis
Uses LLMs via LangChain + Groq to analyze:
- Security vulnerabilities
- Performance bottlenecks
- Logical bugs
- Code maintainability issues

## Rule-Based Detection Engine
Detects common issues instantly using regex/rule-based checks:
- Hardcoded passwords
- `eval()` usage
- Debug print statements
- TODO/FIXME comments

## Severity Scoring System
Assigns severity levels:
- HIGH
- MEDIUM
- LOW

Calculates overall PR risk score.

## Inline GitHub PR Comments
Automatically posts review comments directly on changed lines inside GitHub Pull Requests.

## Streamlit Analytics Dashboard
Interactive dashboard displaying:
- Reviewed PRs
- Risk scores
- Total issues
- Severity distribution
- Detailed findings

---

# Tech Stack

## Backend
- FastAPI
- Python

## AI/LLM
- LangChain
- Groq LLM

## Git Integration
- GitHub Webhooks
- PyGithub

## Dashboard
- Streamlit
- Pandas

---

# Architecture

```text
GitHub Pull Request
        ↓
GitHub Webhook
        ↓
FastAPI Backend
        ↓
Fetch PR Diff via GitHub API
        ↓
Rule-Based Analysis
        ↓
AI Review Engine (Groq + LangChain)
        ↓
Severity Scoring
        ↓
Inline PR Comments
        ↓
Store Review Data
        ↓
Streamlit Dashboard
```

---

# Project Structure

```text
code_review_assistant/
│
├── app.py
├── ui.py
├── requirements.txt
│
├── src/
│   ├── analyzers/
│   │   └── rule_based_checker.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── data/
│   │   └── reviews.json
│   │
│   ├── model/
│   │   └── llm.py
│   │
│   ├── services/
│   │   ├── ai_review_service.py
│   │   ├── github_service.py
│   │   └── storage_service.py
│   │
│   ├── utils/
│   │   ├── severity.py
│   │   └── file_filter.py
│   │
│   └── webhook/
│       └── github_webhook.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/psawner/code_review_assistant

cd code_review_assist
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

GITHUB_TOKEN=your_github_token
```

---

# Running FastAPI Server

```bash
uvicorn app:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# Running Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

# GitHub Webhook Setup

## Install ngrok

Download:
https://ngrok.com/download

Run:

```bash
ngrok http 8000
```

Copy generated public URL.

Example:

```text
https://abcd1234.ngrok-free.app
```

---

## Add GitHub Webhook

GitHub Repository → Settings → Webhooks → Add Webhook

Payload URL:

```text
https://your-ngrok-url/github/webhook
```

Content Type:

```text
application/json
```

Select Event:
- Pull Requests

---

# Example Workflow

1. Developer opens Pull Request
2. GitHub webhook triggers FastAPI backend
3. System fetches changed files
4. Rule-based engine analyzes code
5. AI engine reviews code diff
6. Severity score generated
7. Inline comments posted on PR
8. Dashboard updated automatically

---

# Example Issues Detected

## Security
- Hardcoded credentials
- Unsafe `eval()` usage

## Performance
- Inefficient loops
- Repeated DB/API calls

## Bugs
- Potential null reference
- Incorrect condition handling

## Code Smells
- Debug statements
- TODO/FIXME comments

---

# Future Improvements

- Async background processing
- Multi-language support
- CI/CD integration
- Vector database for repository memory
- Repository-wide context awareness
- AI caching system
- Team analytics dashboard
- Slack/Discord notifications

---

# Demo Highlights

- Real-time GitHub integration
- Automated AI pull request review
- Inline code review comments
- Risk scoring system
- Live analytics dashboard

---

# Contributors

- Piyush Kumar

---

# License

MIT License