from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
from state import State



def create_code_generation_agent(llm):
    def code_generation_agent(state : State) -> State:
        
        user_question = state["user_input"]
        output = state["schema"]
        data_path = state["data_path"]

        table_path_dict = {str(i["table_name"]):data_path+str(i["table_name"])+".csv" for i in output["selected_columns"]}

        table_path = ""
        for i in table_path_dict.keys():
            table_path+="For table "+i+" use path "+table_path_dict[i]+"\n"
        

        prompt_path = state["prompt_path"] + "code_generation.txt"

        with open(prompt_path, 'r') as f:
            code_generation_template = f.read()


        code_generation_prompt = PromptTemplate(input_variables=["structured_json_output", "user_question","table_path","old_code","traceback_error"],
                                                template=code_generation_template  )
        
        parser = JsonOutputParser()

        code_chain = code_generation_prompt | llm | parser

        output = code_chain.invoke({
                            "structured_json_output": output,
                            "user_question": user_question,
                            "table_path":table_path,
                            "old_code": state["pandas_code"],
                            "traceback_error":state["traceback_error"]
                            
                            })
        
        state["chain_of_thought"]["Code Generation"] = output["chain_of_thought"]
        state["pandas_code"] = output['python_code']
        state["code_execution_limit"] -= 1
        print(output)
        return state
    return code_generation_agent   
