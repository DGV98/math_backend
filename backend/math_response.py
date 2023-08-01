import openai
import re

# load_dotenv()

# if not os.environ.get("OPENAI_API_KEY"):
#     raise RuntimeError("API_KEY not set")
# else:
#     openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_response(prompt) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a math professor tutoring one of your students.",
            },
            {
                "role": "user",
                "content": "Can you generate a list of 5 calculus problems that are of easy difficulty? Please format your problems LaTex format.",
            },
            {
                "role": "assistant",
                "content": "Here are the problems formatted in LaTex:\n\n1. Find the derivative of the function \\(f(x) = 3x^2 - 4x + 2\\).\n\n2. Evaluate the definite integral \\(\\int_{0}^{4} (2x + 1) \\, dx\\).\n\n3. Determine the limit \\(\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2}\\).\n\n4. Find the critical points of the function \\(g(x) = x^3 - 6x^2 + 9x\\).\n\n5. Calculate the area bounded by the curve \\(y = x^2\\) and the x-axis in the interval \\([-2, 2]\\).\n\nLet me know if you need any further assistance with these problems!",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["message"]["content"]


def clean_response(response: str):
    q = []
    pattern = r"^\n((?:\n|.)*?)\n$"
    matches = re.findall(pattern, response, flags=re.M)
    for i in matches:
        q.append(i[3:])
    return q


def generate_prompt(category: str, difficulty: str) -> str:
    if not category or not difficulty:
        raise ValueError("No category or difficulty provided.")
    return f"Can you generate a list of 9 {category.lower()} problems that are of {difficulty.lower()} difficulty? Please format your problems LaTex format."
