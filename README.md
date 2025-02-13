# Readme Maker

## About the project

This is a simple README.md file creator that uses Google's gemini model to create a markdown file. It takes user input and leverages the power of Google's Gemini API to generate a well-structured and informative README file based on a provided template.

## Technologies Used

*   Python
*   Flask
*   google-genai

## Getting started:

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:** (Version 3.7 or higher is recommended).  You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **pip:** Python package installer.  Generally comes with Python. Verify by running `pip --version` in your terminal.
*   **Google Cloud Account:** You need a Google Cloud account and a project enabled with the Gemini API.  You'll need to configure API keys or service accounts to access the API.  Refer to the Google Cloud documentation for setting this up.

Install the required Python packages:

```bash
pip install Flask google-genai python-dotenv
```

It is recommended to set up a virtual environment for your project to manage dependencies.  You can create one using:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate.bat # On Windows
```

Then run the `pip install` command above.

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/bkk31/readme-maker
    cd readme-maker
    ```

2.  (Optional) Create a `.env` file in the root directory to store your Gemini API key (strongly recommended for security):

    ```
    GOOGLE_API_KEY=<YOUR_GEMINI_API_KEY>
    ```

    Make sure to replace `<YOUR_GEMINI_API_KEY>` with your actual Gemini API key.  If you do not use a `.env` file, you will need to hardcode the API key into your Python script (not recommended).

### Usage

1.  Run the Flask application:

    ```bash
    python app.py # Or whatever your main app file is named
    ```

2.  Access the application in your web browser at `http://127.0.0.1:5000/` (or the address shown in your console output).

3.  Follow the instructions on the web interface to provide the necessary details for generating the README file.  The application should then generate and display the README content for you.

4.  Copy the generated README content and save it as `README.md` in your project's root directory.

## License

This project is licensed under the GNU Public License 3 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## Contact

If you have any questions or suggestions, please feel free to contact me at [bhargavakk13@gmail.com](mailto:bhargavakk13@gmail.com).

## Acknowledgement

*   This project utilizes the Google Gemini API.
*   We would like to thank the developers of Flask and google-genai libraries for their excellent work.