import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import pytest

testdir = Path(__file__).parent
rootdir =  testdir.parent
path_16 = testdir.joinpath('utf16.txt')
path_8 = testdir.joinpath('utf8.txt')


@pytest.fixture(scope='function')
def tmp_out():
    tempdir = tempfile.mkdtemp()
    temp_path = os.path.join(tempdir, 'testfile')
    # tf = tempfile.NamedTemporaryFile(delete=False)
    # tf.file.close()
    # os.chmod(tf.name, mode=-0o777)
    yield temp_path
    shutil.rmtree(tempdir)


def test_16_to_8(tmp_out):
    completed = subprocess.run(
        ['python',
         str(rootdir.joinpath('convencode.py')),
         str(path_16),
         'utf-16',
         tmp_out,
         'utf-8',
         ],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    completed.check_returncode()
    with open(path_8, 'rb') as f_expected:
        expected = f_expected.read()
    with open(tmp_out, 'rb') as f_actual:
        actual = f_actual.read()
    assert actual == expected


def test_8_to_16(tmp_out):
    completed = subprocess.run(
        ['python',
         str(rootdir.joinpath('convencode.py')),
         str(path_8),
         'utf-8',
         tmp_out,
         'utf-16',
         ],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    assert completed.returncode == 0
    with open(path_16, 'rb') as f_expected:
        expected = f_expected.read()
    with open(tmp_out, 'rb') as f_actual:
        actual = f_actual.read()
    assert actual == expected
