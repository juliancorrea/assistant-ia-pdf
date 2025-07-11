# 🛠️ Intelligent Assistant - AI-Powered Support System

An intelligent customer support system that uses AI to answer questions based on technical documentation in PDF format. The system processes PDF documents, creates a vectorized knowledge base, and responds to questions using the OpenAI API.

## 🚀 Features

- **PDF Processing**: Automatically loads and processes PDF documents
- **Knowledge Base**: Creates a vectorized database using FAISS for efficient search
- **Conversational AI**: Uses ChatGPT to generate contextualized responses
- **User-Friendly Interface**: Web interface built with Streamlit
- **Support Simulation**: Simulates a multi-step customer support workflow
- **Contextualized Responses**: Answers based on specific document content

## 🖥️ Interface

![Application Preview](preview.png)

## 🛠️ Technologies Used

- **Python 3.12+**
- **Streamlit** - Web interface
- **LangChain** - Framework for LLM applications
- **OpenAI API** - Language model (gpt-4o-mini)
- **FAISS** - Efficient vector search
- **PyPDF** - PDF document processing
- **python-dotenv** - Environment variable management
- **NumPy & Pandas** - Data processing

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- PDF document to serve as knowledge base

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/assistente-ia-pdf.git
   cd assistente-ia-pdf
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Add your PDF document**
   
   Place your PDF document in the project root with the name `document.pdf`

## 🚀 How to Use

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**
   
   The application will automatically open in your browser at `http://localhost:8501`

3. **Ask your question**
   
   Type your question in the text field and click "Execute support" or press Enter

4. **Wait for processing**
   
   The system will simulate a multi-step support process and return an answer based on the PDF document

## 📁 Project Structure

```
assistente-ia-pdf/
├── app.py              # Main application
├── document.pdf        # Base PDF document (add your own)
├── preview.png         # Interface screenshot
├── .env               # Environment variables (not committed)
├── .gitignore         # Files to be ignored by Git
├── README.md          # This file (Portuguese)
├── README_EN.md       # English documentation
├── requirements.txt   # Project dependencies
├── LICENSE            # MIT License
└── run.sh             # Quick execution script
```

## 🔧 Advanced Configuration

### Customizing the Model

To change the OpenAI model or adjust parameters:

```python
# In app.py file, line ~74
llm=ChatOpenAI(
    temperature=0,  # Adjust creativity (0-1)
    model_name="gpt-4o-mini",  # or "gpt-4o", "gpt-3.5-turbo"
    openai_api_key=openai_api_key
)
```

### Changing the Base Document

1. Replace the `document.pdf` file with your document
2. Restart the application to reprocess the new document

## 🎯 Use Cases

- **Technical Support**: Support based on technical manuals
- **Intelligent FAQ**: Automatic answers based on documentation
- **Training**: Query system for training materials
- **Compliance**: Queries about company policies and procedures

## 🔒 Security

- API keys are loaded via environment variables
- The `.env` file should not be committed to the repository
- Use `.gitignore` to protect sensitive information

## 🐛 Troubleshooting

### Error: "Define the OPENAI_API_KEY environment variable"
- Check if the `.env` file exists and contains the correct key
- Make sure the API key is valid

### Error: "Could not load PDF manual"
- Check if the `document.pdf` file exists in the project root
- Make sure the PDF file is not corrupted

### Dependency errors
- Run: `pip install --upgrade pip`
- Reinstall dependencies: `pip install -r requirements.txt`

### Architecture Error on Mac M1/M2
If you encounter errors like "(mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e' or 'arm64')":

1. **Remove current virtual environment**:
   ```bash
   rm -rf venv
   ```

2. **Create a new ARM64 virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Update tools**:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Quick Start Script
Use the `run.sh` script for automatic execution:
```bash
./run.sh
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


⭐ If this project helped you, consider giving it a star on the repository!
