from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return te list of tools to be used in the chatbot

    """
    tools=TavilySearchResults(max_results=2)
    return tools

def create_toolnode(tools):
    """
    Creates and returns  tool node for the graph
    """
    return ToolNode(tools=tools)
