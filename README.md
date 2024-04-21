# SQL-chatplot-

#  Talk to a Database  

This is an end to end LLM project based on Google Palm and Langchain. We are building a system that can talk to MySQL database. 
User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and
then executing that query on MySQL database. 

## Project Highlights


Text-based Personal Assistant(chatbot) 
•	Implemented a text-based personal assistant (chatbot) using LangChain.LLM (Large Language Model) involves integrating language processing capabilities with a conversational interface.
•	Implement the PaLM2 transformer architecture to interface with an SQL database,facilitated by the SQL database langchain.
•	Utilize the Hugging Face embedding model 'all-MiniLM-L6-v2' to create embedding vectors that facilitate the identification of word similarities
•	Develop ChromaDB, a vector database designed to store embedded vectors, which aims to reduce model bias through the application of few-shot learning techniques.


- We will build an LLM based question and answer system that will use following,
  - Google Palm LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - Chromadb as a vector store
  - Few shot learning
- In the UI, store manager will ask questions in a natural language and it will produce the answers


## Installation

1.Clone this repository to your local machine using:

```bash
  https://github.com/JayaPradhi/sql-chatplot-.git
```
2.Navigate to the project directory:

```bash
  cd 4_sqldb_
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

EXPLANATION:
1.	The workflow starts with the Store Manager asking a question in natural language (A).
2.	The system preprocesses the question  using NLP techniques.
3.	A question embedding is generated using Hugging Face transformers 
4.	Contextual information might be incorporated to enhance understanding (optional).
5.	The question embedding is matched to existing question-SQL template embeddings in Langchain 
6.	Google PaLM is fine-tuned on a few similar question-SQL template pairs using few-shot learning.
7.	PaLM then generates a candidate SQL query 
8.	The system connects to the MySQL database 
9.	The generated SQL query is executed on the database 
10.	The answer data is retrieved 
11.	Finally, the answer is formatted and presented to the store manager through the Streamlit UI

    EXAMPLE QUESTIONS:

    ![Screenshot 2024-04-15 233726](https://github.com/JayaPradhi/sql-chatplot-/assets/127920413/55f93876-683d-40bc-b5c5-17b539752674)

   	EXAMPLE QUESTIONS:

    ![Screenshot 2024-04-16 234331](https://github.com/JayaPradhi/sql-chatplot-/assets/127920413/d7761dcc-3b4e-464f-800a-bd8a7a702c98)



  
## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- few_shots.py: Contains few shot prompts
- .env: Configuration file for storing your Google API key.
