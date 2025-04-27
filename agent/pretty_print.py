from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
from state import State


def create_pretty_print_agent(llm):
    def pretty_print_agent(state:State)->State:

        user_question = state["user_input"]
        python_output = state["execution_result"]

        prompt_path = state["prompt_path"] + "pretty_print.txt"

        with open(prompt_path, 'r') as f:
            pretty_print_template = f.read()

        pretty_print_prompt = PromptTemplate(
            input_variables=["user_question","output"],
            template=pretty_print_template )


        chain = pretty_print_prompt | llm

        output = chain.invoke({
        "user_question":user_question,
        "output":python_output })

        state["bot_output"] = output.content

        return {"bot_output":output.content}
    return pretty_print_agent
        
    