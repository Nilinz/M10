from django import forms
from .models import Quote, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    tags = forms.CharField(max_length=255, label='Tags', required=True, help_text='Enter tags separated by commas')
    author = forms.CharField(max_length=255, label='Author', required=True)

    class Meta:
        model = Quote
        fields = ['quote']
# class QuoteForm(forms.ModelForm):
# #     author_name = forms.CharField(max_length=255, required=True, label='Author')

#     class Meta:
#         model = Quote
#         fields = ['quote', 'tags', 'author']  

# class QuoteForm(forms.ModelForm):
#     # Поле для введення тексту тегів
#     tags = forms.CharField(max_length=255, required=False, help_text="Enter tags separated by commas")

#     # Поле для введення імені автора
#     author_name = forms.CharField(max_length=255, required=True, label='Author')

#     class Meta:
#         model = Quote
#         fields = ['quote', 'tags', 'author_name']

#     def clean_tags(self):
#         # Отримати значення поля тегів
#         tags = self.cleaned_data['tags']
#         # Розділити теги за комою і видалити пробіли
#         tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
#         # Повернути список тегів
#         return tag_list

#     def clean_author_name(self):
#         # Перевірити, чи існує автор з таким ім'ям у базі даних
#         author_name = self.cleaned_data['author_name']
#         try:
#             author = Author.objects.get(fullname=author_name)
#         except Author.DoesNotExist:
#             # Якщо автор не існує, створити його
#             author = Author.objects.create(fullname=author_name)
#         # Повернути об'єкт автора
#         return author