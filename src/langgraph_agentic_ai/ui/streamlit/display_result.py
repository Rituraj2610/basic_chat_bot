import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage


class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display old history
        for msg in st.session_state.messages:

            if isinstance(msg, HumanMessage):
                with st.chat_message("user"):
                    st.write(msg.content)

            elif isinstance(msg, AIMessage):
                with st.chat_message("assistant"):
                    st.write(msg.content)

        if self.usecase == "Basic Chatbot":

            # Add current user message
            st.session_state.messages.append(
                HumanMessage(content=self.user_message)
            )

            # Run graph with full history
            result = self.graph.invoke({
                "messages": st.session_state.messages
            })

            # Get latest AI response
            ai_message = result["messages"][-1]

            # Save AI response
            st.session_state.messages.append(ai_message)

            # Display current user message
            with st.chat_message("user"):
                st.write(self.user_message)

            # Display AI response
            with st.chat_message("assistant"):
                st.write(ai_message.content)