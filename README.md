# cs350-milestones
**CS350 Emerging Systems, Architectures, and Technologies** (embedded systems w/ raspberry pi4 and grovepi+)

In this class, we explored emerging systems, architectures, and technologies with a focus on hardware/software interface. Utilizing the Raspberry Pi embedded system and the GrovePi+ sensor kit, we wrote specific software to interface with the embedded system and control hardware and software components. The following milestone projects are the building blocks for the eventual final project.

<br />

**Milestone 1 - Sound Sensor**

This introductory milestone introduced a basic sound sensor from the GrovePi+ kit. An LED light was attached to the embedded system along with the sound senor, and software was modified accordingly so that when sound exceeded a specified threshold it triggered the LED light to turn on. The specific milestone 1 modifications are commented in the source code.

Milestone 1 source code: https://github.com/bkoconnell/cs350-milestones/tree/main/milestone1_sound_sensor

Milestone 1 demo: https://youtu.be/Qr349Zf1F6U
(ensure video is set to highest quality)

<br />

**Milestone 2 - Digital Humidity & Temperature Sensor**

This milestone is the first building block for the final project. The Grove DHT (digital humidity and temperature) sensor is used to capture data readings for temperature and humidity of the environment. The software implements a while loop to read in the data from the sensor and converts the temperature reading to Fahrenheit. It then creates a JSON object for the data with specific formatting, then stores the object in a JSON database file (output as data.json). Additionally, the JSON data is output to the console for demonstration purposes. 

The software also converts the data readings to string format then outputs the strings to an LCD screen. A sleep timer is set at the end of the loop, which determines how often the loop iterates. This controls the output frequency for both the JSON file and the LCD screen refresh. It's worth noting that each successive loop iteration appends the new data to the existing JSON file so that previous data is not overwritten. The JSON database file (data.json) for this milestone is located in the directory with the source code (link below). In the demo below, the Python script is run in the terminal and I place my fingers on the DHT sensor to manipulate the humidity and demonstrate functionality of the program.

Milestone 2 source code: https://github.com/bkoconnell/cs350-milestones/tree/main/milestone2_dht_sensor

Milestone 2 demo: https://youtu.be/Epvm2UJLJi0
(ensure video is set to highest quality)

<br />

**Milestone 3 - Light Sensor**

Another component of the final project is the light sensor, which is introduced in this milestone. The goal of this milestone is to simulate an interupt condition for the embedded system. The software is designed so that when the light reading crosses a specific threshold (when the environment's lighting is dark enough) the attached LED will turn on. The logic is written inside of a while loop and a sleep timer is set at the end of the loop, which determines how often the loop iterates. Each iteration executes the logic to read in the sensor data and check it against the threshold.

In the demo below, a blue LED and a light sensor are connected to the embedded system. When the program is initiated, the blue LED turns on because the light in the room is dark enough to trigger it. However, when I shine a flashlight onto the light sensor, the blue LED shuts off. This demonstrates the interupt condition set by the lighting threshold in the software. For each loop iteration, the sensor reading and calculated resistance are output to the console.

Milestone 3 source code: https://github.com/bkoconnell/cs350-milestones/tree/main/milestone3_light_sensor

Milestone 3 demo: https://youtu.be/Vu1d4RBZwRk
(ensure video is set to highest quality)

<br />

**Final Project**

Final Project repository: https://github.com/bkoconnell/cs350-final-project
