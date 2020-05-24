# email-sender
A service to send email messages.

### Features
- Send emails on received POST requests;
- Requests must be authenticated with the [x-api-key](https://stoplight.io/blog/api-keys-best-practices-to-authenticate-apis/) header;
- Request body validation with [pydantic](https://pydantic-docs.helpmanual.io/);
- Auto-generated API docs with [fastapi](https://fastapi.tiangolo.com/)

### Integrations (all on free tiers)
- [Heroku](https://www.heroku.com/free) for automated deployment;
- [Mailjet](https://www.mailjet.com/pricing/) as an email service alternative;
- [Sendgrid](https://sendgrid.com/pricing/) as another email service alternative;
- [Sentry](https://sentry.io/pricing/) for error tracking;
- [Travis-CI](https://travis-ci.com/plans) for automated testing;

## Development

### Requirements
- Python 3.8.1

### Installing
Install dependencies
```console
make install
```

### Testing
```console
make test
```

### Running
Access the API documentation on http://localhost:8000/docs
```console
make run
```
