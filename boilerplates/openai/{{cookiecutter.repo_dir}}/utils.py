from openai import OpenAI


def get_completion(
    client: OpenAI, model: str, messages: list, max_tokens=200, **kwargs
):
    completion = client.chat.completions.create(
        model=model, messages=messages, max_tokens=max_tokens, **kwargs
    )
    return completion.choices[0].message.content
