# Data-Controlled-PKE-using-Neural-ODEs
Using the Neural ODEs library to solve Point Kinetic Equations that stimulate Uranium-235 nuclear reactor

This project implements a Neural Ordinary Differential Equation (NODE) model to model time-series data that depicts the behaviour of a U-235 nuclear reactor. It leverages the `torchdyn` and `torchdiffeq` libraries in PyTorch for defining and solving the ODEs.

## Setup

To run the code, you need to have Python 3.6+ installed. You can install the required libraries using pip:

```bash
!pip install torchdiffeq
!pip install torchdyn
```

These commands are executed in the first cell of the notebook.

## Usage

This code is designed to be run in a Google Colab environment (or any Jupyter-compatible environment with GPU access for faster training).

1.  **Open the notebook:** Load the provided `.ipynb` file into Google Colab.
2.  **Run the cells sequentially:** Execute each code cell in order. The notebook is structured to perform setup, data loading, visualization, model definition, and training step-by-step.
3.  **Ensure GPU is enabled:** For optimal performance, make sure GPU acceleration is enabled in your Colab notebook settings (Runtime -> Change runtime type -> Hardware accelerator -> GPU).

## Notebook Structure

The notebook is organized into the following sections:

-   **Setup and Imports:** Installs necessary libraries and imports all required modules from PyTorch, `torchdiffeq`, `torchdyn`, numpy, pandas, and matplotlib. Sets up the device for computation (GPU if available).
-   **Data Loading and Preprocessing:** Loads time-series data from a `.txt` file, handles potential invalid values, and converts the data into PyTorch tensors (`u` for input, `y` for output). Defines the time tensor `t`.
-   **Visualization of Data:** Contains functions (`visualize`, `visualizePred`) to plot the input and true output time series, and optionally the model's predictions, against time.
-   **Data Preparation for Training:** Creates a `TensorDataset` and `DataLoader` to prepare the data for batching during the training process.
-   **PyTorch Lightning Learner:** Defines a custom `pl.LightningModule` class (`Learner`) that encapsulates the forward pass, training step (calculating MAE loss), and optimizer configuration for the Neural ODE model.
-   **Model Definition and Training:** Defines the neural network that acts as the vector field for the ODE, constructs the `NeuralODE` model, and uses a PyTorch Lightning `Trainer` to train the model on the prepared data.

## Data

The data is loaded from a `.txt` file. It consists of two main parts:
-   `rho` (input, represented as `u` in the code): A time series representing the input signal.
-   `NandC` (output, represented as `y` in the code): A time series with multiple dimensions representing the system's response.

The data is expected to be comma-separated values, with the first line being the input and the subsequent lines being the output dimensions.

## Model

The core of the project is a Neural ODE model. The model's dynamics are governed by a neural network that predicts the time derivative of the system's state based on the current state and the input signal. The `torchdyn` library is used to define this structure, and `torchdiffeq` provides the ODE solver (`tsit5` in this case) to integrate the dynamics over time.

## Training

The model is trained using the PyTorch Lightning framework. The `Learner` module defines the training loop, which calculates the Mean Absolute Error (MAE) between the predicted output and the true output at the last time point of the simulation. The Adam optimizer is used for updating the model's parameters.

## Visualization

The notebook includes functions to visualize the loaded data and to compare the true output with the model's predictions after training. This helps in understanding the data and evaluating the model's performance visually.
