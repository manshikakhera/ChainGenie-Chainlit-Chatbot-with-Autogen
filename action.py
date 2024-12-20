
# try:
#     response = openai.ChatCompletion.create(
#         engine="gpt-4o-team1",  # Your Azure deployment name
#         messages=[
#             {"role": "system", "content": "You are an assistant."},
#             {"role": "user", "content": "What is Python?"}
#         ]
#     )
#     # Print the assistant's reply
#     print(response.choices[0].message['content'])
# except openai.error.OpenAIError as e:
#     print(f"An error occurred: {e}")



import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    uploaded_files = await cl.AskFileMessage(
        content="Please upload a CSV or Excel file:",
        accept=[".csv", ".xlsx"]
    ).send()

    if uploaded_files:
        await cl.Message(content=f"File uploaded: {uploaded_files[0].name}").send()
    else:
        await cl.Message(content="No file uploaded.").send()
 
