from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import random
import time
from datetime import datetime, timedelta

class WebSearchInput(BaseModel):
    """Input schema for WebSearchTool."""
    query: str = Field(description="The search query to look up")
    num_results: int = Field(default=5, description="Number of results to return")

class WebSearchTool(BaseTool):
    """Tool for performing web searches to find current information."""
    
    name: str = "Web Search"
    description: str = "Search the web for current information on a topic"
    args_schema: Type[BaseModel] = WebSearchInput
    
    def _run(self, query: str, num_results: int = 5) -> str:
        """
        Simulates a web search for current information.
        
        In a production environment, this would use an actual search API like 
        Google Search, Bing, or a news API. For this demo, we'll simulate results.
        """
        # Simulate search delay
        time.sleep(random.uniform(1.0, 2.5))
        
        # Generate current date for making results seem current
        current_date = datetime.now()
        yesterday = current_date - timedelta(days=1)
        
        # Simulate search results based on query
        if "ai" in query.lower() or "artificial intelligence" in query.lower():
            results = [
                {
                    "title": "New AI Model Breaks Records in Multi-Modal Reasoning",
                    "url": "https://example.com/tech/ai-model-record",
                    "snippet": "The latest AI model from OpenAI demonstrates unprecedented capabilities in understanding and reasoning about text and images simultaneously.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": "AI Regulation Framework Proposed by International Coalition",
                    "url": "https://example.com/policy/ai-regulation",
                    "snippet": "A group of 25 countries have proposed a unified framework for regulating artificial intelligence development and deployment.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": "AI-Generated Content Now Indistinguishable from Human Work, Study Finds",
                    "url": "https://example.com/tech/ai-content-study",
                    "snippet": "Researchers found that most people cannot reliably distinguish between content created by AI systems and human writers in blind tests.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": "AI Ethics Board Resigns Over Transparency Concerns",
                    "url": "https://example.com/ethics/ai-board-resignation",
                    "snippet": "The entire ethics board of a major AI company has resigned, citing concerns about lack of transparency in the company's development process.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": "AI Assistants Being Deployed in Healthcare at Record Rates",
                    "url": "https://example.com/health/ai-assistants",
                    "snippet": "Hospitals and healthcare providers are adopting AI assistants at unprecedented rates to help with everything from diagnosis to patient communication.",
                    "date": current_date.strftime("%Y-%m-%d")
                }
            ]
        elif "climate" in query.lower() or "environment" in query.lower():
            results = [
                {
                    "title": "Global Temperature Rise Exceeds Previous Projections",
                    "url": "https://example.com/environment/temperature-rise",
                    "snippet": "New data indicates that global temperatures are rising faster than scientists had previously projected, raising concerns about climate modeling.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": "Carbon Capture Technology Breakthrough Announced",
                    "url": "https://example.com/tech/carbon-capture",
                    "snippet": "Scientists have developed a new carbon capture method that is 40% more efficient than existing technologies, potentially transforming climate mitigation efforts.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": "Major Countries Pledge to Triple Renewable Energy by 2030",
                    "url": "https://example.com/policy/renewable-energy-pledge",
                    "snippet": "A coalition of major economies has announced a commitment to triple their renewable energy capacity within the next seven years.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": "Climate Refugees Exceed 20 Million Globally",
                    "url": "https://example.com/society/climate-refugees",
                    "snippet": "A new UN report estimates that over 20 million people have been displaced by climate change-related events in the past year.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": "Ocean Acidity Reaches Historic Levels, Threatening Marine Ecosystems",
                    "url": "https://example.com/environment/ocean-acidity",
                    "snippet": "Researchers have measured record levels of ocean acidity, posing severe threats to coral reefs and marine life worldwide.",
                    "date": current_date.strftime("%Y-%m-%d")
                }
            ]
        else:
            # Generic trending topics
            results = [
                {
                    "title": f"Latest Developments in {query}",
                    "url": f"https://example.com/trending/{query.replace(' ', '-')}",
                    "snippet": f"Recent advancements and news related to {query} that are making headlines globally.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": f"Expert Opinions on {query} Trends",
                    "url": f"https://example.com/experts/{query.replace(' ', '-')}",
                    "snippet": f"Leading experts share their insights on where {query} is headed in the coming months.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": f"Controversy Surrounding {query}",
                    "url": f"https://example.com/analysis/{query.replace(' ', '-')}-debate",
                    "snippet": f"Examining the ongoing debates and controversies related to {query} and their implications.",
                    "date": current_date.strftime("%Y-%m-%d")
                },
                {
                    "title": f"Statistical Analysis of {query} Impact",
                    "url": f"https://example.com/data/{query.replace(' ', '-')}-statistics",
                    "snippet": f"New data reveals surprising statistics about how {query} is affecting various sectors.",
                    "date": yesterday.strftime("%Y-%m-%d")
                },
                {
                    "title": f"Future of {query}: Predictions and Forecasts",
                    "url": f"https://example.com/future/{query.replace(' ', '-')}-outlook",
                    "snippet": f"Analysts present their forecasts for how {query} will evolve over the next several years.",
                    "date": current_date.strftime("%Y-%m-%d")
                }
            ]
            
        # Limit results to requested number
        results = results[:num_results]
        
        # Return results as a formatted string
        return json.dumps({"results": results}, indent=2)