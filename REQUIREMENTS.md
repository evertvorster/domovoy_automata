# Domovoy Automata Requirements

## Overview
Domovoy Automata is a modular system resource management utility for Linux, supporting a plugin-based architecture. The main program coordinates plugins, each of which is responsible for specific aspects of system monitoring and management.

## Main Program Requirements
- List currently installed plugins.
- Show plugin status (running, stopped, OK, ERROR).
- Control buttons to start, stop, or restart each plugin.
- Configuration file (`main_config.json`) lists active plugins.

## Plugin Requirements
- Each plugin has its own configuration utility.
- Separate configuration files for each plugin.
- Plugins should be Python scripts or compiled binaries.
- Plugins can communicate with the main program for status updates and command execution.

## Configuration Utility
- `configure.py` allows setting thresholds, specifying mount points, and configuring disk thresholds.
- Monitor for new mount points and initiate backups when new ones become available.
- Popup dialogs for initiating backups with `rsync -av`, displaying terminal output, and providing a dismiss button.

## Communication
- Robust message passing mechanism between the main program and plugins.
- Dedicated test plugin to verify communication setup.

## Plugin Management
- Plugins directory contains subdirectories for each plugin.
- Plugins can be started, stopped, or restarted via the main program UI.

### System Monitoring Plugins
- **CPU Monitoring Plugin**:
  - Monitor CPU usage and set thresholds.
  - Notify the main program when thresholds are exceeded.
  
- **Memory Monitoring Plugin**:
  - Monitor memory usage and set thresholds.
  - Notify the main program when thresholds are exceeded.
  
- **Disk Monitoring Plugin**:
  - Monitor disk space for specified mount points.
  - Set thresholds for disk usage.
  - Notify the main program when thresholds are exceeded.

### Backup Plugin
- Monitor specific mount points for availability.
- Prompt the user to initiate backup when specific disks are mounted.
- Use `rsync` for backups.
- Display terminal output of the backup process.
- Provide a dismiss button for the terminal output.

### Configuration
- The main program should have a configuration dialog.
- Allow setting of thresholds for CPU, memory, and disk usage.
- Specify mount points to be monitored.
- Configure backup mount points and associated thresholds.
- Validate and update the configuration file.

## Current State

### Implemented Features
Test plugin

## Additional Requirements
- Valid PySide6 (Qt6) support.
- Each plugin has a status of either running, stopped, OK, or ERROR.

### Issues
- Integrating backup functionality with user prompts.
- Handling dynamic changes in configuration.
- Ensuring mount points exist before starting monitoring.

## Next Steps
- Finalize configuration management.
- Implement the plugin architecture.
- Develop the CPU, memory, and disk monitoring plugins.
- Implement the backup plugin.
- Refine the UI for better user experience.
- Develop and integrate the message passing system.
