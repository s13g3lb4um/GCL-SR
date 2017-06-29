from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

EXTENSIONS_ALLOW = ['.mp3', '.wav', '.flv', '.ogg', 'm4a']


def audioFile_validator_manual(value):
    message_text = _(
        "La extension del archivo: " + str(value) + " No está permitida. " +
        "Las extensiones permitidas son: " + str(EXTENSIONS_ALLOW) + "."
    )
    code_text = 'invalid_extension'
    pass_filter = False
    for pos in EXTENSIONS_ALLOW:
        if pos in str(value):
            pass_filter = True
    if pass_filter is False:
        raise ValidationError(message=message_text, code=code_text)


def getExtension(value):
    for pos in EXTENSIONS_ALLOW:
        if pos in str(value):
            return str(EXTENSIONS_ALLOW.index(pos))
