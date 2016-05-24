from django.db import models

class Section (models.Model):
    class Meta:
        verbose_name = "Розділ"
        verbose_name_plural = "Розділи"

    section_name = models.CharField(max_length=200, verbose_name='Назва розділу')
    section_alias = models.SlugField(verbose_name='Alias розділу')
    section_image = models.ImageField(upload_to='images/section', verbose_name='Зображення', null=True, blank=True)

    def __str__(self):
        return self.section_name

class Test (models.Model):
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тести"

    test_name = models.CharField(max_length=200, verbose_name='Назва тесту')
    test_alias = models.SlugField(verbose_name='Alias тесту')
    test_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Розділ')
    test_image = models.ImageField(upload_to='images/test', verbose_name='Зображення', null=True, blank=True)
    def __str__(self):
        return self.test_name

class Question (models.Model):
    class Meta:
        verbose_name = "Питання"
        verbose_name_plural = "Питання"

    question_text = models.TextField(verbose_name='Текст питання')
    question_alias = models.SlugField(verbose_name='Alias питання')
    question_image = models.ImageField(upload_to='images/question', verbose_name='Зображення', null=True, blank=True)
    question_parretn_test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест(батьківський)')

    def __str__(self):
        return self.question_text

class Answer (models.Model):
    class Meta:
        verbose_name = "Відповідь"
        verbose_name_plural = "Відповіді"

    answer_text = models.TextField(verbose_name='Текст відповіді')
    answer_image = models.ImageField(upload_to='images/answer', verbose_name='Зображення', null=True, blank=True)
    answer_parretn_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Питання(батьківське)')
    answer_correct = models.BooleanField(verbose_name='Правильна/неправильна', default=False)

    def __str__(self):
        return self.answer_text