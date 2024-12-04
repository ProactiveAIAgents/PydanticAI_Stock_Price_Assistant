# PydanticAI Stock Price Assistant

## Description
A Python-based financial analysis tool that leverages the Yahoo Finance API (yfinance) to fetch and analyze stock market data. The project features an interactive web interface built with Gradio, allowing users to easily visualize and analyze financial data through interactive plots powered by Plotly. The application utilizes Pydantic for robust data validation and schema enforcement, ensuring data integrity throughout the analysis pipeline and providing type-safe data structures for financial metrics.

## Features
- Real-time stock data fetching using yfinance
- Interactive web interface for data visualization
- Dynamic financial charts and graphs
- Secure environment variable management
- Asynchronous data processing capabilities

## Technologies Used
- Python
- Gradio (Web Interface)
- YFinance (Financial Data API)
- Plotly (Data Visualization)
- Pydantic (Data Validation)
- Python-dotenv (Environment Management)

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in `.env` file
4. Run the application: `python run.py`
