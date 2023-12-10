import gradio as gr
from pydantic import BaseModel, ValidationError
from plugins.sk_bing_plugin import BingPlugin
from plugins.sk_web_pages_plugin import WebPagesPlugin
from planning.autogen_planner import AutoGenPlanner
from web_search_client import WebSearchClient
from web_search_client.models import SafeSearch
from azure.core.credentials import AzureKeyCredential
from semantic_kernel.core_skills.text_skill import TextSkill
from semantic_kernel.planning.basic_planner import BasicPlanner
from semantic_kernel import Kernel

# Configure your credentials here
bing_api_key = "ArXXXXdpJ"  # Replace with your Bing API key

llm_config = {
    "type": "openai",  # "azure" or "openai"
    "openai_api_key": "sk-rR5XXXXm",  # OpenAI API Key
    "azure_deployment": "",  # Azure OpenAI deployment name
    "azure_api_key": "",  # Azure OpenAI API key in the Azure portal
    "azure_endpoint": ""  # Endpoint URL for Azure OpenAI, e.g. https://contoso.openai.azure.com/
}
import semantic_kernel
kernel = semantic_kernel.Kernel()
kernel.import_skill(BingPlugin(bing_api_key))
kernel.import_skill(WebPagesPlugin())
sk_planner = AutoGenPlanner(kernel, llm_config)
assistant = sk_planner.create_assistant_agent("Assistant")

def get_response(question, max_auto_reply):
    worker = sk_planner.create_user_agent("Worker", max_auto_reply=max_auto_reply, human_input="NEVER")
    assistant = sk_planner.create_assistant_agent("Assistant")
    worker.initiate_chat(assistant, message=question)
    return worker.get_response()

class ChainlitAssistantAgent(AssistantAgent):
    def __init__(self, name, sk_planner):
        super().__init__(name)
        self.sk_planner = sk_planner

    async def process_message(self, message):
        # Use sk_planner to process the message and generate a response
        response = self.sk_planner.create_assistant_agent("Assistant")
        response.initiate_chat(self, message=message)
        return response.get_response()

class ChainlitUserProxyAgent(UserProxyAgent):
    def __init__(self, name, assistant_agent):
        super().__init__(name)
        self.assistant_agent = assistant_agent

    async def get_human_input(self, prompt):
        # Get input from the user via Chainlit interface
        reply = await cl.ask_user_message(content=prompt)
        return reply["content"].strip()

    async def send(self, message):
        # Send the message to the assistant agent and get the response
        response = await self.assistant_agent.process_message(message)
        # Display the response in the Chainlit interface
        cl.message(content=response, author=self.assistant_agent.name).send()

# Initialize the agents
assistant_agent = ChainlitAssistantAgent("Assistant", sk_planner)
user_proxy_agent = ChainlitUserProxyAgent("User_Proxy", assistant_agent)

# Chainlit Web Interface
@cl.page("/")
def main_page():
    with cl.form("user_input_form"):
        question = cl.text_input("Describe your problem:")
        submit_button = cl.button("Submit")

        if submit_button:
            cl.run_async(user_proxy_agent.send(question))

if __name__ == "__main__":
    cl.run(main_page)