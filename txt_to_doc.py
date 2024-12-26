"""
author: Sofia Barreto Ojeda
"""

from docx import Document

audio_track = "audio-01" 
def txt_to_word(txt_file, word_file):
    try:
        with open(f'{audio_track}.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        doc = Document()
        doc.add_paragraph(text)
        doc.save(word_file)
        print(f"Document now saved as Word in: {word_file}")
    
    except FileNotFoundError:
        print(f"The file {txt_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

txt_file = f"{audio_track}.txt"  
word_file = f"{audio_track}.docx"  

txt_to_word(txt_file, word_file)
