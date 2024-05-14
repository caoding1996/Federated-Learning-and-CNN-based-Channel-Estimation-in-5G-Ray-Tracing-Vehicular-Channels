# Federated-Learning-and-CNN-based-Channel-Estimation-in-5G-Ray-Tracing-Vehicular-Channels
This simple demo has the following functionality
1. Vehicles serves as transmitter and receiver, and their locations is extracted through SUMO and TraCI.
2. Then the locations of transmitter and receiver are imported to MATLAB ray-tracing simulation in real-time.
![image](https://github.com/caoding1996/Federated-Learning-and-CNN-based-Channel-Estimation-in-5G-Ray-Tracing-Vehicular-Channels/blob/main/IMG/Raytracing.png)
4. Construct the 5G ray-tracing channel in MATLAB, which also include the LDPC encoding process.
5. MATLAB continuously outputs channel response images to form the training dataset for the CNN.
![image](https://github.com/caoding1996/Federated-Learning-and-CNN-based-Channel-Estimation-in-5G-Ray-Tracing-Vehicular-Channels/blob/main/IMG/CR.png)
# Requirement

SUMO 1.6.0
python 3.8
MATLAB 2021a

# How to run?
python sumoraytrace.py

This python script will wake up MATLAB and SUMO.
