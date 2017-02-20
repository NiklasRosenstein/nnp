# Copyright (c) 2017 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configparser
import os


def _get_config():
  """
  Returns the nnp configuration. Section and option keys are joined together
  by a double-color (`:`). By default, the configuration file is located at
  `~/.nnp/config`. The `NNP_CONFIG` environment variable may override this
  filename.
  """

  config = {}
  filename = os.path.expanduser(os.getenv('NNP_CONFIG', '~/.nnp/config'))
  if os.path.isfile(filename):
    parser = configparser.SafeConfigParser()
    parser.read([filename])
    for section in parser.sections():
      for option, value in parser.items(section):
        config[section + ':' + option] = value

  return config


config = _get_config()
config.setdefault('nnp:prefix', os.getenv('NNP_PREFIX', '~/.nnp'))
config.setdefault('nnp:local_packages_dir', 'nnp_packages')
config['nnp:prefix'] = os.path.expanduser(config['nnp:prefix'])