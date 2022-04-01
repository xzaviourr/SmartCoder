class FunctionTemplate:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.primary_attribute = None
        self.secondary_attribute = None
        self.other_attributes = []
        self.dependency = None
        self.dependency_path = None

    def set_description(self, description):
        self.description = description

    def set_primary_attribute(self, attribute):
        self.primary_attribute = attribute

    def set_secondary_attribute(self, attribute):
        self.secondary_attribute = attribute

    def set_other_attributes(self, attributes):
        self.other_ttributes = attributes

    def set_dependency(self, dependency):
        self.dependency = dependency

    def set_dependency_path(self, path):
        self.dependency_path = path

    def __str__(self):
        return f"""
        Function name: {self.name}
        Description: {self.description}
        Primary attribute: {self.primary_attribute}
        Secondary attribute: {self.secondary_attribute}
        Other attributes: {self.other_attributes}
        Dependency: {self.dependency}
        Dependency path: {self.dependency_path}
        """