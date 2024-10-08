import openai
from openai import OpenAI
from .managing_prompt import create_personalized_prompt
from .preprocessing_image import prepare_image_for_api
from ..improve_models import AnalysisResult
from ..improve_models import ImprovementSuggestion
from django.conf import settings
import json
from pydantic import BaseModel


class ImproveResult(BaseModel):
    environment: str
    objects_detected: str
    suggestion: str
    alternative: str



def analyze_image_with_openai(image_path, user):
    # Bild vorbereiten (resize und base64)
    openai.api_key = settings.OPENAI_API_KEY
    image_data_url = prepare_image_for_api(image_path)

    # Erstelle den personalisierten Prompt
    prompt = create_personalized_prompt(image_path, user)

    # Sende die Anfrage an die OpenAI API
    client = OpenAI()
    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "user", 
                "content": [
                    {
                        "type": "text", 
                        "text": prompt
                    },
                    {
                        "type": "image_url", 
                        "image_url": {
                            "url": image_data_url,
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        response_format=ImproveResult,
        max_tokens=500
    )

    improve_result = response.choices[0].message.parsed    
    return improve_result

def process_and_store_analysis_result(image, user, analysis_result):
    # Inhalt in ein JSON-Objekt umwandeln
    try:
        test = analysis_result.environment
    except json.JSONDecodeError:
        raise ValueError("Fehler beim Parsen der OpenAI-Antwort")

    # Extrahiere die Daten aus dem API-Ergebnis
    environment = analysis_result.environment
    objects_detected = analysis_result.objects_detected
    suggestion = analysis_result.suggestion
    alternative = analysis_result.alternative

    # Speichere die Analyseergebnisse im AnalysisResult-Modell
    analysis = AnalysisResult.objects.create(
        image=image,
        environment=environment,
        objects_detected=objects_detected
    )

    # Speichere die Verbesserungsvorschläge im ImprovementSuggestion-Modell
    ImprovementSuggestion.objects.create(
        analysis_result=analysis,
        suggestion_markdown=suggestion,
        alternative_markdown=alternative
    )
