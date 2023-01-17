import openai
import languages

# Insert your OpenAI API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def get_response(prompt, lang):
    # Get the input text and target language
    text = f"{prompt}"
    target_language = languages.find_closest_match(lang)
    # Use the OpenAI GPT-3 language model to translate the text
    response = openai.Completion.create(engine="text-davinci-002",
                                        prompt=f"translate  the following text to  {target_language}: {text}")
    # Return the translated text
    return response.choices[0].text
