
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

# This is a mock tool that we'll use in our graph.
def my_tool(messages):
    # In a real application, this would do something useful.
    # For this example, it just returns a message.
    return "Tool response: The weather is nice."

# This is the main graph.
graph = MessageGraph()

# The graph has one node, which is our mock tool.
graph.add_node("tool", my_tool)

# The entry point for the graph is the "tool" node.
graph.add_edge("tool", END)

# The entry point for the graph is the "tool" node.
graph.set_entry_point("tool")


# Compile the graph into a runnable object.
runnable = graph.compile()

# Let's run it!
if __name__ == "__main__":
    # We'll send a message to the graph. The content of the message doesn't
    # matter for this example, because our mock tool doesn't use it.
    inputs = [HumanMessage(content="What is the weather?")]
    
    # Invoke the graph and print the result.
    result = runnable.invoke(inputs)
    
    # The result will be the message returned by our mock tool.
    print(result)
