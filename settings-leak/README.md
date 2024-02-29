# Settings leak to `test_package`

## Setup Steps

1. Make sure you are in the root of this directory, or in the same directory as
this README.md file. Also make sure your conan version is set to 2.1.0 using the following:

```bash
$ conan --version
Conan version 2.1.0
```

1. Install `user_settings.yml`:

```bash
conan config install -sf config .
```

## Demonstration

The tool-pkg prints out the LIBC value or prints out that the settings_target
does not exist for this build.

1. Build tool-pkg `conan create tool-pkg`. Should get:

```text
tool-pkg/1.0.0: WARN: target settings unavailable
```

1. Build library `conan create library -pr profile`. Incorrectly get `✅ LIBC: custom` for both the library and the test package even though neither requests
the libc setting.

2. Build app `conan build app -pr profile` and correctly get `✅ LIBC: custom`
