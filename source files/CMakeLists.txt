cmake_minimum_required(VERSION 3.10)
project(CookieCutterCNC)

# Force MinGW
set(CMAKE_GENERATOR "MinGW Makefiles" CACHE INTERNAL "" FORCE)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)

# Add SFML path (escaped parentheses with quotes)
set(SFML_DIR "C:/Users/Ayman Zahir UoY/Dropbox/My PC \(LAPTOP-3CCP2LSQ\)/Downloads/SFML-3.0.0-windows-gcc-14.2.0-mingw-64-bit/SFML-3.0.0")
message(STATUS "SFML_DIR is set to: ${SFML_DIR}")

# Add include directory
include_directories("${SFML_DIR}/include")

# Add source files
add_executable(CookieCutterCNC main.cpp SpiralToolpath.cpp Circle.cpp)

# Link SFML libraries manually
target_link_libraries(CookieCutterCNC
    "${SFML_DIR}/lib/libsfml-graphics.a"
    "${SFML_DIR}/lib/libsfml-window.a"
    "${SFML_DIR}/lib/libsfml-system.a"
)
