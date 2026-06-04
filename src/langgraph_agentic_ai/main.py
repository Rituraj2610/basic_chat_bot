import streamlit as st

from src.langgraph_agentic_ai.llms.groqllm import GroqLLM
from src.langgraph_agentic_ai.ui.streamlit.loadui import LoadStreamlitUI
from src.langgraph_agentic_ai.llms.groqllm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlit.display_result import DisplayResultStreamlit

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the Langgraph Agentic AI APplication with Streamlit UI.
    This function initializes the ui, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    """

    # LOAD UI

    ui = LoadStreamlitUI()  # class
    user_input = ui.load_streamlit_ui() # class's method

    if not user_input:
        st.error("Failed to load user input")
        return

    user_message = st.chat_input("Enter your message")

    if user_message:
        try:
            # CONfigure llms
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: llm model could not be initialized")
                return

            usecase = user_input.get("selected_usecases")

            if not usecase:
                st.error("Error: No use case selected")
                return

            ## Graph Builder
            graph_builder = GraphBuilder(model=model)
            try:
                graph= graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Graph setup failed -{e}")
                return
        except Exception as e:
            st.error(f"No user message -{e}")
            return

