import openai

summary = """Write sumamry of the following: 
---
{input}
---
This is the summary: """

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key
    
class TextSummary:
    def __init__(self):
        print("Text Summary Model Intialized--->")

    def summarize(self, input_text, myKwargs={}):
        """
        wrapper for the API to save the input text and the summary
        """        
        # Arguments to send the API
        kwargs = {
            "model":"text-babbage-001",
            "prompt":input_text, 
            "temperature":0.9, 
            "max_tokens":256,
            "top_p":1.0, 
            "frequency_penalty":0.0, 
            "presence_penalty":0.0,
            "stop": ["."]
        }

        # update the arguments
        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]
        
        summary = openai.Completion.create(**kwargs)["choices"][0]["text"].strip()
        return summary
    
    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.summarize(summary.format(input = input))
        return output


