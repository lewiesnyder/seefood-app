# SeeFood App

A Python implementation of the "SeeFood" app from HBO's Silicon Valley series. This app classifies images as either "Hotdog" or "Not Hotdog" using Ollama for inference.

## This project was create using [Cursor AI](https://www.cursor.com/)

## Requirements

- Python 3.11+
- Poetry for dependency management
- [Ollama](https://ollama.com/) runningwith [llama3.2-vision](https://ollama.com/library/llama3.2-vision) model

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

Start the Streamlit UI:
```bash
poetry run python run_ui.py
```
or 
```bash
poetry run streamlit run app/main.py
```

Optionally, start the FastAPI server:
```bash
poetry run python run_api.py
```
or 
```bash
poetry run uvicorn app.main:app --reload
```
The api isn't used by the app. The docs can be viewed at `http://localhost:8000/docs`.

## Project Structure
- `app/main.py`: Main FastAPI and Streamit application
- `app/models/hotdog_classifier.py`: Image classification model
- `app/utils/image_utils.py`: Image processing utilities
- `app/tests/`: Test files 
- `images`: Some sample images for testing