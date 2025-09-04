#!/bin/bash

# A simple script to install dependencies and run the Streamlit dashboard.

# Function to check for Python installation
check_python() {
    if ! command -v python3 &> /dev/null
    then
        echo "Python 3 is not installed. Please install Python 3 and try again."
        exit 1
    fi
}

# Function to install dependencies
install_dependencies() {
    echo "Installing required Python libraries..."
    pip install streamlit pandas plotly
    if [ $? -ne 0 ]
    then
        echo "Error: Failed to install dependencies. Please check your internet connection."
        exit 1
    fi
    echo "Dependencies installed successfully."
}

# Function to run the Streamlit app
run_app() {
    echo "Starting the Streamlit dashboard..."
    streamlit run app.py
    if [ $? -ne 0 ]
    then
        echo "Error: Failed to start the Streamlit application. Please check your app.py file."
        exit 1
    fi
}

# Main script execution
check_python
install_dependencies
run_app
