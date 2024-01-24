# English Proficiency Evaluator

This tool enables the evaluation of English proficiency in short stories using OpenAI's GPT-3.

## Getting Started

### Prerequisites

To use the English Proficiency Evaluator, you need Python installed on your system. Additionally, you'll require an OpenAI API key. If you don't have one, you can sign up for an API key on the OpenAI platform.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/english-evaluator.git
   cd english-evaluator
   ```

2. Create a virtual environment (venv) for the English evaluator. Replace `venv` with your preferred environment name:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   After activation, your command prompt should show the virtual environment's name, indicating that it's active.

4. Install the required packages within the virtual environment using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install the necessary packages, including the `openai` package.

## Running the English Evaluator
 
Replace `your-api-key` with your API Key.

To evaluate English proficiency in short stories, use the following command:

```bash
python evaluate_story.py input.json
```

Replace `evaluate_story.py` with the actual name of your Python file (if different) and `input.json` with the JSON input file you want to use.

## Deactivating the Virtual Environment

When you're finished using the English Evaluator, deactivate the virtual environment:

- On Windows:

  ```bash
  deactivate
  ```

- On macOS and Linux:

  ```bash
  deactivate
  ```

This ensures that dependencies are isolated and won't interfere with your system's global Python environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy evaluating English proficiency with ease!