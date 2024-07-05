# Domovoy Automata Requirements

## Overview

Domovoy Automata is a modular utility designed for system resource management on Linux. It leverages a plugin architecture to extend functionality, enabling the automation of various system administration tasks.

## General Requirements

1. **Plugin Structure**: 
    - The main program (`domovoy_automata.py`) should support plugins to manage different aspects of the system.
    - Each plugin should be modular and self-contained, with its own configuration file.
    - The main configuration file should only manage which plugins are active.

2. **Plugin Communication**: 
    - Plugins should communicate with the main program using message passing.
    - The message passing should be robust, allowing for two-way communication between the main program and plugins.

## Main Program (`domovoy_automata.py`)

1. **UI Elements**:
    - Display a list of currently installed plugins.
    - Show the status of each plugin: running, stopped, OK, or ERROR.
    - Provide buttons to start, stop, or restart each plugin.
    - Include a "Configure" button to open the configuration utility.

2. **Configuration**:
    - Check if the `main_config.json` file exists and is compatible with the current configuration requirements.
    - If not, recreate the file using existing settings and default values for new options.
    - On startup, verify that specified mount points exist and allow the user to adjust the configuration if they don't.

## Plugin Requirements

1. **General**:
    - Each plugin must have its own configuration utility and a separate configuration file.
    - Plugins should be able to be started, stopped, and restarted by the main program.

2. **Example Plugin**:
    - A test plugin should be created to set up and test the communication between the main program and its plugins.
    - This plugin should follow the standard structure and demonstrate the basic functionality expected of all plugins.

## Configuration Utility (`configure.py`)

1. **UI Elements**:
    - Allow the user to set thresholds for various system resources.
    - Enable the configuration of mount points, including the mount point path, user-definable name, and threshold.
    - Display a list of available plugins and allow the user to configure each plugin individually.

2. **Functionality**:
    - Verify that the mount points exist before saving them to the configuration.
    - Provide a user-friendly interface for adjusting settings and thresholds.
    - Save the configuration in a format compatible with the main program.

## Additional Considerations

- **Extensibility**: 
    - Ensure the system is easy to extend with new plugins.
    - Maintain a clean and modular codebase to facilitate future development.

- **Error Handling**: 
    - Implement robust error handling in both the main program and plugins.
    - Provide meaningful error messages to help users troubleshoot issues.

## Future Enhancements

1. **Backup Functionality**:
    - Monitor specified mount points for the availability of external drives.
    - Prompt the user to initiate a backup using `rsync` when a drive becomes available.
    - Display terminal output during the backup process and provide a dismiss button once the backup is complete.

2. **System Administration Tasks**:
    - Extend the functionality to include tasks such as CPU frequency setting and other administrative actions.

## Conclusion

Domovoy Automata aims to simplify system resource management on Linux through a flexible and extensible plugin architecture. By adhering to these requirements, the project will provide a robust foundation for automating a variety of system tasks.

---

### Note

Ensure all code adheres to Python's best practices and is compatible with Qt6 for UI elements.
