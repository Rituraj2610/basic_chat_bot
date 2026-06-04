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

        response = self.llm.invoke(state["messages"])

        return {
            "messages": [response]
        }