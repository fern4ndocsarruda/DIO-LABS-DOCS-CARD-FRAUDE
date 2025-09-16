# Copilot Instructions for AI Coding Agents

## Project Overview
This project is a Python backend service for analyzing credit card information using Azure Document Intelligence. The codebase is organized by service responsibility, with configuration and utility logic separated for clarity and maintainability.

## Key Components
- `src/app.py`: Main application entry point (not shown, but typically orchestrates service usage).
- `src/services/credit_card_service.py`: Contains `analize_credit_card(card_url)`, which uses Azure's Document Intelligence API to extract credit card details from a document URL.
- `src/services/blob_service.py`: (Not shown) Presumed to handle Azure Blob Storage interactions.
- `src/ultils/Config.py`: Centralizes configuration, including Azure API keys and endpoints.

## Patterns & Conventions
- **Configuration**: All secrets and endpoints are accessed via the `Config` class in `ultils/Config.py`. Do not hardcode credentials.
- **Service Layer**: Each external integration (e.g., Azure Document Intelligence, Blob Storage) has its own service module under `src/services/`.
- **Return Values**: Service functions return dictionaries with extracted or processed data, not raw API responses.
- **Imports**: Use absolute imports from the `src` root (e.g., `from ultils.Config import Config`).

## External Dependencies
- Azure SDKs: `azure-core`, `azure-ai-documentintelligence` (see `requirements.txt`).
- All dependencies must be listed in `src/requirements.txt`.

## Developer Workflows
- **Install dependencies**: `pip install -r src/requirements.txt`
- **Run the app**: (Assumed) `python src/app.py`
- **Add new services**: Place new integrations in `src/services/` and follow the pattern of using configuration from `ultils/Config.py`.

## Example: Credit Card Analysis
```python
from services.credit_card_service import analize_credit_card
result = analize_credit_card('https://example.com/card-image.jpg')
# result: {'card_name': ..., 'card_number': ..., 'expiry_date': ..., 'bank_name': ...}
```

## Special Notes
- The project uses a misspelled folder name `ultils` (not `utils`).
- All configuration is centralized; update `Config.py` for any new secrets or endpoints.
- No test or build automation scripts are present; add as needed for your workflow.

---
For questions about project structure or patterns, review the service modules and `Config.py` for examples.
