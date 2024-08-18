# Race Condition

This project uses [Poetry](https://python-poetry.org/docs/#installation)

## Quick start

```bash
poetry install
poetry shell
flask --app race_condition init-db
flask --app race_condition --debug run --host=0.0.0.0 --port=5000
```

# Administration

Register an admin account ASAP. New admin registrations will not be accepted once the first user has been registered
http://127.0.0.1:5000/auth/register

List admin capabilities
http://127.0.0.1:5000/admin

Contestants never need to leave the root of the site http://127.0.0.1:5000/

Admins can set the challenge that is active http://127.0.0.1:5000/problems/list/
