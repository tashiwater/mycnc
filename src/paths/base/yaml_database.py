#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
class YamlDatabase():

    def __init__(self, yaml_path):
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.yaml_folder = current_path + "./../../../data/yaml/"
        self.__yaml_path = self.yaml_folder + yaml_path
        self.load_from_file()


    def load_from_file(self):
        with open(self.__yaml_path, 'r') as f:
            self.__all_data = yaml.load(f)


    def dump_to_file(self):
        with open(self.__yaml_path, 'w') as f:
            f.write(yaml.dump(self.__all_data, default_flow_style=False))


    def get(self, name):
        if name not in self.__all_data:
            return None
        data = self.__all_data[name]
        return data


    def keys(self):
        return self.__all_data.keys()


    def register(self, name, data):
        self.__all_data[name] = data


    def delete(self, name):
        if name not in self.__all_data:
            return None

        del self.__all_data[name]
