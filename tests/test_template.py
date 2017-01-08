import os
import pytest


@pytest.fixture
def context():
    """Test template creation with these parameters."""
    return {
        "full_name": "Lisa Simpson",
        "email": "smartgirl63_\@yahoo.com",
        "github_username": "none",
        "repo_name": "Lisa_Lionheart",
        "package_name": "lisa",
        "application_name": "saxophone",
        "application_title": "Saxophone",
        "project_short_description": "Learn how to play the sax.",
        "version": "0.0.2",
        "insert_statusbar": "yes"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files.
    Borrowed from https://github.com/pydanny/cookiecutter-django/"""
    return [os.path.join(dirpath, file_path) for dirpath, __, files in os.walk(root_dir)
            for file_path in files]


def test_template(cookies, context):
    """Test the template for proper creation."""
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'Lisa_Lionheart'
    assert result.project.isdir()


def test_setuptools(cookies, context):
    """Test setup.py for proper creation."""
    result = cookies.bake(extra_context=context)
    for file in build_files_list(str(result.project)):
        if 'setup.py' in file:
            test_setup_file = file

    with open(test_setup_file) as infile:
        for line in infile.readlines():
            if 'name=' in line:
                assert context['repo_name'] in line
            elif 'version=' in line:
                assert context['version'] in line
            elif 'description=' in line and 'long_description' not in line:
                assert context['project_short_description'] in line
            elif 'author=' in line:
                assert context['full_name'] in line
            elif 'author_email' in line:
                assert context['email'] in line
            elif 'url=' in line:
                assert 'https://github.com/{}/{}' .format(
                    context['github_username'], context['repo_name']) in line
            elif 'packages=' in line:
                assert context['package_name'] in line
            elif 'keywords=' in line:
                assert context['repo_name'] in line
            elif '{}:main' .format(context['application_name']) in line:
                assert '{}={}.{}:main' .format(
                    context['application_title'], context['package_name'],
                    context['application_name']) in line
