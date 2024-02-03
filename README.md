# cerx-ML - Cost-Effective Rocketry Experiments with Machine Learning

## Overview

Welcome to cerx-ML, a project aimed at minimizing costs for rocketry experiments, particularly focusing on **sounding rockets**, through the application of machine learning techniques. The project leverages the power of Intel extensions, along with oneAPI optimized machine learning libraries for enhanced performance across a diverse range of hardware accelerators.

## Project Goals

- **Cost Reduction -** The primary goal of cerx-ML is to explore and implement machine learning algorithms that contribute to cost-effective rocketry experiments, especially those involving sounding rockets.

- **Optimization with oneAPI -** The project is powered by [oneAPI](https://www.oneapi.io/), a cross-architecture programming model designed to deliver high performance computing across various hardware platforms. The use of oneAPI ensures efficient utilization of computational resources.

- **Intel Extensions -** Intel extensions are incorporated to further enhance the performance of machine learning libraries. This optimization is crucial for achieving reliable and rapid results in the field of rocketry.

## Usage

To use cerx-ML, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mdjannatulnayem/cerx-ml.git
   ```

2. Locate the `det_classification.py` file and run it using the following command:

   ```bash
   python det_classification.py
   ```

   You will be prompted to provide the following attributes defined by the `crex_utility` class in the `utility.py` file:

   - `ed` -> engine diameter (float)
   - `nd` -> nozzle diameter (float)
   - `l` -> engine length (float)
   - `mat_S` -> material strength (float)
   - `fuel` -> fuel type (int)
   - `ewt` -> empty weight (float)
   - `lwt` -> loaded weight (float)

   The variable `det` (detonate or not) will be predicted by classification algorithms, and `max_t` (max thrust produced by the engine) will be predicted by a regression algorithm.

3. Locate the `force_regression.py` file and run it using the following command:

   ```bash
   python force_regression.py
   ```

   Again, you will be prompted to provide the necessary attributes to determine the maximum amount of thrust to be produced by the engine.

Note: All attributes should be non-negative.

Feel free to explore and contribute to the cerx-ML project!
