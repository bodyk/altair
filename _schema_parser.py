"""
This file contains utilities to parse the vegalite schema and write low-level
Python wrappers into the altair source directory.
"""
import json
import os


class SchemaFile(object):
    file_comment = ("# This file auto-generated by `_schema_parser.py`.\n"
                    "# Do not modify this file directly.")

    @staticmethod
    def format_help_string(help_str, summarize=True):
        if summarize:
            help_str = help_str.split('(e.g.')[0].split('.')[0]
        return '"""{0}."""'.format(help_str.rstrip())

    @staticmethod
    def kwds_to_str(kwds):
        vals = ', '.join("{0}={1}".format(key, val)
                         for key, val in kwds.items()
                         if key != 'help')
        if 'help' in kwds:
            vals += ', help={0}'.format(kwds['help'])
        return vals

    def __str__(self):
        code = self.code()
        # imports now populated; prepend them to the code
        imports = '\n'.join(self.imports)
        return "{0}\n\n{1}\n\n\n{2}\n".format(self.file_comment, imports, code)


class StringSchema(SchemaFile):
    enum_template = """class {cls}(T.Enum):
    def __init__(self, default_value=T.Undefined, **metadata):
        super({cls}, self).__init__({values},
                                    default_value=default_value,
                                    **metadata)"""
    string_template = """class {cls}(T.Unicode):
    pass"""

    def __init__(self, name, schema, full_schema):
        self.name = name
        self.schema = schema
        self.full_schema = full_schema
        self.imports = ['import traitlets as T']

    def code(self):
        if 'enum' in self.schema:
            values = self.schema['enum']
            return self.enum_template.format(cls=self.name,
                                             values=values)
        else:
            return self.string_template.format(cls=self.name)


class ObjectSchema(SchemaFile):
    class_template = """class {name}(BaseObject):\n"""
    attr_template = """    {0} = {1}\n"""

    def __init__(self, name, schema, full_schema):
        self.name = name
        self.schema = schema
        self.full_schema = full_schema
        self.prop_dict = schema['properties']
        self.imports = ['import traitlets as T',
                        'from ..baseobject import BaseObject']

    def code(self):
        code = self.class_template.format(name=self.name)
        code += ''.join(self.attr_template.format(key, self.any_attribute(val))
                       for key, val in sorted(self.prop_dict.items()))
        return code

    def any_attribute(self, attr_dict):
        if 'type' in attr_dict:
            return self.type_attribute(attr_dict)
        elif '$ref' in attr_dict:
            return self.ref_attribute(attr_dict)
        elif 'oneOf' in attr_dict:
            return self.oneof_attribute(attr_dict)
        else:
            raise NotImplementedError('unrecognized keys')

    def type_attribute(self, attr_dict):
        kwds = {}
        kwds['allow_none'] = 'True'
        kwds['default_value'] = 'None'
        if 'description' in attr_dict:
            kwds['help'] = self.format_help_string(attr_dict['description'],
                                                   summarize=True)

        tp = attr_dict["type"]

        if tp == "array":
            typename = self.any_attribute(attr_dict['items'])
            return "T.List({0}, {1})".format(typename, self.kwds_to_str(kwds))
        elif tp == "boolean":
            return "T.Bool({0})".format(self.kwds_to_str(kwds))
        elif tp == "number":
            if 'minimum' in attr_dict:
                kwds['min'] = attr_dict['minimum']
            if 'maximum' in attr_dict:
                kwds['max'] = attr_dict['maximum']
            return "T.CFloat({0})".format(self.kwds_to_str(kwds))
        elif tp == "string":
            return "T.Unicode({0})".format(self.kwds_to_str(kwds))
        elif tp == "object":
            return "T.Any({0})".format(self.kwds_to_str(kwds))
        else:
            raise NotImplementedError(tp)

    def ref_attribute(self, attr_dict):
        kwds = {}
        kwds['allow_none'] = 'True'
        kwds['default_value'] = 'None'
        if 'description' in attr_dict:
            kwds['help'] = self.format_help_string(attr_dict['description'],
                                                   summarize=True)


        pound, cls, name = attr_dict['$ref'].split('/')
        self.imports.append('from .{0} import {1}'
                            ''.format(name.lower(), name))

        reftype = self.full_schema['definitions'][name]['type']
        if reftype == 'object':
            return "T.Instance({0}, {1})".format(name, self.kwds_to_str(kwds))
        elif reftype == 'string':
            return "{0}({1})".format(name, self.kwds_to_str(kwds))
        else:
            raise NotImplementedError("type = '{0}'".format(reftype))

    def oneof_attribute(self, attr_dict):
        types = (self.any_attribute(attr) for attr in attr_dict['oneOf'])
        return "T.Union([{0}])".format(', '.join(types))


def read_vegalite_schema():
    """Read the vega-lite schema and return as a Python dict"""
    schema_file = os.path.join(os.path.dirname(__file__),
                               'altair', 'schema',
                               'vega-lite-schema.json')
    with open(schema_file) as f:
        schema = json.load(f)

    return schema


def iterate_schemas():
    schema = read_vegalite_schema()
    for key, val in schema['definitions'].items():
        if val['type'] == 'object':
            yield key, ObjectSchema(key, val, schema)
        elif val['type'] == 'string':
            yield key, StringSchema(key, val, schema)
        else:
            raise NotImplementedError(val['type'])


def write_files(directory=None, verbose=True):
    directory = os.path.join(os.path.dirname(__file__),
                             'altair', 'schema', '_generated')

    if verbose:
        print("writing Python schema to {0}".format(directory))
    if not os.path.exists(directory):
        if verbose:
            print("creating directory {0}".format(directory))
        os.makedirs(directory)

    with open(os.path.join(directory, '__init__.py'), 'w') as initfile:
        initfile.write('"""Auto-generated Python '
                       'wrappers for vegalite schema"""\n')

        for name, code in sorted(iterate_schemas()):
            filename = os.path.join(directory, '{0}.py'.format(name.lower()))
            if verbose:
                print("writing {0} to {1}".format(name, filename))
            with open(filename, 'w') as codefile:
                codefile.write(str(code))
            initfile.write("\nfrom .{0} import {1}".format(name.lower(), name))


if __name__ == '__main__':
    write_files()
