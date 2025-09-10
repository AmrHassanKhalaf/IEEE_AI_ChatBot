


# IEEE_AI_ChatBot

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup & Installation](#setup--installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview
IEEE_AI_ChatBot is an intelligent chatbot designed for the IEEE Beni-Suef Student Branch. It helps students and members get instant, accurate answers about academic activities, events, technical and non-technical committees, and IEEE resources. The bot leverages state-of-the-art AI and retrieval technologies to deliver a seamless support experience.

## Features
- Fast, accurate answers to academic and organizational questions
- Supports both Arabic and English languages
- Interactive, user-friendly Gradio interface
- Retrieves information from PDFs and custom knowledge sources
- Secure and privacy-focused
- Context-aware responses using conversation history

## Tech Stack
- **LangChain**: Orchestrates AI chains and retrieval logic
- **Gemini (Google GenAI)**: Advanced language model for generating responses
- **Pinecone**: Vector database for storing and retrieving document embeddings
- **Gradio**: Web-based UI for chatbot interaction
- **HuggingFace Embeddings**: For semantic search and document understanding

## Setup & Installation
1. **Clone the repository:**
	```bash
	git clone https://github.com/AmrHassanKhalaf/IEEE_AI_ChatBot.git
	cd IEEE_AI_ChatBot
	```
2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
3. **Set up environment variables:**
	- Create a `.env` file in the root directory with your API keys:
	  ```env
	  PINECONE_API_KEY=your_pinecone_key
	  GOOGLE_API_KEY=your_google_genai_key
	  ```
4. **Prepare your data:**
	- Place PDF files and other resources in the `data/` directory as needed.

## Usage
Run the chatbot locally:
```bash
python app.py
```
The Gradio interface will launch in your browser. Enter your questions and get instant answers!

## Project Structure
```
IEEE_AI_ChatBot/
├── app.py                # Main application (Gradio UI & chatbot logic)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not committed)
├── src/
│   ├── helper.py         # PDF loading, text splitting, embeddings
│   ├── prompt.py         # System prompt for chatbot behavior
│   └── __init__.py
├── data/                 # PDF and resource files
├── static/               # CSS and static assets
├── templates/            # HTML templates
├── research/             # Jupyter notebooks and experiments
└── README.md
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Make your changes and commit them
4. Push to your fork and open a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
