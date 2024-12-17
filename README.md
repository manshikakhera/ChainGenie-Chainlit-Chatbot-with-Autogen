# ChainGenie-Chainlit-Chatbot-with-Autogen
🤖 ChainGenie: Chainlit Chatbot with Autogen
ChainGenie is an AI-powered chatbot built using Chainlit and Autogen. It offers advanced conversational capabilities, data visualization, and seamless integration with Computer Vision and GPT models. Designed for backend applications, ChainGenie can analyze data, visualize insights, and provide intelligent responses through a RESTful API.

📌 Features
Conversational AI: Engages users with intelligent and context-aware conversations.
File Upload Support: Users can upload CSV and Excel files for data visualization.
Data Visualization: Automatically generates graphs and visual insights from uploaded data.
Computer Vision Integration: Analyzes images and extracts text using OCR.
GPT Integration: Provides contextual insights using OpenAI's GPT model.
RESTful API: Built with Flask and deployed using Azure Functions.
.NET Integration: Easily consumable API endpoints for .NET applications.
🛠️ Technology Stack
Component	Technologies
Frontend	Chainlit
Backend	Python, Flask, Azure Functions
AI Models	OpenAI GPT, Autogen
Computer Vision	OpenCV, EasyOCR
Data Visualization	Matplotlib, Pandas
Deployment	Azure, Docker (optional)
.NET Integration	.NET Core, HttpClient
🚀 How It Works
Chatbot Interaction: Users interact with the chatbot via Chainlit.
File Upload: Upload CSV/Excel files directly through the chatbot interface.
Visualization: Upon request, ChainGenie generates visualizations from the uploaded data.
Image Analysis: Upload images to extract text and pass insights to GPT for analysis.
API Integration: Expose Flask API endpoints for .NET consumption.
📂 Project Structure
plaintext
Copy code
.
├── agents/
│   ├── chainlit_agents.py      # Custom agents for visualization and processing
│
├── app.py                      # Main Chainlit chatbot and API entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .env                        # Environment variables (API keys, configurations)
📝 Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/ChainGenie.git
cd ChainGenie
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory:

plaintext
Copy code
API_KEY=your_openai_api_key
AZURE_API_KEY=your_azure_api_key
AZURE_API_BASE_URL=your_azure_base_url
MODEL_NAME=gpt-4o-aus-team01
4. Run the Application
bash
Copy code
chainlit run app.py
Access the app at http://localhost:8000.

📊 Example API Request
Using cURL to send a file upload request:

bash
Copy code
curl -X POST "http://localhost:8000/upload" -H "Content-Type: multipart/form-data" -F "file=@data.xlsx"
🤖 Usage Scenarios
Data Analysis: Upload datasets and generate visual insights.
Document Processing: Extract and analyze text from images or scanned documents.
Intelligent Chatbot: Engage in conversations for AI-driven assistance.
.NET Integration: Seamlessly integrate with .NET projects using RESTful APIs.
🧪 Testing
Run unit tests using unittest:

bash
Copy code
python -m unittest discover tests
📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by [Your Name]
Role: Software Development Engineer (SDE)
Expertise: AI, Python Backend, NLP, and API Development

🌐 Connect
LinkedIn: Your LinkedIn Profile
GitHub: Your GitHub Profile
This README provides all the essential information, making it easy for users and collaborators to understand and utilize the project.
