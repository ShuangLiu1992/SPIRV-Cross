from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, cmake_layout


class SPIRVCROSSConan(ConanFile):
    name = "spirv_cross"
    settings = "os", "compiler", "build_type", "arch"

    generators = "CMakeToolchain"

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append("share")
