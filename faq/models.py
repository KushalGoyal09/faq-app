from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    question_hi = models.TextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_translated_question(self, lang='en'):
        try:
            return getattr(self, f'question_{lang}', self.question)
        except AttributeError:
            return self.question

    def save(self, *args, **kwargs):
        if not self.pk:  
            translator = Translator()
            try:
                self.question_hi = translator.translate(self.question, dest='hi').text
            except:
                pass
            try:
                self.question_bn = translator.translate(self.question, dest='bn').text
            except:
                pass
        super().save(*args, **kwargs)