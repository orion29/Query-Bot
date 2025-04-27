from langchain.prompts import PromptTemplate
import pandas as pd
from state import State



def code_execution_agent(state:State)->State:
    
    local_vars = {}
    pandas_code = state["pandas_code" ]
    exec(pandas_code ,globals(),local_vars)
    python_output = local_vars['final_output']["output"]
    error = local_vars['final_output']['traceback_error']
    

    state["execution_result"] = python_output
    state["traceback_error"] = error

    print(local_vars['final_output'])

    return state