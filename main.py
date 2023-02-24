# Import necessary libraries
from art import tprint
from gtts import gTTS
from pathlib import Path

# Define a function that converts PDF to MP3
def pdf_to_mp3(file_path='test.pdf', language='en'):
    # Check if the file path exists and if the file is a PDF
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # Print the original file name and start processing
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        # Use pdfplumber to extract the text from the PDF file
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        # Join the extracted text and replace newlines with spaces
        text = ''.join(pages)
        text = text.replace('\n', '')
        # Convert the text to speech using the gTTS API
        my_audio = gTTS(text=text, lang=language, slow=False)
        # Get the file name without the extension and save the MP3 file
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        # Return a success message
        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'
    else:
        # Return an error message if the file path or file type is invalid
        return 'File not exists, check the file path!'

# Define the main function
def main():
    # Print a fancy title using the tprint function from the art library
    tprint('PDF>>TO>>MP3', font='bulbhead')
    # Ask the user for the file path and language
    file_path = input("\nEnter a file`s path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    # Call the pdf_to_mp3 function and print the result
    print(pdf_to_mp3(file_path=file_path, language=language))

# Call the main function if this script is being run directly
if __name__ == '__main__':
    main()
