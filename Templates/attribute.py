class AttributeTemplate:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.input_types = []

    def set_description(self, description):
        self.description = description

    def set_input_types(self, input_types):
        self.input_types = input_types

    def __str__(self):
        return f"""
        Attribute Name: {self.name}
        Description: {self.description}
        Input types: {self.input_types}
        """
