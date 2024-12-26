# speech-to-text-tools

## TXT to Word Converter

This Python script converts a plain text file (.txt) into a Microsoft Word document (.docx). It ensures that the content from the text file is transferred as a single paragraph in the Word document, maintaining encoding compatibility for special characters.

### How It Works

1. **Input File**: Place your `.txt` file in the same directory as the script. Ensure the `audio_track` variable matches the file name (without the extension).
2. **Processing**:
   - Reads the content of the `.txt` file with UTF-8 encoding to preserve special characters (e.g., accents, ñ).
   - Creates a Word document and inserts the text as a single paragraph.
3. **Output File**: The Word document is saved in the same directory with the same base name as the input `.txt` file.

### Key Features
- **Error Handling**: 
  - Alerts the user if the input file is missing.
  - Provides information on any unexpected errors during execution.
- **Encoding**: Ensures proper handling of special characters for Spanish and other languages.

### Code Structure
- `txt_to_word(txt_file, word_file)`: The main function handling the conversion process. It reads the text file, writes the content to a `.docx` file, and saves it.
- Variables:
  - `audio_track`: Specifies the base name for the input and output files.
  - `txt_file`: Full path of the `.txt` file.
  - `word_file`: Full path for the resulting `.docx` file.

### Requirements
- Python 3.x
- `python-docx` library (`pip install python-docx`)

Run the script to seamlessly convert your text files into Word documents with a simple, automated process!


# SRT to DOCX Converter

This Python script converts a SubRip Subtitle (SRT) file into a formatted Microsoft Word document (DOCX). It extracts timestamps and subtitle text from the SRT file, formats the timestamps in bold, and organizes the text into paragraphs in the DOCX file.

## How It Works

1. **Input File**: Place your `.srt` file in the same directory as the script and ensure the `audio_track` variable matches your file's name.
2. **Processing**: The script reads the SRT file line by line:
   - Identifies timestamps and subtitles.
   - Formats the timestamps in bold and organizes the subtitles into paragraphs.
3. **Output File**: The resulting DOCX file is saved with the same base name as the SRT file.

### Key Functions
- `process_buffer(buffer)`: Extracts timestamps and subtitles from SRT data.
- `write_to_doc(doc, timestamp, subtitle_text)`: Writes formatted content to the DOCX file.
- `srt_to_docx(srt_file, docx_file)`: Handles the conversion process and saves the DOCX file.

## Requirements
- Python 3.x
- `python-docx` library (`pip install python-docx`)

Run the script and generate professional Word documents from your subtitle files with ease!
