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

TODO

## Get Started on Your Local Machine

### (Option 1) Installing Anaconda/Miniconda
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

### TODO: Install PyTorch


### TODO: Install dependencies
```bash
pip install -r requirements.txt
```