# Monitory process using SNMP

Project developed using python 3 and the library EasySNMP.
This first version, basically list all the processes current in the host, and you can monitoring the process in real time, checking the usage of memory and CPU.

## Getting Started

Easy to run, you need only install some libraries and execute the script.

### Prerequisites

SNMP agent running in the host that will be monitored.

### Installing

We need install the librarie Easy SNMP and tabulate.
You can use the file requirements.txt to install all the correctly versions in your virtual environments.

Install EasySNMP

```
pip3 install easysnmp
```

Install tabulate

```
pip3 install tabulate
```

Install the requirements using the file.

```
pip3 install -r requirements.txt
```

## Running the script

To run the script use the commnad bellow

```
python3 monitora_snmp.py
```

## Built With

* [Easy SNMP](https://easysnmp.readthedocs.io/en/latest/index.html) - The library to use SNMP command
* [Tabulate](https://pypi.org/project/tabulate/) - Project Tabulate, print tabular data in Python

## Author

* **Matheus Gonçalves** - [Linkedin](https://www.linkedin.com/in/matheus-sgoncalves/)