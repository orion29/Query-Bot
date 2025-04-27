from langgraph.graph import StateGraph, START, END
from state import State,state_defination_agent
from helper.llm_loader import LLMLoader
from agent.schema_selection import create_schema_selection_agent
from agent.code_generation import create_code_generation_agent
from agent.code_execution import code_execution_agent
from agent.pretty_print import create_pretty_print_agent
from helper.conditions import check_code_status, check_execution_status
from dotenv import load_dotenv
import os



load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
loader = LLMLoader(google_api_key=GOOGLE_API_KEY)
llm = loader.load_google_model_flash2()

builder = StateGraph(State)
schema_selection_agent = create_schema_selection_agent(llm)
code_generation_agent = create_code_generation_agent(llm)
pretty_print_agent = create_pretty_print_agent(llm)


builder.add_node(state_defination_agent,"state_defination_agent")
builder.add_node(schema_selection_agent,"schema_selection_agent")
builder.add_node(code_generation_agent,"code_generation_agent")
builder.add_node(code_execution_agent,"code_execution_agent")
builder.add_node(pretty_print_agent,"pretty_print_agent")

builder.add_edge(START,"state_defination_agent")
builder.add_edge("state_defination_agent","schema_selection_agent")
#builder.add_edge(START,"schema_selection_agent")
builder.add_edge("schema_selection_agent","code_generation_agent")
#builder.add_edge("code_generation_agent","code_execution_agent")
builder.add_conditional_edges("code_generation_agent",check_code_status)
builder.add_conditional_edges("code_execution_agent",check_execution_status)
#builder.add_edge("code_execution_agent","pretty_print_agent")
builder.add_edge("pretty_print_agent",END)

graph = builder.compile()

