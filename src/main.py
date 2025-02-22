import streamlit as st
import ollama

class OllamaChat:
    """
    A class to interact with the Ollama chat model.
    """
    def __init__(self, model: str = "qwen2.5:0.5b"):
        """Initialize the chat model."""
        self.model = model

    def generate_response(self, prompt: str) -> str:
        """Generate a response from the Ollama model."""
        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']

class StreamlitChatUI:
    """
    A class to create a Streamlit-based chat UI.
    """
    
    def __init__(self, chat_model: OllamaChat):
        """
        Initialize the Streamlit UI.
        
        Parameters
        ----------
        chat_model : OllamaChat
            An instance of the OllamaChat class.
        """
        self.chat_model = chat_model
        self.setup_ui()

    def setup_ui(self):
        """Setup the Streamlit UI layout."""
        st.set_page_config(page_title="Chatbot", page_icon="🤖")
        st.title("🤖 Chatbot")
        st.write("Chat with your local Ollama model!")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input box
        user_input = st.chat_input("Ask me anything...")
        if user_input:
            self.process_input(user_input)

    def process_input(self, user_input: str):
        """
        Handle user input and generate a response.
        
        Parameters
        ----------
        user_input : str
            The input provided by the user.
        """
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            response = self.chat_model.generate_response(user_input)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    chat_model = OllamaChat(model="qwen2.5:0.5b")  # Change model if needed
    StreamlitChatUI(chat_model)
