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
    worker.initiate_chat(assistant, message=question)
    return worker.get_response()

iface = gr.Interface(fn=get_response, inputs=["text", "number"], outputs="text", inputs_label=["Question", "Max Auto Reply"])
iface.launch()
