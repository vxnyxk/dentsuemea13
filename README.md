# Azure OpenAI Assistant

You can deploy your Azure OpenAI assistant with Chainlit using this template.
![openai-assistant](https://github.com/Chainlit/openai-assistant/assets/13104895/5c095a89-e426-417e-977d-772c4d4974c2)

### Supported Assistant Features

| Streaming | Files | Code Interpreter | File Search | Voice |
| --------- | ----- | ---------------- | ----------- | ----- |
| ✅        | ✅    | ✅               | ✅          | ✅    |

### Instructions

1. Provision an Azure OpenAI resource and create a deployment for gpt-4 (Model number:- 0125). Assistants API (Preview) is only [supported in certain regions and models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#assistants-preview). In addition, [only certain API versions are supported](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/assistant#api-versions)

1. Update .env.sample with the correct Azure OpenAI configuration (leave OPENAI_ASSISTANT_ID blank for now, we will create it in step 4). Rename ".env.sample" to ".env".

1. Install the required Python modules

    ```
    pip install -r requirements.txt
    ```

1. Create an Assistant

    ```
    & python create_assistant.py
    ```

    Copy the ID value from the output "Assistant created with ID: X" and update .env OPENAI_ASSISTANT_ID with the value of X.

1. Run chainlit

    ```
    chainlit run app.py  -w
    ```