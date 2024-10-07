# app/signals.py

import logging
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

logger = logging.getLogger(__name__)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Sendet eine HTML-E-Mail mit einem Passwort-Reset-Link, wenn ein Token erstellt wird.
    """
    try:
        # Erstelle die UID des Benutzers
        #uid = urlsafe_base64_encode(force_bytes(reset_password_token.user.id))
        uid = reset_password_token.user.id
        
        # Erstelle den Reset-Link, der auf dein Frontend verweist
        reset_url = f"{settings.FRONTEND_URL}/password_reset_confirm/?uid={uid}&token={reset_password_token.key}"

        # Aktuelles Jahr für den Footer
        current_year = timezone.now().year

        # Render das HTML-Template
        html_content = render_to_string('emails/password_reset_email.html', {
            'user': reset_password_token.user,
            'reset_url': reset_url,
            'current_year': current_year,
        })

        # Erstelle die E-Mail-Nachricht
        email = EmailMultiAlternatives(
            subject="Passwort zurücksetzen",
            body=f"Hallo {reset_password_token.user.username},\n\nSie haben eine Anfrage zum Zurücksetzen Ihres Passworts gestellt.\n\nKlicken Sie auf den folgenden Link, um Ihr Passwort zurückzusetzen:\n{reset_url}\n\nWenn Sie diese Anfrage nicht gestellt haben, ignorieren Sie bitte diese E-Mail.\n\nVielen Dank!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[reset_password_token.user.email],
        )

        # Füge den HTML-Inhalt hinzu
        email.attach_alternative(html_content, "text/html")

        # Sende die E-Mail
        email.send()
        logger.debug(f"Passwort-Reset-E-Mail an {reset_password_token.user.email} gesendet.")
    except Exception as e:
        logger.error(f"Fehler beim Senden der Passwort-Reset-E-Mail: {e}")
