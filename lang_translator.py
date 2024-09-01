from googletrans import Translator

translator = Translator()

text =  str(input("Enter the string you want to translate it to --> "))

translated = translator.translate(text, dest = 'hi')
print(translated.text)
