from graph import build_graph

graph = build_graph()

user_question  = "Lets start"
while(user_question):

    user_question  = input("Ask query : \n")
    if user_question.lower() == "exit":
        break

    state = {
    "user_input":user_question  
    }
    output = graph.invoke(state)

    print("\n\nOutput: ",output["bot_output"])




    