from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class SPIRVCROSSConan(ConanFile):
    name = "spirv_cross"
    settings = "os", "compiler", "build_type", "arch"

    generators = "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append("share")
