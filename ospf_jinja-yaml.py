from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result
import time

from saved_configuration import saved_config

saved_config()

nr = InitNornir(config_file="config.yaml")

def execute_configure_ospf():
    print("#####...SENDING...OSPF...CONFIGURATION...COMMANDS...#####")
    time.sleep(10)
    results = nr.run(task=netmiko_send_config, config_file='ospf_configs')
    print_result(results)
    time.sleep(5)
    
execute_configure_ospf()
