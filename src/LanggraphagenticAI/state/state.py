from typing import Annotated,Optional,TypedDict,List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage,AIMessage

class state(TypedDict):
    """
    Represents the structure of state used in the graph
    """
    messages:Annotated[list,add_messages]

