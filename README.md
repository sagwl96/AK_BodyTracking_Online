# AK_BodyTracking
Create JSON file of tracked joints from the Microsoft Azure Kinect Camera

Before starting:
- Make sure Azure Kinect Body Tracking SDK is installed
- Make sure the following NuGet packages are installed in Visual Studio:
    - Microsoft.Azure.Kinect.Sensor
    - Microsoft.Azure.Kinect.BodyTracking
    - Microsoft.Azure.Kinect.BodyTracking.Dependencies
    - Microsoft.Azure.Kinect.BodyTracking.Dependencies.cuDNN
    
What code does:
- Detects bodies and prints the joints (32 of them) on screen.
    
Things left to do:
- Dump detected joints into JSON file
