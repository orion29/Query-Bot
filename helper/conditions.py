import pandas as pd
from state import State
from typing import Literal


def check_code_status(state:State)-> Literal["pretty_print_agent", "code_execution_agent"]:

    pandas_code = state["pandas_code"] 
    if pandas_code is None:
        return "pretty_print_agent"
    else:
        return "code_execution_agent"
    
def check_execution_status(state:State)-> Literal["pretty_print_agent", "code_generation_agent"]:

    execution_result = state["execution_result"] 
    
    state["code_execution_limit"]
    code_execution_limit = state["code_execution_limit" ]

    if execution_result  :
        return "pretty_print_agent"
    elif code_execution_limit == 0:
        return "pretty_print_agent"
    else:
        return "code_generation_agent"
