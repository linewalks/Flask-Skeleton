"""
Check here when we need more argument options
https://github.com/miguelgrinberg/Flask-Migrate/blob/master/flask_migrate/__init__.py#L168
"""


import os
from alembic import command
from main import create_app


SCHEMA = "SCHEMA_TEST"


def replace_schema(txt, schema_name):
  txt = txt.replace(f"schema='{schema_name}'", f"schema=app.config['{SCHEMA}']")

  # for foreign key name
  txt = txt.replace(f"{schema_name}.", f"' + app.config['{SCHEMA}'] + '.")

  # for index name
  txt = txt.replace(f"_{schema_name}_", f"_' + app.config['{SCHEMA}'] + '_")

  code_start_idx = txt.find("from alembic")
  txt = txt[:code_start_idx] + f"\nfrom flask import current_app as app\n" + txt[code_start_idx:]
  return txt


def migrate(**kwargs):
  """Autogenerate a new revision file (Alias for
  'revision --autogenerate')
  """
  app = create_app()
  schema_name = app.config[SCHEMA]

  with app.app_context():
    config = app.extensions["migrate"].migrate.get_config(
        None, opts=["autogenerate"], x_arg=None)
    result_list = command.revision(config, None, autogenerate=True, sql=False,
                                   head="head", splice=False, branch_label=None,
                                   version_path=None, rev_id=None)
    if not isinstance(result_list, list):
      result_list = [result_list]

    for res in result_list:
      file_path = res.path
      with open(file_path, "r") as f:
        txt = replace_schema(f.read(), schema_name)

      with open(file_path, "w") as f:
        f.write(txt)


if __name__ == "__main__":
  migrate()
