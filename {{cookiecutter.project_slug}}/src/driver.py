from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface

class {{cookiecutter.driver_name}}(ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
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

    def cleanup_reservation(self, context):
        """
        Clear reservation when it ends
        :param context:
        :return:
        """
        pass
    
    def send_arp(self, context,):
        """
        Send arp
        :param context:
        :return:
        """
        pass
    
    def start_protocols(self, context,):
        """
        Start protocols
        :param context:
        :return:
        """
        pass
    
    def stop_protocols(self, context,):
        """
        Stop protocols
        :param context:
        :return:
        """
        pass
    
    def run_quick_test(self, context,):
        """
        Run quick test
        :param context:
        :return:
        """
        pass
