# Image Classification Project

## Overview
This project focuses on building and deploying an image classification model using machine learning operations (MLOps) practices. The goal is to automate the process of training, validating, and deploying a model that can classify images into predefined categories.

## Project Structure

```
.
├── data
│   ├── raw
│   ├── processed
├── notebooks
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
├── src
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
├── models
│   ├── saved_model
├── README.md
├── requirements.txt
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vishnu-E/image_classification
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application server:

   ```bash
   uvicorn app.Main:app --reload
   ```

2. Open the link in your browser (e.g., `http://127.0.0.1:8000`).

3. Add `/docs` to the URL (e.g., `http://127.0.0.1:8000/docs`) to access the interactive API documentation.

4. Click **Try it out**, upload a photo, and execute the request to see the classification results.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [scikit-learn](https://scikit-learn.org/)

