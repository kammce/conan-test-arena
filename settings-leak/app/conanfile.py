from conan import ConanFile
from conan.tools.layout import basic_layout


class demos(ConanFile):
    settings = "compiler", "build_type", "os", "arch", "libc"
    generators = "VirtualBuildEnv"

    def layout(self):
        basic_layout(self)

    def validate(self):
        pass

    def build_requirements(self):
        pass

    def requirements(self):
        self.requires("library/1.0.0")

    def build(self):
        pass
