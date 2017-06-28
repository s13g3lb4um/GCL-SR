from django.db import models
from django.utils import timezone
from pydub import AudioSegment
from django.conf import settings
from os import listdir, remove
from . utils import WIT_API_KEY, GOOGLE_CLOUD_SPEECH_CREDENTIALS
import speech_recognition as sr


class Speech_Recognition(models.Model):
    audioFile = models.FileField(upload_to='audios/%Y/%m/%d/')
    description = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now)

    def recognition(self, audio=None):
        if audio is None:
            AUDIO_FILE = self.audioFile.path
        else:
            AUDIO_FILE = audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = recognizer.record(source)
            try:
                # temp_text = recognizer.recognize_google(audio, None, language="es-419")
                temp_text = recognizer.recognize_wit(audio, key=WIT_API_KEY)
                self.text += temp_text + " "
                self.save()
            except sr.UnknownValueError:
                print("No es posible entender el audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; \
                    {0}".format(e))

    def analyze_audio(self):
        self.text = "test "
        AUDIO_FILE = self.audioFile.path
        file_in = AudioSegment.from_wav(AUDIO_FILE)
        if int(file_in.duration_seconds) > 5:
            for a in range(0, int(file_in.duration_seconds), 5):
                b = a * 1000
                fileOut = file_in[b:b + 5000]
                fileOut.export(settings.MEDIA_ROOT +
                               "/temp/part" + str(a) + ".wav", format="wav")
            for audio_part in listdir(settings.MEDIA_ROOT + "/temp/"):
                self.recognition(settings.MEDIA_ROOT + "/temp/" + audio_part)
        else:
            self.recognition()

        if len(listdir(settings.MEDIA_ROOT + "/temp/")) > 0:
            for temp_file in listdir(settings.MEDIA_ROOT + "/temp/"):
                remove(settings.MEDIA_ROOT + "/temp/" + temp_file)

    def __str__(self):
        return self.description + " - " + str(self.created_date)
