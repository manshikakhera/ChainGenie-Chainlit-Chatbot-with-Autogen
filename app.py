import chainlit as cl
import autogen
from agents.chainlit_agents import ChainlitAssistantAgent, ChainlitUserProxyAgent, DataVisualizationAgent
import os 
# -------------------- LLM Configuration ----------------------------- #


# -------------------- Global Constants ----------------------------- #
USER_PROXY_NAME = "Query_Agent"
ASSISTANT = "Assistant"

llm_config = {
    "api_type": "azure",
    "api_key": os.getenv("AZURE_API_KEY"),
    "base_url": os.getenv("AZURE_API_BASE_URL"),
    "api_version": "2024-08-01-preview",  # model name
}
# -------------------- Initialize Agents ----------------------------- #
@cl.on_chat_start
async def on_chat_start():
    try:
        # Instantiate agents
        assistant = ChainlitAssistantAgent(
            name=ASSISTANT,
            llm_config=llm_config,
            system_message="Assistant. Assist the User Proxy in the task.",
            description="Assistant Agent",
            code_execution_config={"use_docker": False}
        )

        user_proxy = ChainlitUserProxyAgent(
            name=USER_PROXY_NAME,
            human_input_mode="ALWAYS",
            llm_config=llm_config,
            description="User Proxy Agent",
            code_execution_config={"use_docker": False}
        )

        data_viz_agent = DataVisualizationAgent(
            name="DataVisualizer",
            llm_config=llm_config,
            system_message="Visualize and analyze user data.",
            description="Data Visualization Agent",
            code_execution_config={"use_docker": False}
        )

        # Store agents in the user session
        cl.user_session.set(USER_PROXY_NAME, user_proxy)
        cl.user_session.set(ASSISTANT, assistant)
        cl.user_session.set("DataVisualizer", data_viz_agent)

        # Initial message
        await cl.Message(
            content="Hello! What task would you like to get done today?",
        ).send()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

# -------------------- Handle Message and File Upload ----------------------------- #
@cl.on_message
async def handle_message(message: cl.Message):
    context = message.content.lower()

    # Check if there's a file uploaded with the message
    uploaded_files = message.elements

    # Retrieve agents from the user session
    user_proxy = cl.user_session.get(USER_PROXY_NAME)
    assistant = cl.user_session.get(ASSISTANT)
    data_viz_agent = cl.user_session.get("DataVisualizer")

    # If there's a file uploaded, save it and trigger visualization
    if uploaded_files:
        file_path = uploaded_files[0].path
        cl.user_session.set("uploaded_file", file_path)
        await cl.Message(content="File uploaded successfully! Generating visualization...").send()
        await data_viz_agent.visualize_data(file_path)
        return  # Exit after handling the file upload

    # Check if the message contains keywords for visualization
    if "visualize" in context or "graph" in context or "analyze" in context:
        file_path = cl.user_session.get("uploaded_file")

        if file_path:
            # If a file is uploaded, visualize it
            await data_viz_agent.visualize_data(file_path)
        else:
            # No file uploaded, forward the query to the assistant
            await cl.make_async(assistant.send)(message.content, recipient=user_proxy)
    else:
        # Default behavior for conversation with the assistant and user proxy
        MAX_ITER = 15

        groupchat = autogen.GroupChat(
            agents=[user_proxy, assistant, data_viz_agent],
            messages=[],
            max_round=MAX_ITER
        )

        manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

        await cl.make_async(user_proxy.initiate_chat)(manager, message=message.content)
