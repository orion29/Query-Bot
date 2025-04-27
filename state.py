from typing import TypedDict

class MandatoryState(TypedDict):
    user_input: str  

class OptionalState(TypedDict, total=False):
    optimized_prompt: str    
    context: dict             
    schema: dict            
    ambiguity_flags: bool     
    pandas_code: str         
    execution_result: str     
    memory: list                   
    agent_status: dict 
    prompt_path: str 
    data_path: str 
    column_description_table: str 
    traceback_error: str 
    chain_of_thought: dict
    bot_output: str 
    code_execution_limit: int

class State(MandatoryState, OptionalState):
    pass


def state_defination_agent(state: State) -> State:
    state["agent_status"] = {"schema_selection_node": True}
    state["prompt_path"] = "prompt/"
    state["data_path"] = "data/"
    state["column_description_table"] = "data/column_description_table.csv"
    state["pandas_code"] = ""
    state["traceback_error"] = ""
    state["chain_of_thought"] = {}
    state["code_execution_limit"] = 3
    state["execution_result"] = ""
    state["schema"] = {}
    state["bot_output"] = ""
    return state
