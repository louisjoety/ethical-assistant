# Ethical Assistant

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Installation

### Prerequisites

* Python 3.8+
* An API key for Gemini (Google Generative AI)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ethical-assistant.git
   cd ethical-assistant
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```

   * On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.streamlit/secrets.toml` file in the root directory of your project, and add your Gemini API key:

   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run Home.py
```

Open the URL shown in your browser (usually `http://localhost:8501`).

Type your questions about ethical shopping or brands in the chat interface and get responses generated by Gemini.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for bug fixes and improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
