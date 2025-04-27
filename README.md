# LangGraph Integration for Data Science Workflow

This repository integrates LangGraph with a custom data science workflow for schema selection, code generation, and code execution in a structured manner. The system uses large language models (LLMs) for AI-driven automation in data manipulation tasks, leveraging LangGraph's state graph architecture for process management.

## Architecture

- **LLM Integration**: Generative AI models are used for schema selection and code generation.
- **LangGraph**: The framework is used to model the flow of tasks as a state graph.
- **File Handling**: Metadata (schema and column descriptions) are read from CSV files for processing.


## What Has Been Done

### Features Implemented:

- **Schema Selection**: The `schema_selection_agent` reads metadata and selects the appropriate schema based on user input.
- **Code Generation**: The `code_generation_agent` generates Python code (using Pandas) based on selected schema and user input.
- **Code Execution**: The `code_execution_agent` executes the generated code and returns the output.
- **Pretty Print**: The `pretty_print_agent` formats the output for human-readable explanations.

####      Example:
![LangGraph Dev Image](https://github.com/orion29/Query-Bot/blob/154f8b9b6d2d59e73004872f59104e28fb52b08a/assets/langgraph_studio.png)


## What’s Pending

### Remaining Work:

- **Error Handling**: More robust error handling in the execution agent, especially for syntax errors and logical mistakes in code generation.
- **Performance Optimizations**: Optimizing the code generation logic and execution time, particularly for larger datasets. (Pyspark / or loading tables initially while running)
- **Enhanced User Interaction for Ambiguity Handling**: Adding more interactive components to enhance user input and output handling, possibly with a web interface or GUI.
- **Context handling**: A new contextual engine that takes previous questions (in case we don't want to expose table content) or both previous questions and answers 

## How to Run

### 1. Set up Environment:

- Clone the repository and install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Running the Workflow:

#### If you want to run it on the terminal:

- You can run the script directly from the terminal:
    ```bash
    python main.py
    ```

#### If you want to run it on LangGraph Studio:

- You can use LangGraph Studio to run the workflow by executing:
    ```bash
    langgraph dev
    ```

- Once LangGraph Studio is running, you will be prompted to enter your query in the `user_input` field. 

### 3. Modifying Data Files:

- **Modify the column description file** located in the `data` folder to match the name of your CSV files. For example, if your CSV file is named `resource_table.csv`, you should edit the description file as follows:
    ```plaintext
    table_name = resource_table
    ```

- **Add your CSV files** containing the necessary tables into the `data` folder. Make sure the names match those mentioned in the column description file.

## Contributing

Feel free to fork this repository and make changes. Contributions are welcome! Please submit a pull request with your proposed changes.

### Steps for Contribution:
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Implement the change and test it locally.
- Submit a pull request with a clear description of the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
