#!/usr/bin/env python
#
# PoC hack to demonstrate one possible way to template a boot job with multiple tests
# The "test_templates" variable is a list of simple jinja2 templates
#

import os
import glob
from jinja2 import Environment, FileSystemLoader

template_file = os.path.join("boot", "generic-uboot-tftp-ramdisk-template.jinja2")
job_file = "job-multitest.yaml"

job = {}
job['short_template_file'] = template_file
job['kernel_image'] = "Image"
job['test_templates'] = ("tests/test1.jinja2", "tests/test2.jinja2")

def jinja_render(job):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(job['short_template_file'])
    return template.render(job)

def main():
    with open(job_file, 'w') as f:
        f.write(jinja_render(job))
    print "Job written: %s" % job_file

if __name__ == '__main__':
    main()
    
