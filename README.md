# GPT Content Analyzer

GPT Content Analyzer is a Python-based tool that leverages the power of GPT-3.5 to analyze and summarize transcripts from meetings and video content. With the help of GPT, this tool aims to provide insights and key takeaways from the input transcripts.

## Features

- Analyze transcripts from meetings to provide an overview, decisions made, and tasks assigned
- Summarize video transcripts to extract main points and conclusions
- Split long text into smaller chunks for efficient GPT-3 processing

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mshatunov/gpt-content-analyser.git
```

2. Change to the project directory:
```bash
cd gpt-content-analyser
```

3. Install the required dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage
1. Ensure you have your GPT-3 API key in the api_key variable.
2. Run the script using Python 3:
```
python3 analyser.py
```

3. Follow the prompts to input the file name and content type (1 for meeting, 2 for video).
4. The script will process the input file, generate summarized content, and save the results in an output file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.