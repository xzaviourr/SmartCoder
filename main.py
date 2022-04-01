from Templates.function import FunctionTemplate
from Templates.attribute import AttributeTemplate


new_attr = AttributeTemplate('number')
new_attr.set_description("Input number")
new_attr.set_input_types([int, float])

new_function = FunctionTemplate('check_even')
new_function.set_description('check if number is even')
new_function.set_dependency(None)
new_function.set_dependency_path('UserFunctions')
new_function.set_primary_attribute(new_attr)

Database = list()