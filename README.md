# dotTest

> The name test is reserved by the Internet Engineering Task Force (IETF) in RFC 2606 (June 1999) as a domain name that is not intended to be installed as a top-level domain (TLD) in the global Domain Name System (DNS) of the Internet for production use.

dotTest is a small script which allows you to configure local .test domains to point to different ports on your machine. For example, if you're developing some software which consists of a frontend service (running on port 8000) and a backend service (running on port 8080), it can be more clear to use http://frontend.test and http://backend.test instead of http://localhost:8000 and http://localhost:8080. This is what dotTest allows.

You can install it with `pip install dottest` (or use [pipsy](https://github.com/mitsuhiko/pipsi) `pipsy install dottest`).

Right now this is only confirmed to work on MacOS High Sierra (it uses `/etc/hosts`, `pfctl`, and `ifconfig` as configured by default on MacOS High Sierra). There's no reason why it won't work on other \*nix systems which use these tools. If you need support for a different set of tools for your system, please submit a pull request.


It also does not work with Windows at all. If you can make it work for Windows please submit a pull request.

## Usage

Once installed, use `dottest add <domain> <port>` to begin directing a domain to a local port, and `dottest remove <domain>` to stop. `dottest list` will list currently configured domains, and `dottest clear` will remove all configured domains. `dottest init` should be run after restarting your computer to restore the configured domains.

## Discovery

`dottest auto [path]` can be used to automatically add domains configured in files within the given path (or the current directory if no path is supplied). By default, this works by recursively searching from the given path for files named `.dottest`. In this file, each line describes a domain in the form `domain.test=port` (e.g. `frontend.test=8000`).

If you use [Spring](https://spring.io), you can configure (see below) the "spring" discovery mechanism. This will recursively search for files named `src/main/resources/application-dev.properties` and `src/main/resources/application.properties` for lines of the form `server.port=port` (e.g. `server.port=8000`). If this line is found, then the domain name is given as the directory name followed by `.test`.

## Configuration

The default configuration is:
```yaml

domain_suffix: .test
address_prefix: 127.0.0.
discovery:
    - dottest
```

This can be changed globally by creating a `~/.dottest-config` file, or on a project-by-project bases by creating a `.dottest-config` file in the directory where you will run dottest. Any keys added to these files will overwrite the defaults.