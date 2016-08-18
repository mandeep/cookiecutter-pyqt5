import os
import pytest


@pytest.fixture
def context():
    return {
        "full_name": "Lisa Simpson",
        "email": "smartgirl63_\@yahoo.com",
        "github_username": "none",
        "repo_name": "Lisa_Lionheart",
        "package_name": "lisa",
        "application_name": "saxophone",
        "application_title": "Saxophone",
        "project_short_description": "Learn how to play the sax.",
        "version": "0.0.1",
        "insert_menubar": "yes",
        "insert_statusbar": "yes"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files.
    Borrowed from https://github.com/pydanny/cookiecutter-django/"""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def test_template(cookies, context):
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'Lisa_Lionheart'
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
