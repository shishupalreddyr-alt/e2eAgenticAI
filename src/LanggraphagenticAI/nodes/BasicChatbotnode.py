from src.LanggraphagenticAI.state import state

class BasicChatbotnode:
    """
    Basic chatbot logic implementation
    """
    def __init__(self,model):
        self.llm = model 

    def process(self,state:state)->dict:
        """
        Processes the input state and generates chatbot response
        """
        return{"Messages":self.ll.invoke(state['messages'])}

