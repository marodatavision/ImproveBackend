def create_personalized_prompt(image_path, user, language="german"):
    prompt = f"""
    Analyze the image located at {image_path}. 
    Try to detect all objects in the image in the best precision and finest granularity and remember the objects with their possibilities as objects_detected. 
    Based on the analysis of the environment and objects in the image, 
    provide detailed improvement suggestions and alternative. Personalize the suggestions and alternative based on the user's preferences and profile.

    User Profile:
    - Preferences: {user.preferences}

    Role of ChatGPT: You are an expert in the identified environment. 
    If it's an office, you act as a productivity consultant. 
    If it's a kitchen, you are a chef. If it's a workshop, you are a craftsman, and so on.

    The output should fit into the following python class via Structured Outputs. 
    Make sure you have a corresponding value for all attributes. 
    Also make sure you put a comma-separated list of objects as strin in objects_detected.
    Translate the whole output to the {language} language:

    class ImproveResult(BaseModel):
        environment: str
        objects_detected: str
        suggestion: str
        alternative: str
    """
    return prompt
