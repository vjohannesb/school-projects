# C# (30yhp)

-   Object-Oriented Programming (OOP)
-   .NET class libraries and frameworks
-   Error handling and debugging
-   Unit testing within TDD
-   Testing with nUnit
-   Using SCRUM/KANBAN
-   Azure Functions
-   Azure IoT
-   Version control with Git

## Assigments

-   Assignment 1 - Worker Service
    -   Log random "weather data" every minute
    -   Include init and exit messages
    -   Alert if temp. above or below certain temperatures
    -   **VG**: Use an API for actual weather data
-   Assignment 2 - WPF Application
    -   Windows Mail Lookalike
    -   Tabs/Views: Messages, Contacts, Calendar, Tasks, Settings
    -   **VG**:
        -   Switch views and detailed views
        -   Use Custom Controls
-   Assignment 3 - Azure (Functions + IoT)
    -   Azure IoT Hub
    -   .NET Core Console App (as IoT Device)
    -   Send weather data (from API or random) to IoT Hub
    -   **VG**:
        -   Azure Function App w/ HttpTrigger
        -   Receive DeviceId and Message
        -   Send message to Console App and print it
-   Assignment 4 - Azure + UWP
    -   Basically assignment 3 but with an UWP App instead of Console App
-   Assignment 5 - Unit Testing (with Azure IoT)
    -   Azure IoT Hub + .NET Core Console App
    -   Send weather data to IoT Hub
    -   Receive Direct Method message (using Device Explorer) to change interval of messages
    -   Unit Test (xUnit, nUnit or MSTest) according to TDD
    -   **VG**:
        -   Another Console App to replace Device Explorer (send Direct Method messages to IoT Device)
        -   Unit Test this as well
