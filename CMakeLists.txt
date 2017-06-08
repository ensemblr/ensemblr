cmake_minimum_required(VERSION 3.5)

project(ensemblr C CXX)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/Modules)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/build/private/local_config.cmake)
  include(${CMAKE_CURRENT_SOURCE_DIR}/build/private/local_config.cmake)
endif()
