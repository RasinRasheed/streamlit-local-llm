# Streamlit Local LLM

This project demonstrates how to use a local language model with Streamlit.

## Requirements

- Python 3.7+
- Streamlit
- Ollama

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RasinRasheed/streamlit-local-llm.git
    cd streamlit-local-llm
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the Ollama model separately using the following command:
    ```bash
    ollama run <model-name>
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run .\src\main.py 
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the app.

## License

This project is licensed under the MIT License.