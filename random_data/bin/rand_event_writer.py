"""
writes random bandwidth data into spluk
"""
"""
A class inhereting splunk pyhton sdk Script class 
"""
import sys

from splunklib.modularinput import *
from write_event import write_splunk_event



class SplunkScript(Script):
    """
    todo:
    """

    def get_scheme(self):
        """
        Args:
        Returns:
        """
        scheme = Scheme("Random Bandwidth Input")
        scheme.description = "Sends random bandwidth data to splunk"
        scheme.use_external_validation = False
        scheme.use_single_instance = True

        datakind_argument = Argument("datakind")
        datakind_argument.data_type = Argument.data_type_string
        datakind_argument.description = "The Data Kind of Random Generated Data"
        datakind_argument.required_on_create = True
        scheme.add_argument(datakind_argument)

        return scheme

    def validate_input(self, validation_definition):
        """
        Args:
        Returns:
        """
        datakind = str(validation_definition.parameters["datakind"])
        if len(datakind) < 1:
            raise ValueError("The datakind has to be at least 1 character long!")

        
    def stream_events(self, inputs, ew):
        """
        Args:
        Returns:
        """
        for input_name, input_item in inputs.inputs.iteritems():
            datakind = str(input_item["datakind"])
            write_splunk_event(input_name, ew, datakind)


if __name__ == "__main__":
    SplunkScript().run(sys.argv)