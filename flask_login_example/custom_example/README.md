
Example modified from a DigitalOcean tutorial.

Made to be a "secret" admin with sign up through a JSON API endpoint.

Registering a user

```bash
curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username": "user", "password": "***", "name": "G"}'
```
