"""
A function writes events for splunk using splunk python sdk event writer
"""

from splunklib.modularinput import *
from bandwidthusage.generatedata import get_bandwidth
def write_splunk_event(input_name, ew, server_address):
    """
    Args:
    Returns:
    """
    #It's best practice for your modular input script to log diagnostic data to splunkd.log. Use an EventWriter's log method to write log messages, which include both a standard splunkd.log level (such as "DEBUG" or "ERROR") and a descriptive message.
    EventWriter.log(ew, EventWriter.INFO, "Started generating Random data for %s" % server_address)   
    event = Event()
    event.stanza = input_name
    event.data = get_bandwidth() //get_bandwidth generates random bandwidth data for ex "user=localhost download=150 upload=100"
    ew.write_event(event)
