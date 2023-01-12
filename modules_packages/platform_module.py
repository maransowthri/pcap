import platform

# To see generic operating system name

print(platform.system())

# To see the OS installed

print(platform.platform())

# To see the system's release version

print(platform.version())

# To see brief form

print(platform.platform(aliased=True, terse=True))

# To see the short name of the processor

print(platform.machine())

# To see the real name of the processor

print(platform.processor())

# To see the name of the python implementation

print(platform.python_implementation())

# To see Python version as a tuple

print(platform.python_version_tuple())
