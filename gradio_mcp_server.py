import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
   Count the number of occurrence of a letter in a word or text.
   Args:
        word (str): The input text to search through
        letter (str): The letter to search for

        Returns:
        int: The number of time the letter appears in the text
    """
    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# create a standard gradio interafce
demo = gr.Interface(
    fn = letter_counter,
    inputs = ["textbox", "textbox"],
    outputs = "number",
    title = "Letter Counter",
    description = "Enter text and a letter to count how many times the letter appears in the text."
)

if __name__ == "__main__":
    demo.launch(mcp_server=True) # <------|

# https://huggingface.co/learn/mcp-course/unit1/gradio-mcp
# When you set mcp_server=True in launch(), several things happen:

# Gradio functions are automatically converted to MCP Tools

# Input components map to tool argument schemas

# Output components determine the response format

# The Gradio server now also listens for MCP protocol messages
    
# JSON-RPC over HTTP+SSE is set up for client-server communicatio