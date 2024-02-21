import os
import sys
import pkg_resources


sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(
        ["%s==%s" % (i.key, i.version) for i in installed_packages]
    )
    version = "Python v" + sys.version.split()[0] + "\n"
    response = "\n".join([str(installed_packages_list), version])
    return [response.encode()]
