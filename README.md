# CSV Data Processor with Chainlit Integration

This project loads data from multiple CSV files, processes it into chunks, creates embeddings using a HuggingFace model, and sets up a Chainlit application for conversational query handling.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

This project demonstrates how to:
1. Load data from multiple CSV files.
2. Process the data into manageable chunks.
3. Create embeddings using a pre-trained HuggingFace model.
4. Set up a Flask API server.
5. Integrate with Chainlit for conversational AI capabilities.

## Features

- Load and combine data from multiple CSV files.
- Split data into chunks for efficient processing.
- Generate embeddings using the `sentence-transformers/all-mpnet-base-v2` model.
- Expose a Flask API endpoint for querying the processed data.
- Set up a Chainlit application for interactive querying.

## Setup

1. **Clone the repository:**
    ```bash
    git https://github.com/KelvinTichana-creator/RAG-mistralAI
    cd RAG-mistralAI
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure paths to your CSV files:**
    Update the `csv_files` list in your script to point to the actual locations of your CSV files.

4. **Save the Chainlit application code:**
    Make sure to save your Chainlit application code in a file named `chain_app.py`.

## Usage

1. **Run the Flask API server in the background of your Notebook in colab:**
    ```bash
  !ssh -R 80:localhost:5003 serveo.net  
    ```

2. **Run the Chainlit application:**
    ```bash
    chainlit run chainlit_app.py -h localhost -p 8000
    ```

3. **Access the Chainlit application:**
    Open your browser and go to the address provided by the Chainlit application (usually `http://localhost:8000`).

4. **Interact with the API:**
    Use the Chainlit interface to send queries and get responses based on your processed data.

## Dependencies

- `flask`
- `pandas`
- `langchain`
- `transformers`
- `chainlit`
- `requests`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Kelvin Carrington Tichana

