# Domovoy Automata

## Project Overview
**Project Name**: Domovoy Automata  
**Description**: A system monitoring and automation utility for Linux, using a plugin structure to manage different aspects of the system. The main program will handle message passing between plugins and the user interface.

## Requirements

### Plugin Structure
- Each aspect of the system (CPU monitoring, memory monitoring, disk monitoring, backups, etc.) should be implemented as a separate plugin.
- Plugins should be discoverable and loadable at runtime.
- The main program should be able to communicate with each plugin and facilitate communication between plugins.

### Message Passing
- Implement a robust message passing system between the main program and plugins.
- Allow two-way communication between the main program and plugins.
- Consider using `multiprocessing.Queue`, `multiprocessing.Pipe`, or sockets for IPC.
- Explore the use of pub/sub systems like ZeroMQ or Redis for more complex messaging requirements.
- Ensure the message passing system is scalable and efficient.

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
- Basic system monitoring for CPU, memory, and disk usage.
- Initial configuration dialog for setting thresholds and mount points.

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
