cmake_minimum_required(VERSION 3.16.3)

project(HelloWorld)

# Variable:
set (source_dir "${PROJECT_SOURCE_DIR}/src/") 

# Files to compile
file (GLOB source_files "${source_dir}/*.cpp")

add_executable (${PROJECT_NAME} ${source_files})

add_subdirectory(${source_dir}/Helper)
target_link_directories(${PROJECT_NAME} PRIVATE ${source_dir}/Helper/)
target_link_libraries(${PROJECT_NAME} helper)