class Capabilities(object):
    # link between fields of Capability and capability names
    browser_name = "browserName"
    version = "version"
    page_load_strategy = "pageLoadStrategy"
    command_executor = "command_executor"

    def __init__(self, browser_name, version, page_load_strategy, command_executor=None):
        self._capability = {
            Capabilities.browser_name: browser_name,
            Capabilities.version: version,
            Capabilities.page_load_strategy: page_load_strategy,
            Capabilities.command_executor: command_executor,
        }

    def set_capability(self, key, value) -> None:
        self._capability[key] = value

    def get_capability(self, key):
        return self._capability[key]

    def to_dictionary(self) -> dict:
        return self._capability
