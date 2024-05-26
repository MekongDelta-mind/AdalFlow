from typing import Any


class Parameter:
    r"""A generic class to represent a parameter.

    Parameters are any data type that has a special property when
    used in a component - when they are assigned as Component attributes
    they are automatically added to the list of its parameters, and  will
    appear in the :meth:`~Component.parameters` iterator.

    Args:
        data (Any): parameter data.
        requires_opt (bool, optional): if the parameter requires optimization. Default: `True`

    """

    def __init__(self, key: str, data: Any, requires_opt: bool = True):
        self.data = data
        self.key = key
        self.requires_opt = requires_opt
        print(f"data: {data}, requires_opt: {requires_opt}")

    def update_value(self, data: Any):
        self.data = data

    def __repr__(self):
        return f"Parameter: {self.data} with key: {self.key}"
