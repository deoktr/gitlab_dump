# gitlab_dump

Clone every accessible Gitlab repository.

This can be usefull during red team engagment if you come across a Gitlab server and want to analyse everything offline.

## Requirements

You need to have a user account and to generate a Gitlab API token.

## Usage

Setup:

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
python main.py https://gitlab_host.local YOUR_GITLAB_TOKEN
```

## License

[MIT](./LICENSE)
