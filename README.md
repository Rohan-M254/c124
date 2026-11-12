# Contacts API

A small Flask learning project that demonstrates basic JSON API operations.

## Requirements

- Python 3
- Flask

Install Flask:

```bash
python -m pip install Flask
```

Run the application:

```bash
python flask.py
```

The development server runs at the local address printed by Flask.

## Endpoints

### `GET /`

Returns a basic API status message.

### `GET /contacts`

Returns the contacts currently held in memory.

### `POST /contacts`

Creates a contact. Send a JSON object with a non-empty `name` field and an optional string `contact` field.

Example request body:

```json
{
  "name": "Example Person",
  "contact": "example"
}
```

## Limitations

- Data is stored in memory and is lost when the application restarts.
- This is a learning example, not a production contacts service.
- It has no authentication, authorisation, database or automated tests.
- Do not use real personal contact information in the demo.

## Security and privacy

The original hardcoded sample contact records have been removed from the current source. If those values represented real people, consider whether the public Git history also needs remediation; deleting them from the latest version does not erase previous commits.
