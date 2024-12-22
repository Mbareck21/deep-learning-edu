# Deep Learning Educational App

Interactive desktop application for learning Deep Learning with PyTorch.

## Requirements

### System Requirements
- Windows 10/11 or Linux
- Python 3.8+
- Git
- Visual Studio Build Tools (Windows only)
- CUDA Toolkit 11.8+ (optional, for GPU support)

### Development Tools
- Visual Studio Code (recommended)
- Python extension for VS Code
- Git extension for VS Code

## Installation

1. Install Visual Studio Build Tools (Windows):
   - Download from [Visual Studio Downloads](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - Select "Desktop development with C++"
   - Install Windows 10/11 SDK

2. Install CUDA (Optional for GPU):
   - Download CUDA Toolkit from [NVIDIA](https://developer.nvidia.com/cuda-downloads)
   - Install cuDNN library

3. Clone and Setup:
```bash
# Clone repository
git clone https://github.com/Mbareck21/deep-learning-edu.git
cd deep-learning-edu

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

4. Run Application:
```bash
python main.py
```

## Project Structure
```
deep_learning_edu/
├── src/
│   ├── lessons/          # Lesson content
│   │   ├── base_lesson.py
│   │   └── deep_learning_basics.py
│   ├── ui/              # UI components
│   │   ├── code_editor.py
│   │   └── styles.py
│   └── utils/           # Utilities
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

## Troubleshooting

### Windows
- Error "Microsoft Visual C++ 14.0 is required": Install Visual Studio Build Tools
- PyQt6 installation fails: Ensure Python and pip are up to date
- CUDA errors: Verify NVIDIA drivers and CUDA installation

### Linux
- QT dependencies missing: Install required packages
```bash
sudo apt-get install python3-pyqt6
```

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request