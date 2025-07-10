# CodeInsight: AI-Powered Source Code Analysis Pipeline for Enhanced Code Quality

## Start the project by running the following command:
**STEPS:** *Clone the repository, navigate to the project directory, and run the following command:*
```bash
https://github.com/jcm-ai/CodeInsight-AI-Powered-Source-Code-Analysis-Pipeline-for-Enhanced-Code-Quality.git
```
**STEP 1:** Create a `virtual environment` or `conda environment` using the following command:
```bash
conda create --name codeinsight python=3.10 -y
```
*Incase if you get error (for example: CondaError: Run 'conda init' before 'conda activate') when activate environment, use below command:*
```bash
source activate base
```
Activate the `virtual environment` or `conda environment` using the following command:
```bash
conda activate codeinsight
```
**STEP 2:** Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```
### Create a `.env` file and add the following environment variables:

```bash
OPENAI_API_KEY="*****************************"
```
And then run the following command to start the project:
```bash
python app.py
```
Now, we can access the application locally at: `http://localhost:8080`

### Technologies Used:
- Python : A high-level programming language
- Langchain : A framework for building applications with LLMs
- OpenAI API : The OpenAI API provides developers with programmatic access to OpenAI's powerful AI models, such as GPT-3, GPT-4 etc
- GPT 3 : An advanced language model from OpenAI
- ChromaDB : A vector database for storing and querying embeddings
- Flask : A micro web framework for Python web development
