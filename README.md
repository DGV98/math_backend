# Math Generator Backend using Flask

Using flask and openai api, generate a list of math questions based on category and difficulty.

## math_response.py

Script used to provide a prompt to the OpenAI API. Handles generation of the prompt with a category and difficulty. Handles the response object and cleans the response into lists of questions using regular expressions. Uses the davinci model. 

## api.py

API for creating a request to generate a list of questions based on the response gotten from the OpenAI api. 
