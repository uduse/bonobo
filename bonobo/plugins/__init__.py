class Plugin:
    """
    A plugin is an extension to the core behavior of bonobo. If you're writing transformations, you should not need
    to use this interface.
    
    For examples, you can read bonobo.ext.console.ConsoleOutputPlugin, or bonobo.ext.jupyter.JupyterOutputPlugin that
    respectively permits an interactive output on an ANSI console and a rich output in a jupyter notebook.
    
    Warning: THE PLUGIN API IS PRE-ALPHA AND WILL EVOLVE BEFORE 1.0, DO NOT RELY ON IT BEING STABLE!

    """

    def register(self, dispatcher):
        """
        :param dispatcher: whistle.EventDispatcher
        """
        pass

    def unregister(self, dispatcher):
        """
        :param dispatcher: whistle.EventDispatcher
        """
        pass