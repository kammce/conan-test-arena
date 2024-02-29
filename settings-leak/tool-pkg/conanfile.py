from conan import ConanFile


required_conan_version = ">=2.1.0"


class tool_pkg(ConanFile):
    name = "tool-pkg"
    version = "1.0.0"
    settings = "os", "arch", "compiler", "build_type", "libc"
    package_type = "application"
    short_paths = True

    @property
    def target_settings_available(self):
        return (self.settings_target and self.settings_target.get_safe('libc'))

    def validate(self):
        pass

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.bindirs = ["bin"]

        if self.target_settings_available:
          libc = self.settings_target.get_safe("libc")
          if libc == "custom":
              self.output.warning("✅ LIBC: custom")
          else:
              self.output.warning(f"❌ LIBC: {libc}")
        else:
            self.output.warning("target settings unavailable")

    def package_id(self):
        pass
