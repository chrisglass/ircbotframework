# -*- coding: utf-8 -*-
from importlib import import_module
import re

def load_object(import_path):
    """
    Import paths should be: "mypackage.mymodule.MyObject". It then imports the
    module up until the last dot and tries to get the attribute after that dot
    from the imported module.
    
    If the import path does not contain any dots, a TypeError is raised.
    
    If the module cannot be imported, an ImportError is raised.
    
    If the attribute does not exist in the module, a AttributeError is raised.
    """
    if '.' not in import_path:
        raise TypeError(
            "'import_path' argument to 'django_load.core.load_object' must "
            "contain at least one dot."
        )
    module_name, object_name = import_path.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)

get_plugin_conf_key = lambda class_name: re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', class_name).upper().strip('_')
