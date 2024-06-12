import os
import chainlit as cl
import asyncio

from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
        azure_endpoint=os.getenv("OPENAI_API_BASE"),
        api_key=os.getenv("OPENAI_API_KEY"),
        api_version=os.getenv("OPENAI_API_VERSION"),
)

async def create_assistant():
    assistant = await client.beta.assistants.create(
        name="General Assistant",
        instructions="You are an AI assistant. Please help the user with their queries.",
        tools=[{"type": "code_interpreter"}],
        model=os.getenv("OPENAI_ASSISTANT_MODEL"),
    )
    return assistant


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    assistant = loop.run_until_complete(create_assistant())
    print(f"Assistant created with ID: {assistant.id}")

