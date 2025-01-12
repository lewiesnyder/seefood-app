# SeeFood App

A Python implementation of the "SeeFood" app from HBO's Silicon Valley series. This app classifies images as either "Hotdog" or "Not Hotdog" using Ollama for inference.

## Requirements

- Python 3.11+
- Poetry for dependency management
- Ollama installed locally

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Set up environment variables:
Create a `.env` file with:
```
OLLAMA_BASE_URL=http://localhost:11434
```

3. Run the application:

Start the FastAPI server:
```bash
poetry run uvicorn app.main:app --reload
```

Start the Streamlit UI:
```bash
poetry run streamlit run app/main.py
```

## Project Structure

- `app/main.py`: Main FastAPI application
- `app/models/hotdog_classifier.py`: Image classification model
- `app/utils/image_utils.py`: Image processing utilities
- `app/tests/`: Test files 