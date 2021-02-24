from utils import plugins

PLUGIN_NAME = 'Scripts Plugin'
DISPLAY_NAME = 'Scripts'
DESCRIPTION = 'A scripts utility plugin.'
AUTHOR = 'Birkbeck Centre for Technology and Publishing'
VERSION = '0.1'
SHORT_NAME = 'scripts'
JANEWAY_VERSION = "1.3.9"


class Scripts(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME

    version = VERSION
    janeway_version = JANEWAY_VERSION

    is_workflow_plugin = False


def install():
    Scripts.install()


def hook_registry():
    pass


def register_for_events():
    pass