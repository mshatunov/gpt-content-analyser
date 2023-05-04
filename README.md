# GPT Content Analyzer

GPT Content Analyzer is a Python-based tool that leverages the power of GPT-3.5 to analyze and summarize transcripts from meetings and video content. With the help of GPT, this tool aims to provide insights and key takeaways from the input transcripts.

## Requirements

- Python 3
- Create OpenAI API key
https://platform.openai.com/account/api-keys
![API key](https://media.cleanshot.cloud/media/45130/yPtQ9HYaz8jNXdMCdJFtO0auPF29btqbEu2RrQdS.jpeg?Expires=1683221900&Signature=BeQDYMPLvFjrAdnT8ZblAWc2~CdiqmE27GskBcGLDs3UmzJ0yO-Vt9jHUyUv9Oy3bgWq9IXtg9MkVEWXZ1BJHy7pwEUnsQrYKbpeeb8dMvYd8RO45rdF8-rBXk-2vctlNHDMi6aRIO8Tf5ZUV26V~8efd1bBOjkEpIhhNAOdeHPsIiGjJ3OlAdyD~qmAMw1xAOSnO0YDqaKuP7B5Yhv-~TfHlEjrreZyRu1dxDZzzt0toYWLCDiwjyEU9s1OGfQquODdRWj2YxDPx9WsrZKJH0x3y2zgTHbeeP21hOCLpk6D6YEtyKaE3AVYJDtyPOvxRYxGMVOl5TlETwTUjEoiMg__&Key-Pair-Id=K269JMAT9ZF4GZ)
- Set usage limits in preferences
https://platform.openai.com/account/billing/limits
![Usage limite](https://media.cleanshot.cloud/media/45130/jzOBjfCxldgb30sLuIxX4EGJIqIPkgq2DaVlg8bW.jpeg?Expires=1683221818&Signature=JDLuD24gNbwWRmNV5qjBDQ3-0FR3RL-6GGbo8MrfvN4-Zih1hGWD~yZO1v3EpvXX4781FCdX6o8vjHUwJk3Z4ckPN118KQ0Ck1izdYd-c3FX-28vXhijC4tTMmEqFvR0NYTaDCNxg-i1zRPY5tuxEK70~ZNBxlHML~e6R1YVmTldRtQc2xxEvd7428u8xHlQ0TzWyMwgMjCYA-DJnxoZuVEo38DEAXJ2BNJ9C3q2q7DOsTyT-V6e7hCw848qHRoFIITnPxgPBsxCktq0gfFRFuurQXKpEKOFrbvb796QNP0Imp7kC9rxdcqnnKcoqhgAND5gquzxwLbReCWPqLQnWg__&Key-Pair-Id=K269JMAT9ZF4GZ)

## Features

- Analyze transcripts from meetings to provide an overview, decisions made, and tasks assigned
- Summarize video transcripts to extract main points and conclusions
- Split long text into smaller chunks for efficient GPT processing

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
pip3 install -r requirements
```

## API Key Setup

1. Obtain an API key from OpenAI.
2. Create a file named `api_key` in the project root directory.
3. Copy and paste your API key into the `api_key` file and save it.

**Important:** Add `api_key` to your `.gitignore` file to avoid accidentally committing the API key to your repository.

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