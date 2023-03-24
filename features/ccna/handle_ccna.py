import random

from .ccnadict import ccnadict


import random

def handle_ccna(user_responses):
    # Create a list of question IDs, weighted based on user responses
    weighted_question_ids = []
    for i, question in enumerate(ccnadict):
        # Get the question ID and correct answer
        prefix = "ccna_"  # Unique prefix for CCNA questions
        question_id = prefix + str(i)
        correct_answer = question["correctanswer"].lower()

        # Compute the weight based on user responses
        weight = 1
        if question_id in user_responses:
            user_answer = user_responses[question_id].lower()
            if user_answer != correct_answer:
                weight += 1  # Increase weight for incorrect answers
            else:
                weight -= 1  # Decrease weight for correct answers

        # Add the question ID to the list with the appropriate weight
        weighted_question_ids.extend([question_id] * weight)

    # If all questions have been answered correctly, reset all the weights to 1
    if not weighted_question_ids:
        weighted_question_ids = [f"ccna_{i}" for i in range(len(ccnadict))]

    # If all questions have been answered correctly, reset all the weights to 1
    if not weighted_question_ids:
        weighted_question_ids = [f"{prefix}{i}" for i in range(len(ccnadict))]

    # Retrieve the selected question
    question = ccnadict[int(question_id.split('_')[1])]
    prompt = question["question"]
    answers = question["answers"]
    correct_answer = question["correctanswer"]

    # Format the response
    options = []
    for key, value in answers.items():
        if key != "correctanswer":
            options.append(f"**{key.upper()}**: {value}")
    options = "\n".join(options)
    if "reasoning" in question:
        reasoning = question["reasoning"]
        response = f"**Here's a CCNA question for you**:\n\n**Question**: {prompt}\n\n**Options**: \n{options}\n\n**Correct Answer**: ||{correct_answer}||\n\n**Reasoning**: ||{reasoning}||"
    else:
        response = f"**Here's a CCNA question for you**:\n\n**Question**: {prompt}\n\n**Options**: \n{options}\n\n**Correct Answer**: ||{correct_answer}||"

    return response, question_id