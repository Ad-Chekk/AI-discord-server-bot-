%%writefile responses.py


import requests
import random
import calendar
import time
import wikipedia
from transformers import pipeline  # Import the summarizer pipeline
import language_tool_python
import nltk
from textblob import TextBlob

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Create an instance for grammar checking
tool = language_tool_python.LanguageTool('en-US')

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_response(message: str) -> str:
    define = ['wikipedia', 'wiki', 'wikihow', 'define']

    p_message = message.lower()

    if p_message == 'yolo':
        return "test.txt"

    if p_message in ['rock', 'paper', 'scissor', 'stone']:
        rcs = ['🪨Rock', '📃Paper', '✂️Scissor']
        return str(random.choice(rcs))

    if p_message == 'hello':
        return 'Hey there!😃🔥'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'month':
        return calendar.month(2023, 2)

    if p_message == 'password:admin':
        return '''password is correct
                    here are your confidential files:
                    example to store all files
                    https://www.google.com/
                    https://www.geeksforgeeks.com'''

    if p_message == 'link':
        return 'https://www.youtube.com/'

    if p_message == '!help':
        return ('`hey there!😃\n My commands are:\n'
                '> hello\n'
                '> roll\n'
                '> stone, paper, scissor\n'
                '> !help\n'
                '> link\n'
                '> remind "message to be displayed"\n'
                '> create file, edit file, peek file\n'
                '> password:<enter password>\n')

    msplit = p_message.split()  # Split the message into words

    if msplit[0] in define:
        search = ' '.join(msplit[2:])
        lin = int(msplit[1])
        result = wikipedia.summary(search, sentences=lin)
        return result

    if msplit[0] in ["summarize", "Summarize"]:  # Summarizer command
        try:
            text_to_summarize = ' '.join(msplit[1:])  # Get the text to summarize
            summary = summarizer(text_to_summarize, max_length=50, min_length=25, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error in summarization: {e}"

    if msplit[0] == 'checkgrammar':
        text_to_check = ' '.join(msplit[1:])
        matches = tool.check(text_to_check)
        corrections = [f"Error: {match.ruleId}, Message: {match.message}, Suggestions: {match.replacements}" for match in matches]
        return "Corrections:\n" + "\n".join(corrections) if corrections else "Your grammar looks good!"

    if msplit[0] == 'sentiment':
        text_to_analyze = ' '.join(msplit[1:])
        blob = TextBlob(text_to_analyze)
        return f"Polarity: {blob.sentiment.polarity}, Subjectivity: {blob.sentiment.subjectivity}"

    if msplit[0] == 'tokenize':
        text_to_tokenize = ' '.join(msplit[1:])
        tokens = nltk.word_tokenize(text_to_tokenize)
        return f"Tokens: {tokens}"

    if msplit[0] == 'pos':
        text_to_tag = ' '.join(msplit[1:])
        tokens = nltk.word_tokenize(text_to_tag)
        tags = nltk.pos_tag(tokens)
        return f"POS Tags: {tags}"

    if msplit[0] == 'remind':  # Reminder functionality
        count = len(msplit)
        reminder_message = ' '.join(msplit[2:count])
        time.sleep(10.0)  # Sleep for 10 seconds
        return reminder_message

    return 'Sorry, I didn\'t understand what you wrote. Try typing "!help" to view all my commands.'
