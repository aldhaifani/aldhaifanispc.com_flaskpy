import os
import sys
import pip


sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(
        ["%s==%s" % (i.key, i.version) for i in installed_packages]
    )
    version = "Python v" + sys.version.split()[0] + "\n"
    response = "\n".join([installed_packages, version])
    return [response.encode()]
