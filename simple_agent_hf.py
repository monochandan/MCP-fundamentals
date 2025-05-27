from smolagents import CodeAgent, InferenceClientModel
from dotenv import load_dotenv
import os
from huggingface_hub import login
load_dotenv()
hf_token = os.environ.get("HUGGING_FACE_TOKEN")
login(hf_token)
# print(hf_token)
model_id = "mistralai/Mistral-7B-Instruct-v0.1"

model = InferenceClientModel()

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you get me the title of the publication mentioned in this page also the authores of this paper url 'https://link.springer.com/chapter/10.1007/978-3-031-56826-8_10'?"
)
