from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def audioFile_validator_manual(value):
    ext = ['.mp3', '.wav', '.flv', '.ogg']
    message_text = _(
        "La extension del archivo: " + str(value) + " No está permitida. " +
        "Las extensiones permitidas son: " + str(ext) + "."
    )
    code_text = 'invalid_extension'
    pass_filter = False
    for pos in ext:
        if pos in str(value):
            pass_filter = True
    if pass_filter is False:
        raise ValidationError(message=message_text, code=code_text)
