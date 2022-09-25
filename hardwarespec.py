#import tkinter as tk
import psutil as ps
import platform as plat
from termcolor import colored as col
#help("modules")

"""
Geting System Inforamtion
"""

print(f"Computer network name: {plat.node()} \n")
print(f"Machine Type: {plat.machine()} \n")
print(f"Processor type: {plat.processor()} \n")
print(f"Platform type: {plat.platform()} \n")
print(f"Operating system: {plat.system()} \n")
print(f"Operating system release: {plat.release()} \n")
print(f"Operating system release: {plat.release()} \n")
print(f"Operating system version: {plat.version()} \n")

"""
CPU Usage, CPU Frequency, CPU Utilization Percentage
"""
#Number of Cores

print(f"# of PHYSICAL CORES: {ps.cpu_count(logical=False)} \n")
print(f"# of LOGICAL CORES: {ps.cpu_count(logical=True)} \n")

#CPU {Current, Min, Max} Frequency

print(f"Current CPU frequency: {ps.cpu_freq().current}")
print(f"Min CPU frequency: {ps.cpu_freq().min}")
print(f"Max CPU frequency: {ps.cpu_freq().max}")


#CPU Utilization

print(f"Current CPU Utilization: {ps.cpu_percent(interval=1)}% \n")
print(f"Current per-CPU Utilization: {ps.cpu_percent(interval=1, percpu=True)} \n")
#interval=1 should ideally be set to any value > 0.
"""
RAM Usage
"""
#print(f"Tot. RAM installed: {round(ps.virtual.memory().total/1000")
