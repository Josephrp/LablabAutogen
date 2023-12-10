import gradio as gr
import os
from pydantic import BaseModel, ValidationError
from plugins.sk_bing_plugin import BingPlugin
from plugins.sk_web_pages_plugin import WebPagesPlugin
from planning.autogen_planner import AutoGenPlanner
from web_search_client import WebSearchClient
from web_search_client.models import SafeSearch
from azure.core.credentials import AzureKeyCredential
from semantic_kernel.core_skills.text_skill import TextSkill
from semantic_kernel.planning.basic_planner import BasicPlanner
from dotenv import load_dotenv
import semantic_kernel



load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BING_API_KEY = os.getenv("BING_API_KEY")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")



llm_config = {
    "type": "openai",  # "azure" or "openai"
    "openai_api_key": OPENAI_API_KEY,  # OpenAI API Key
    "azure_deployment": "",  # Azure OpenAI deployment name
    "azure_api_key": AZURE_API_KEY,  # Azure OpenAI API key in the Azure portal
    "azure_endpoint": ""  # Endpoint URL for Azure OpenAI, e.g. https://contoso.openai.azure.com/
}
kernel = semantic_kernel.Kernel()
kernel.import_skill(BingPlugin(BING_API_KEY))
kernel.import_skill(WebPagesPlugin())
sk_planner = AutoGenPlanner(kernel, llm_config)
assistant = sk_planner.create_assistant_agent("Assistant")

def get_response(question, max_auto_reply):
    worker = sk_planner.create_user_agent("Worker", max_auto_reply=max_auto_reply, human_input="NEVER")
    worker.initiate_chat(assistant, message=question)
    return worker.get_response()

iface = gr.Interface(fn=get_response, inputs=["text", "number"], outputs="text", inputs_label=["Question", "Max Auto Reply"])
iface.launch()
