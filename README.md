# EEE4113F Design Project
<div align="center">
  <img src="img/UCT_Emblem.png" width="350" height="350">
</div>

# Data Processing and Bird Identification Subsystem

This repository contains the code for the Data Processing and Bird Identification subsystem of this Wireless Autonomous Digital Scale project. This subsystem is designed to process weight data from the scale and identify individual birds based on images captured when they land on the perch. Additionally, this subsystem includes a Python script which monitors the size of the collected data directory.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data Processing](#data-processing)
- [Bird Identification](#bird-identification)
- [File Monitoring and Intervention System](#file-monitoring)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Data Processing and Bird Identification subsystem is an integral part of the Wireless Autonomous Digital Scale project which has been designed specifically for the Fork-tailed Drongo. It includes algorithms and techniques for accurate weight processing, filtering out bird movement effects, and identifying individual birds based on captured images. This README provides an overview of the repository, installation instructions, usage guidelines, and details about the data processing and bird identification components.

## Installation
To install and set up the Data Processing and Bird Identification subsystem, follow these steps:
1. Clone this repository to your local machine.
2. Ensure that the required dependencies and libraries are installed (detailed instructions can be found in the respective sections).
3. Configure any necessary settings or parameters as described in the documentation.

## Usage
Before using the subsystem, make sure to complete the installation process. Once installed, the system can be used as follows:
1. Connect the necessary hardware components (scale, microcontroller, camera) according to the provided instructions.
2. Run the main program, specifying the appropriate parameters and settings.
3. The system will process weight measurements, filter out bird movement effects, and store the data in the desired format.
4. Captured images will be analyzed for bird identification, allowing for species tracking and behavior analysis.

## Data Processing
The Data Processing component of this subsystem employs a technique whereby weight readings which are deemed to be out of range are discarded. Weight readings in range are recorded while the bird is on the scale and once it leaves, the average weight measurement is calculated and recorded. This approach aimed to mitigate the effect of bird movements on the weight readings.

## Bird Identification
The Bird Identification component utilizes a Raspberry Pi Camera (Specifically the Raspberry Pi NoIR Camera Module V2) to capture images of the bird as it is being weighed on the perch. The camera is triggered as the bird lands on the perch and continiously photographs the bird while it is being weighed. <br>
The prupose of this components was for the researcher to be able to uniquely identify which bird landed on the scale and was being weighed.

## File Monitoring
The File Monitoring component utilizes a Python script which monitors the size of the data directory of this project. If the size of the folder exceeds a maximum threshold, the oldest time-stamped files will be continously deleted until the threshold is no longer exceeded.

## Contributing
I welcome contributions to this repository! If you would like to contribute, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file. Contributions can include bug fixes, feature enhancements, documentation improvements, or additional functionalities.

## License
This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of the license.
