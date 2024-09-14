# Building a Discord Chatbot with LLaMA 3 for Student Q&A

An intelligent Discord chatbot designed to enhance the student learning experience by providing quick, automated answers to questions using LLaMA 3 and Retrieval-Augmented Generation (RAG).

![Discord Chatbot Demo](assets/demo.gif)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Prerequisites](#prerequisites)

## Introduction

As a data science research assistant, I noticed that students often struggled to find relevant information from lecture slides and past discussions efficiently. To address this, I developed an AI-powered Discord chatbot using LLaMA 3 that automatically responds to student questions by retrieving and summarizing information from lecture materials and previous chats.

## Features

- **Natural Language Understanding**: Utilizes LLaMA 3 to comprehend and respond to a wide range of student queries.
- **Retrieval-Augmented Generation (RAG)**: Combines question understanding with context retrieval for accurate answers.
- **Efficient Data Retrieval**: Employs a Chroma vector database for quick similarity searches.
- **Scalable Deployment**: Runs continuously on an AWS cloud server to handle multiple queries simultaneously.
- **Interactive Interface**: Includes a Gradio web interface for testing and interaction.

## Architecture Overview

1. **Data Extraction**: Lecture slides are converted from PDFs to text using PyPDF2.
2. **Text Chunking**: The extracted text is split into manageable chunks using LangChain's `RecursiveCharacterTextSplitter`.
3. **Embedding Generation**: Each text chunk is converted into embeddings via Ollama's LLaMA 3 model.
4. **Vector Storage**: Embeddings are stored in a Chroma vector database for efficient retrieval.
5. **Question Processing**: The Discord bot captures student questions and formats them into prompts.
6. **Context Retrieval**: Relevant text chunks are retrieved based on the question's context.
7. **Response Generation**: LLaMA 3 generates a coherent answer using the retrieved context.
8. **User Interaction**: The bot sends the answer back to the student on Discord.

## Prerequisites

- Python 3.8 or higher
- Discord account and server
- AWS account or any cloud service provider
- The following Python packages:
  - `ollama`
  - `langchain`
  - `langchain-community`
  - `chromadb`
  - `gradio`
  - `discord.py`
  - `PyPDF2`
