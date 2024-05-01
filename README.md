# SQL-chatplot-

🔍 Project Title: Talking to Databases with Language Models

📝 Project Description:
This project showcases an innovative approach to interacting with MySQL databases using natural language. Leveraging cutting-edge technologies like Google Palm LLM and Langchain,  built a system that enables users to ask questions in plain English and receive accurate responses by translating those questions into SQL queries and executing them on MySQL databases.

🌟 Project Highlights:

Text-based Personal Assistant (Chatbot): Implemented a text-based personal assistant using LLM, integrating language processing capabilities with a conversational interface.
PaLM2 Transformer Architecture: Utilized the PaLM2 transformer architecture to interface with an SQL database, powered by the Langchain framework.
Hugging Face Embeddings: Employed the 'all-MiniLM-L6-v2' Hugging Face embedding model to create embedding vectors, enhancing word similarity identification.
Streamlit for User Interface: Developed a user-friendly UI using Streamlit, allowing store managers to ask questions in natural language and receive instant answers.
ChromaDB for Vector Storage: Designed ChromaDB, a vector database for storing embedded vectors, aimed at reducing model bias through few-shot learning techniques.
Excited to showcase the power of language models in bridging the gap between human language and database interactions! 💬🔍


## Installation

1.Clone this repository to your local machine using:

```bash
  https://github.com/JayaPradhi/sql-chatplot-.git
```

2. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
2.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run streamlit.py

```

EXPLANATION:
1.	The workflow starts with the Store Manager asking a question in natural language .
2.	The system preprocesses the question  using NLP techniques.
3.	A question embedding is generated using Hugging Face transformers 
4.	Contextual information might be incorporated to enhance understanding .
5.	The question embedding is matched to existing question-SQL template embeddings in Langchain 
6.	Google PaLM is fine-tuned on a few similar question-SQL template pairs using few-shot learning.
7.	PaLM then generates a candidate SQL query 
8.	The system connects to the MySQL database 
9.	The generated SQL query is executed on the database 
10.	The answer data is retrieved 
11.	Finally, the answer is formatted and presented to the store manager through the Streamlit UI

    EXAMPLE QUESTIONS:

    ![image](https://github.com/JayaPradhi/sql-chatplot-/assets/127920413/7a749f3f-1623-4c53-a35c-52a5bb4f3528)


   	EXAMPLE QUESTIONS:

    ![image](https://github.com/JayaPradhi/sql-chatplot-/assets/127920413/7d589b13-f92f-4be6-beef-e4e4f2958e4f)





  

