from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, CancellationContext
#from data_model import *  # run 'shellfoundry generate' to generate data model classes


class {{cookiecutter.driver_name}}ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass


    def load_configuration(self, context, config_file_location):
        """
        Load configuration file
        :param context:
        :param config_file_location:
        :return:
        """
        pass

    def start_traffic(self, context, blocking):
        """
        Start traffic
        :param context: the context the command runs on
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        :param blocking:
        """
        pass

    def stop_traffic(self, context):
        """
        Stop traffic
        :param context: the context the command runs on
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        pass

    def get_statistics(self, context, view_name, output_type):
        """
        Get statistics
        :param context:
        :param view_name:
        :param output_type:
        :return:
        """
        pass