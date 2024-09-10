import os
import random
from faker import Faker


def add_tags_to_random_words(text, num_bold, num_italic):
    words = text.split()
    tagged_words = []
    for word in words:
        if num_bold > 0 and random.choice([True, False]):
            word = f'<b>{word}</b>'
            num_bold -= 1
        elif num_italic > 0 and random.choice([True, False]):
            word = f'<i>{word}</i>'
            num_italic -= 1
        tagged_words.append(word)

    return tagged_words


def main():
    faker = Faker()
    num_words = 1000
    num_bold = random.randint(1, 400)
    num_italic = random.randint(1, 400)

    text = faker.texts(nb_texts=1, max_nb_chars=num_words)[0]

    tagged_text = add_tags_to_random_words(text, num_bold, num_italic)

    # Annotate each word individually
    annotated_words = []
    for word in tagged_text:
        if word.startswith('<b>') and word.endswith('</b>'):
            annotated_words.append((word.strip('<b>').strip('</b>'), 'bold'))
        elif word.startswith('<i>') and word.endswith('</i>'):
            annotated_words.append((word.strip('<i>').strip('</i>'), 'italic'))
        else:
            annotated_words.append((word, 'normal'))

    # Create HTML content with annotated words
    html_content = f'''
    <html>
    <head>
        <title>Tagged Text</title>
    </head>
    <body>
        <!-- Annotated Data -->
        <p>Generated text contains {num_bold} bold words and {num_italic} italic words.</p>
        <!-- End Annotated Data -->'''

    # Add annotated words to HTML content
    for word, style in annotated_words:
        html_content += f'<span style="font-weight: {"bold" if style == "bold" else "normal"}; font-style: {"italic" if style == "italic" else "normal"}">{word}</span> '

    # Add spacing between lines
    html_content += '</body>\n\n</html>'

    output_directory = "C:\\Users\\Aarush\\Documents\\Prism\\Dataset Generation"
    output_filename = "outputfile1.html"
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f'HTML file saved to: {output_path}')


if __name__ == "__main__":
    main()
