import openai

# Replace with your OpenAI API key
openai.api_key = "your_openai_api_key"

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()
