# Physics-Aware Deep Learning
Lecture materials for the "Physics-Aware Deep Learning" course (Prof. Stephen Baek, University of Virginia)

## Course Schedule
| Session                           | Lecture Slides                                                   | Lab     |
|   ----------------------------    | ---------------------------------------------------------------- | ------  |
| Course Orientation                | [slides](lectures/00_Orientation.pdf)                            | -       |
| Introduction to Neural Networks   | [slides](lectures/01_Introduction%20to%20Neural%20Networks.pdf)  | [intro](labs/01_introduction_to_pytorch.ipynb) |
| Convolutional Neural Networks     | [slides](lectures/02_Convolutional%20Neural%20Networks.pdf)      | [crack](labs/02_cnn_crack_detection.ipynb) |
| How to Train Convolutional Neural Networks | [slides](lectures/03_How%20to%20Train%20Convolutional%20Neural%20Networks.pdf) | [autograd](labs/03_1_autograd.ipynb) |
| Physics Informed Neural Networks | [slides](lectures/04_Physics-informed%20neural%20networks.pdf) | [harmonic](labs/03_2_pinn_harmonic_oscillator.ipynb),<br/>[heat](labs/03_3_pinn_1d_heat_diffusion.ipynb) |
| Neural Operators | [slides](lectures/05_Neural%20Operators.pdf) | [lab](labs/04_neural_op_1d_burger.ipynb)|
| Physics-Aware Recurrent Convolutions | [slides](lectures/06_Physics-Aware%20Recurrent%20Convolutions.pdf) | [lab](labs/05_parc_harmonic_oscillator.ipynb) |
| Deep Reduced Order Modeling | [slides](lectures/07_Deep%20Reduced%20Order%20Modeling.pdf) | - |
| Generative Networks and Digital Twins | [slides](lectures/08_Generative%20Networks.pdf) | - |




## Get Started with Google Colab (Recommended)

The easiest way of getting started with the course materials, especially if you don't have much experience with Python and computer programming in general, would be to use what's called [Google Colab](https://colab.research.google.com/). 

Colab is essentially a Jupyter Notebook service hosted on Google's server, which requires no setup to use and provides free access to computing resources, especially CUDA-enabled GPUs. If you are a complete beginner or have no access to high-end NVIDIA GPUs, Colab is probably the best way of learning the course materials.

In case you are new to Python, Jupyter Notebook is an interactive Python environment you can run on a web browser. You can run Python scripts on a notebook, make notes, experiment with different implementations, etc. If you have not used Jupyter Notebook before, [this tutorial](https://github.com/Reproducible-Science-Curriculum/introduction-RR-Jupyter/blob/e5aece1011a43edfd739cbd83a2f4346091a86e2/notebooks/Navigating%20the%20notebook%20-%20instructor%20script.ipynb
) might help you get started.

All lab sessions in this course are directly accessible from Google Colab. For each lab session file (`*.ipynb`), look for the <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open and Execute in Google Colaboratory"> badge at the top and just click it, which will let you open the lab session in Colab directly.





## Get Started on Your Local Machine

### Installing Anaconda/Miniconda
Anaconda and Miniconda are popular package managers for Python, especially for data science and machine learning. Anaconda comes with a large collection of pre-installed packages, while Miniconda provides a minimal setup with only essential tools. You just need to install both, but choose one you need.

#### Installing Miniconda (Recommended)
1. Download Miniconda
    - Visit the [Miniconda download page](https://www.anaconda.com/download/success/#miniconda).
    - Select the installer for your operating system.

1. Run the Installer
    - On Windows, execute the downloaded .exe file and follow the instructions.
    - On macOS and Linux, run the following command in the terminal:
        ```bash
        bash Miniconda3-*.sh
        ```
    - Follow the prompts to complete the installation.

1. Verify Installation
    - Open a terminal or command prompt and type below. If Miniconda is installed correctly, it will display the installed version.
        ```bash
        conda --version
        ```

#### Installing the Full Anaconda
1. Download Anaconda
    - Visit the [official Anaconda website](https://www.anaconda.com/download/success).
    - Choose the appropriate installer for your operating system (Windows, macOS, Linux).
1. Run the Installer
    - On Windows, run the .exe file and follow the installation prompts.
    - On macOS and Linux, run the .sh script in the terminal using:
        ```bash
        bash Anaconda3-*.sh
        ```
    - Follow the on-screen instructions.
1. Verify Installation

    - Open a terminal or command prompt and type below. If Anaconda is installed correctly, it will display the installed version.
        ```bash
        conda --version
        ```

#### Post-Installation Setup (For both Miniconda and Anaconda)
Conda virtual environments allow users to create isolated Python environments with specific dependencies. This helps prevent conflicts between different packages and projects. Each environment can have its own Python version and set of libraries. Using Conda environments ensures a clean and manageable workspace for different projects.

1. Create a virtual environment:
    ```bash
    conda create -n padl python=3.11 ipykernel
    ```

2. Activate the environment:
    ```bash
    conda activate padl
    ```

### Install PyTorch
PyTorch is a popular open-source machine learning framework used for deep learning applications. It provides dynamic computation graphs and GPU acceleration, making it a preferred choice for researchers and practitioners. Physics-aware deep learning community also widely adopts PyTorch for research.

The best and most reliable way to install PyTorch is by following their [official documentation](https://pytorch.org/get-started/locally/), which gets updated quite frequently.

Overall, the procedure should look something like this:

1. Make sure you activated the environment (see "Post-Installation Setup" for Anaconda/Miniconda)
    ```bash
    conda activate padl
    ```
1. Visit the Official Installation Guide
    - Go to the PyTorch website.
    - Select your operating system (OS), package manager (you can choose 'pip'), language ('Python'), and CUDA version (if using a GPU). If you don't have a [CUDA-compatible GPU](https://developer.nvidia.com/cuda-gpus) on your machine, choose 'CPU' instead of 'CUDA'.

1. Install PyTorch
    - Once you have made selections on the official PyTorch website, it will generate a command for you to run. It should look something like this (but may vary according to your selection):
        ```bash
        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
        ```

1. Verify Installation
    - If PyTorch is correctly installed, the following command should display a version number:
        ```bash
        python -c "import torch; print(torch.__version__)"
        ```
    - Also, if you installed the GPU version with the 'CUDA' option, the following command should return "True":
        ```bash
        python -c "import torch; print(torch.cuda.is_available())"
        ```

### Install dependencies
Finally, once you are done with installing PyTorch, run the following command to install the rest of the 3rd party libraries that are required for running the lab tutorials.
```bash
pip install -r requirements.txt
```

### Run Notebooks
Materials for the lab sessions can be found under the `./labs` folder of this repository. To run a notebook, you can type the following command:
```bash
jupyter notebook labs/<name-of-the-notebook>.ipynb
```
This will open up a web browser tab, in which you can interact with the codes. While the user interface of these notebooks are pretty straightforward, it wouldn't hurt to read [this tutorial](https://github.com/Reproducible-Science-Curriculum/introduction-RR-Jupyter/blob/e5aece1011a43edfd739cbd83a2f4346091a86e2/notebooks/Navigating%20the%20notebook%20-%20instructor%20script.ipynb) to get familiarize yourself with it.