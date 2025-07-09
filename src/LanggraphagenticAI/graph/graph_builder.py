from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime

from src.LanggraphagenticAI.nodes.BasicChatbotnode import BasicChatbotnode
from src.LanggraphagenticAI.state.state import State

class Graph_Builder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_buildgraph(self):
        """
        Builds a basic chatbot graph using Langgraph
        This method initializes a chatbot node using the BasicChatBOTNODE class
        and integrates it into the graph.The chatbot node is set as both the entry and exit
        point fo the graph
        """

        self.basic_chatbot_node=BasicChatbotnode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """
        Sets the graph based on the use case selection
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_buildgraph()

###Compile the graph after the respective use case selection
        return self.graph_builder.compile()    

