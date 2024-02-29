#!/usr/bin/python

from conan import ConanFile


required_conan_version = ">=2.1.0"


class library(ConanFile):
    name = "library"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"

    def validate(self):
       pass

    def build_requirements(self):
        pass

    def requirements(self):
        pass

    def layout(self):
        pass

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        pass

    def package_id(self):
        pass
