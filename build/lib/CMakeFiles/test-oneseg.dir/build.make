# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jordy/gr-oneseg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jordy/gr-oneseg/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-oneseg.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-oneseg.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-oneseg.dir/flags.make

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o: lib/CMakeFiles/test-oneseg.dir/flags.make
lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o: ../lib/test_oneseg.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jordy/gr-oneseg/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-oneseg.dir/test_oneseg.cc.o -c /home/jordy/gr-oneseg/lib/test_oneseg.cc

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-oneseg.dir/test_oneseg.cc.i"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jordy/gr-oneseg/lib/test_oneseg.cc > CMakeFiles/test-oneseg.dir/test_oneseg.cc.i

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-oneseg.dir/test_oneseg.cc.s"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jordy/gr-oneseg/lib/test_oneseg.cc -o CMakeFiles/test-oneseg.dir/test_oneseg.cc.s

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.requires:

.PHONY : lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.requires

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.provides: lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-oneseg.dir/build.make lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.provides

lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.provides.build: lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o


lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o: lib/CMakeFiles/test-oneseg.dir/flags.make
lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o: ../lib/qa_oneseg.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jordy/gr-oneseg/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o -c /home/jordy/gr-oneseg/lib/qa_oneseg.cc

lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-oneseg.dir/qa_oneseg.cc.i"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jordy/gr-oneseg/lib/qa_oneseg.cc > CMakeFiles/test-oneseg.dir/qa_oneseg.cc.i

lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-oneseg.dir/qa_oneseg.cc.s"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jordy/gr-oneseg/lib/qa_oneseg.cc -o CMakeFiles/test-oneseg.dir/qa_oneseg.cc.s

lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.requires:

.PHONY : lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.requires

lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.provides: lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-oneseg.dir/build.make lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.provides

lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.provides.build: lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o


lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o: lib/CMakeFiles/test-oneseg.dir/flags.make
lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o: ../lib/qa_ofdm_synchronization_1seg.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jordy/gr-oneseg/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o -c /home/jordy/gr-oneseg/lib/qa_ofdm_synchronization_1seg.cc

lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.i"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jordy/gr-oneseg/lib/qa_ofdm_synchronization_1seg.cc > CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.i

lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.s"
	cd /home/jordy/gr-oneseg/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jordy/gr-oneseg/lib/qa_ofdm_synchronization_1seg.cc -o CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.s

lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.requires:

.PHONY : lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.requires

lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.provides: lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-oneseg.dir/build.make lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.provides

lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.provides.build: lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o


# Object files for target test-oneseg
test__oneseg_OBJECTS = \
"CMakeFiles/test-oneseg.dir/test_oneseg.cc.o" \
"CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o" \
"CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o"

# External object files for target test-oneseg
test__oneseg_EXTERNAL_OBJECTS =

lib/test-oneseg: lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o
lib/test-oneseg: lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o
lib/test-oneseg: lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o
lib/test-oneseg: lib/CMakeFiles/test-oneseg.dir/build.make
lib/test-oneseg: /usr/local/lib/libgnuradio-runtime.so
lib/test-oneseg: /usr/local/lib/libgnuradio-pmt.so
lib/test-oneseg: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-oneseg: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-oneseg: /usr/lib/x86_64-linux-gnu/libcppunit.so
lib/test-oneseg: lib/libgnuradio-oneseg-1.0.0git.so.0.0.0
lib/test-oneseg: /usr/local/lib/libgnuradio-runtime.so
lib/test-oneseg: /usr/local/lib/libgnuradio-pmt.so
lib/test-oneseg: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-oneseg: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-oneseg: lib/CMakeFiles/test-oneseg.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jordy/gr-oneseg/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable test-oneseg"
	cd /home/jordy/gr-oneseg/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-oneseg.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-oneseg.dir/build: lib/test-oneseg

.PHONY : lib/CMakeFiles/test-oneseg.dir/build

lib/CMakeFiles/test-oneseg.dir/requires: lib/CMakeFiles/test-oneseg.dir/test_oneseg.cc.o.requires
lib/CMakeFiles/test-oneseg.dir/requires: lib/CMakeFiles/test-oneseg.dir/qa_oneseg.cc.o.requires
lib/CMakeFiles/test-oneseg.dir/requires: lib/CMakeFiles/test-oneseg.dir/qa_ofdm_synchronization_1seg.cc.o.requires

.PHONY : lib/CMakeFiles/test-oneseg.dir/requires

lib/CMakeFiles/test-oneseg.dir/clean:
	cd /home/jordy/gr-oneseg/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-oneseg.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-oneseg.dir/clean

lib/CMakeFiles/test-oneseg.dir/depend:
	cd /home/jordy/gr-oneseg/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jordy/gr-oneseg /home/jordy/gr-oneseg/lib /home/jordy/gr-oneseg/build /home/jordy/gr-oneseg/build/lib /home/jordy/gr-oneseg/build/lib/CMakeFiles/test-oneseg.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-oneseg.dir/depend

