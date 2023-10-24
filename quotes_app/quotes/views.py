import os
import json
from django.shortcuts import render
from .forms import TagForm, AuthorForm, QuoteForm
from constants import FIELD_MAPPING

def read_data_from_json(file_name):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, '..'))
    file_path = os.path.join(parent_directory, file_name)
    
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        # Перейменуйте поля за допомогою словника FIELD_MAPPING
        renamed_data = []
        for item in data:
            renamed_item = {}
            for key, value in item.items():
                renamed_item[FIELD_MAPPING.get(key, key)] = value
            renamed_data.append(renamed_item)
    return renamed_data

def main(request):
    authors_data = read_data_from_json('authors.json')
    quotes_data = read_data_from_json('quotes.json')

    return render(request, 'quotes/index.html', {
        'authors': authors_data,
        'quotes': quotes_data,
    })


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': AuthorForm()})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': QuoteForm()})