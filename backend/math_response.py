import openai
import os
from collections import deque
import re
import random
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError("API_KEY not set")
else:
    openai.api_key = os.environ.get("OPENAI_API_KEY")


class Problem():
    def __init__(self, prompt):
        self.q = deque()
        self.prompt = prompt
        self.get_response()

    def __next__(self):
        if len(self.q) == 1:
            self.get_response()
        return self.q.popleft()

    def __iter__(self):
        return self

    def get_response(self) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=.2,
            max_tokens=400,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        self.clean_response(response["choices"][0]["text"])

    def clean_response(self, response: str) -> None:
        response = response.strip().split("\n")
        # print(response)
        for problem in response:
            if not problem:
                continue
            problem = problem[3:]
            self.q.append(problem)

    def __repr__(self) -> str:
        return f"Questions: {self.q}"


def generate_prompt(category: str, difficulty: str) -> str:
    if not category or not difficulty:
        raise ValueError("No category or difficulty provided.")
    return f"Act like you are a math professor tutoring one of your students. Can you generate a list of 5 {category.lower()} problems that are of {difficulty.lower()} difficulty. Please format your problems in a way that can be interpreted by Wolfram Alpha for answers."
