from src.LanggraphagenticAI.state.state import State
class BasicChatbotnode:
    """
    Basic chatbot logic implementation
    """
    def __init__(self,model):
        self.llm = model 

    def process(self,state:State)->dict:
        """
        Processes the input state and generates chatbot response
        """
        return{"Messages":self.llm.invoke(State['messages'])}

