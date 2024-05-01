from translate import Translator

translator = Translator(
    from_lang="pt",
    to_lang="ja")

try:
    with open('traducao_input.txt', encoding="utf-8", mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
        with open('traducao_output.txt',encoding="utf-8", mode='w') as file2:
            file2.write(translation)
except FileNotFoundError as e:
    print('check your file path!')