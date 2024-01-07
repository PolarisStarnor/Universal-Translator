# cleanup text input

import replicate
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = "You are a minimal text correction engine. Print the following character sequence before and after your modifications to the text: '%%%'"

def clean(text : str) -> str:
    pre_prompt = "This is a clean up request. Preserve the semantics of the input, but add nothing. make the input more concise and clear. Produce only the clean text."
    prompt_input = f"Clean up the following text and ensure there are no repetitions: {text}"
    return run(pre_prompt, prompt_input)

def rephrase(text : str) -> str:
    pre_prompt = "This is a rephrase request. Preserve the semantics of the input text, but change the wording of the text. You produce only the rephrased text."
    prompt_input = f"Rephrase the following text: {text}"
    return run(pre_prompt, prompt_input)

def eliminate_repetitions(text : str) -> str:
    pre_prompt = "This is a repetition reduction request. Reduce the number of repetitions in the given text. Produce only the corrected text."
    prompt_input = f"Reduce repetition in the following text: {text}"
    return run(pre_prompt, prompt_input)

def run(pre_prompt : str, prompt_input : str) -> str:
    output = replicate.run('meta/llama-2-70b-chat',
                           input={"prompt": f"{SYSTEM_PROMPT}\n\n{pre_prompt} {prompt_input}",
                                  "temperature":0.1,
                                  "top_p":0.9,
                                  "max_length":128,
                                  "repetition_penalty":1})
    return output
