import click
import os
from click.testing import CliRunner
from tulip import tulip

here = os.path.abspath(os.path.dirname(__file__))
test_resources_path = os.path.join(here, 'test-resources')

get_test_resource_path = lambda s: os.path.join(test_resources_path, s)

def test_ascii_invocation():
    height, width = 39, 136
    
    runner = CliRunner()

    result = runner.invoke(tulip, [
        '--width', str(width), 
        '--height', str(height), 
        '--just-ascii', 
        get_test_resource_path('batman.png')
    ])

    assert result.exit_code == 0
    
    with open(get_test_resource_path('batman-ascii-output.txt')) as f:
        assert f.read() == result.output

        
def test_normal_invocation():
    height, width = 24, 80
    runner = CliRunner()

    result = runner.invoke(tulip, [
        '--width', str(width),
        '--height', str(height),
        get_test_resource_path('batman.png')
    ])

    assert result.exit_code == 0
    with open(get_test_resource_path('batman-output.txt')) as f:
        assert f.read() == result.output
