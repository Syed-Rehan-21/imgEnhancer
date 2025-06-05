# Image Enhancer

Image Enhancer is a versatile and user-friendly Streamlit application designed to enhance and transform images effortlessly. With an intuitive interface, users can upload their images and access the editing tools. They can adjust sharpness, colors, brightness, and contrast, apply captivating filters like black and white or blur, and even remove the background and replace it with a custom color. The real-time preview allows users to visualize the impact of their edits, and the edited image can be easily downloaded in PNG format. Experience the power of Image Enhancer and elevate your images to new heights.

## Prerequisites
- Python 3.10
- [UV package manager](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

### Method 1: Quick Setup with UV (Recommended)
UV is a fast Python package manager that makes dependency management easier and more reliable.

1. **Install UV** (if not already installed):
   ```bash
   # macOS using Homebrew (recommended)
   brew install uv
   
   # macOS/Linux using installer
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Using pip
   pip install uv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Syed-Rehan-21/imgEnhancer.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd imgEnhancer
   ```

4. **Setup with UV**:
   
   **If pyproject.toml exists in the project:**
   ```bash
   # Install dependencies and create environment automatically
   uv sync
   ```
   
   **If only requirements.txt exists:**
   ```bash
   # Create virtual environment with Python 3.10
   uv venv --python 3.10
   
   # Activate virtual environment
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   
   # Install dependencies
   uv pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   # If using uv sync
   uv run streamlit run app.py
   
   # Or with activated environment
   streamlit run app.py
   ```

### Method 2: Traditional Setup with pip

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Syed-Rehan-21/imgEnhancer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd imgEnhancer
   ```

3. **Create virtual environment** (recommended):
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application** in your web browser at `http://localhost:8501`

3. **Upload an image** by clicking on the "Upload" button 

4. **Adjust the settings** in the sidebar to customize the image enhancements and edits

5. **Preview your changes** - the original and edited images will be displayed side by side

6. **Download the edited image** by clicking on the "Download" button

## Features
- **Image Enhancement**: Adjust sharpness, brightness, contrast, and colors
- **Filters**: Apply black and white, blur, and other artistic filters
- **Background Removal**: Remove image backgrounds and replace with custom colors
- **Real-time Preview**: See changes instantly as you adjust settings
- **Easy Download**: Save your enhanced images in PNG format