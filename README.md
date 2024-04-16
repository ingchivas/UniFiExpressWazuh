# UniFi Express MAC Lookup Integration for Wazuh

This repository contains the necessary files for integrating a MAC address lookup API with Wazuh, a popular open-source security information and event management (SIEM) platform.

The purpose of this integration is to enrich the logging data from a UniFi Express router by providing additional information about the MAC addresses detected in various network events, such as DHCP actions and router solicitations.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Overview
This Integration for Wazuh consists of the following components:

1. **custom-maclookup.py**: A Python script that retrieves MAC address details from the [Maclookup API](https://www.maclookup.app/) and logs the information to a custom log file.
2. **Wazuh Decoders and Rules**: Custom decoders and rules that parse the log file and generate alerts for unknown or known MAC addresses.

By using this integration, you can gain valuable insights into the devices connected to your network, including the manufacturer and location of the devices, which can be useful for network monitoring and security purposes.

## Features
- Automatically retrieves MAC address details from the Maclookup API
- Logs the MAC address, vendor, and location information to a custom log file
- Generates Wazuh alerts for unknown and known MAC addresses
- Supports DHCP actions and router solicitations from a UniFi Express router

## Installation
1. Clone the repository to your Wazuh server:
```bash
git clone https://github.com/ingchivas/UniFiExpressWazuh.git
```
2. Copy the `custom-maclookup.py` script to the Wazuh integrations directory:
```bash
cp UniFiExpressWazuh/MAC_LOOKUP/custom-maclookup.py /var/ossec/integrations/
```
3. Copy the Wazuh decoders and rules to the Wazuh configuration directory

4. Restart the Wazuh manager:
```bash
systemctl restart wazuh-manager
```
## Configuration
1. Obtain an API key from the [Maclookup API](https://www.maclookup.app/) website.
2. Update the `api_key` value in the `<integration>` section of the `ossec.conf` file.
3. Customize the log file location in the `<localfile>` section of the `ossec.conf` file, if desired.

## Usage
Once the integration is set up, the `custom-maclookup.py` script will be automatically executed whenever a DHCP or router solicitation event is detected on the UniFi Express router. The script will look up the MAC address details and log the information to the specified log file.

Wazuh will then parse the log file and generate alerts for unknown and known MAC addresses, which can be viewed in the Wazuh web interface or through the command-line interface.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open a new issue or submit a pull request.

## License
This project is licensed under the [GPL-3.0](LICENSE).

