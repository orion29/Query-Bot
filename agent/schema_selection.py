from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
from state import State

def create_schema_selection_agent(llm):
    def schema_selection_agent(state: State) -> State:
        user_question = state["user_input"]
        column_description_table_path = state["column_description_table"]
        column_description_table = pd.read_csv(column_description_table_path)

        prompt_path = state["prompt_path"] + "schema_selection.txt"
        with open(prompt_path, 'r') as f:
            schema_selection_template = f.read()

        table_schema = ""
        for i, j in column_description_table.groupby("table_name"):
            j = j.reset_index(drop=True)
            table_schema += "Table name: " + str(i) + "\n"
            table_schema += "Table description: " + str(j["table_description"].unique()[0]) + "\n\n"
            table_schema += f"Column descriptions of table {i}: \n"
            for k in range(len(j)):
                l = j.iloc[k]
                table_schema += "Column name: " + str(l["column_name"]) + "\n"
                table_schema += "Column description: " + str(l["column_description"]) + "\n"
                table_schema += "Typical values: " + str(l["typical_values"]) + "\n"
            table_schema += "\n\n"

        schema_selection_prompt = PromptTemplate(
            input_variables=["user_question", "table_schema"],
            template=schema_selection_template
        )

        parser = JsonOutputParser()

        schema_chain = schema_selection_prompt | llm | parser
        schema_json = schema_chain.invoke({
            "table_schema": table_schema,
            "user_question": user_question
        })

        state["schema"] = schema_json
        state["chain_of_thought"]["Schema selection"] = schema_json['chain_of_thought']
        print("Schema selected : \n",schema_json)
        return state

    return schema_selection_agent
