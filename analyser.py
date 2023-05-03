import re
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi


def get_api_key(file_name):
    """Read the API key from a file."""
    with open(file_name, 'r') as file:
        return file.read().strip()

def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        return transcript_text
    except Exception as e:
        print(f"Ошибка при получении субтитров с YouTube: {e}")
        return None

def generate_text(api_key, model, prompt, advise):
    """Generate text using GPT model with given prompt and advise."""
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': model,
        'messages': [
            {
                'role': 'user',
                'content': advise + prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        if response.ok:
            choice = response.json()['choices'][0]
            total_tokens = response.json()['usage']['total_tokens']
            return total_tokens, choice['message']['content']
        else:
            raise Exception('Failed to generate text')
    except requests.exceptions.HTTPError as error:
        print(f"Failed to generate text: {error}")
        print(f"API Response: {response.text}")
        return None, None


def split_text(text, max_words):
    """Split text into smaller chunks based on maximum words allowed."""
    words = text.split()
    result = []
    current_chunk = []

    for word in words:
        if len(current_chunk) < max_words:
            current_chunk.append(word)
        else:
            result.append(' '.join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        result.append(' '.join(current_chunk))
    return result


def read_file(file_name):
    """Read the content of a file."""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def write_to_file(file_name, text_chunks):
    """Write the text chunks to a file."""
    with open(file_name, 'w', encoding='utf-8') as file:
        for chunk in text_chunks:
            if chunk is not None:
                file.write(chunk + '\n\n')


def main():
    content_type = input("Введите тип контента (1 - встреча, 2 - видео): ")

    if content_type == "1":
        file_name = input("Введите имя файла: ")
        text = read_file(file_name)
        output_file = f"{file_name.rstrip('.txt')}_output.txt"
    elif content_type == "2":
        video_id = input("Введите идентификатор видео на YouTube: ")
        text = get_youtube_transcript(video_id)
        output_file = f"{video_id}_output.txt"
    else:
        print("Некорректный тип контента")
        return
    
    api_key_file = "api_key"
    api_key = get_api_key(api_key_file)
    model = "gpt-3.5-turbo"
    MAX_TOKENS = 1400

    text_chunks = split_text(text, MAX_TOKENS)

    # Set up the advice based on content type
    if content_type == "1":
        advise = "Я хочу, чтобы ты действовал как личный помощник руководителя. Предоставь мне основные выводы из записи встречи, указав общую информацию, решения, принятые на встрече, и действия, которые необходимо совершить. Если из текста понятно, кто будет выполнять задачи, укажи возможного исполнителя в скобках."
    elif content_type == "2":
        viewing_purpose = input("Введите цель просмотра видео: ")
        advise = f"Я хочу, чтобы вы действовали в качестве личного помощника исследователя, предоставляя основные выводы из представленного мною текста с учетом цели просмотра '{viewing_purpose}'. Сосредоточьтесь на ключевых выводах, которые могут быть полезными для дальнейшей работы, а не на общей информации. Проанализируйте текст и предоставьте мне только самые важные выводы. Каждый вывод делай с новой строки, на русском языке, перед выводом вставляй тире. Вот текст для анализа:"        
    else:
        print("Некорректный тип контента")
        return

    text_responses = []
    for chunk in text_chunks:
        usage, text_response = generate_text(api_key, model, chunk, advise)
        text_responses.append(text_response)
        print(f"Processed part {len(text_responses)} of {len(text_chunks)}. Current chunk: {chunk[:100]}...")
        if usage:
            print(f"API usage: {usage}")

    write_to_file(output_file, text_responses)
    print(f"Результат работы программы сохранен в файл {output_file}")


if __name__ == "__main__":
    main()
