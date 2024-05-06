import openai

def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in pounds and height in inches.
    Formula: BMI = (weight / (height ** 2)) * 703
    """
    return (weight / (height ** 2)) * 703

def interpret_bmi(bmi):
    """
    Interpret BMI value according to WHO guidelines.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def generate_diet_plan(weight_goal):
    """
    Generate a diet plan based on weight goals using OpenAI API.
    """
    openai.api_key = 'sk-proj-EMw2AyWfuLyJ3kukG4VKT3BlbkFJoDzhsMaTiWo37Yl7Wm1v'
    prompt = f"Generate a diet plan for one day for someone looking to {weight_goal} weight. The diet plan should include healthy and balanced meals. Include how many calories they should eat to achive their goal."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].text.strip()

