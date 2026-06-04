from src.langgraph_agentic_ai.state.state import State

class BasicChatBotNode:
    """
    Basic Chat Bot login implementation
    """

    def __init__(self, model):
        self.llm=model

    def process(self, state: State)->dict:
        """
        Process input state and generates a chatbot response
        """

        return {"messages": self.llm.invoke(state['messages'])}