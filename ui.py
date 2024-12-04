import asyncio
import os

import gradio as gr
import nest_asyncio
import yfinance as yf
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent

# Load environment variables
load_dotenv()

# Set the API key in environment
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()


class StockPriceResult(BaseModel):
    symbol: str
    price: float
    currency: str = "USD"
    message: str


# Create the agent globally
stock_agent = Agent(
    "groq:mixtral-8x7b-32768",
    result_type=StockPriceResult,
    system_prompt="You are a helpful financial assistant that can look up stock prices. Use the get_stock_price function to look up current stock prices.",
)


@stock_agent.tool_plain
def get_stock_price(symbol: str) -> dict:
    """Get the current stock price for a given symbol."""
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info.last_price
        if price is None:
            raise ValueError(f"Could not get price for {symbol}")
        return {"price": round(price, 2), "currency": "USD"}
    except Exception as e:
        raise ValueError(f"Error getting stock price: {str(e)}")


async def async_get_stock_info(query: str) -> str:
    try:
        # Run the query asynchronously
        result = await stock_agent.run(query)

        # Format the response
        response = f"Stock: {result.data.symbol}\n"
        response += f"Price: ${result.data.price:.2f} {result.data.currency}\n"
        response += f"{result.data.message}"
        return response
    except Exception as e:
        return f"Error: {str(e)}"


def get_stock_info(query: str) -> str:
    # Run the async function in the event loop
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_get_stock_info(query))


# Create the Gradio interface
demo = gr.Interface(
    fn=get_stock_info,
    inputs=gr.Textbox(
        label="Ask about any stock price",
        placeholder="Example: What is the price of Tesla?",
    ),
    outputs=gr.Textbox(label="Stock Information"),
    title="Stock Price AI Assistant",
    description="Ask me about any stock price and I will help you find it!",
    examples=[
        ["What is Apple's current stock price?"],
        ["What is the price of Tesla stock?"],
        ["How much does Microsoft stock cost?"],
    ],
)

if __name__ == "__main__":
    demo.launch()
