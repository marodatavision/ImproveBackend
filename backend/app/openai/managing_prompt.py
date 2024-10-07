def create_personalized_prompt(image_path, user):
    prompt = f"""
    Analyze the image located at {image_path}. Based on the analysis of the environment and objects in the image, 
    provide improvement suggestions and an alternative. Personalize the suggestions based on the user's preferences and profile.

    User Profile:
    - Username: {user.username}
    - Email: {user.email}
    - Preferences: {user.preferences}

    Role of ChatGPT: You are an expert in the identified environment. 
    If it's an office, you act as a productivity consultant. 
    If it's a kitchen, you are a chef. If it's a workshop, you are a craftsman, and so on.

    The output should be in the following JSON format:
    {{
        "environment": "<identified_environment>",
        "objects_detected": <detected_objects>,
        "suggestion": "<personalized_suggestion_based_on_user_profile>",
        "alternative": "<alternative_suggestion_based_on_user_profile>"
    }}
    """
    return prompt
