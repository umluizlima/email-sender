# email-sender
A service to send email messages.

### Features
- Multiple email service integrations that can be easily switched;
- Send emails with POST requests;
- Requests must be authenticated with the [x-api-key](https://stoplight.io/blog/api-keys-best-practices-to-authenticate-apis/) header;
- Request body validation with [pydantic](https://pydantic-docs.helpmanual.io/);
- Auto-generated API docs with [fastapi](https://fastapi.tiangolo.com/)

### Resources (all on free tiers)
- [Heroku](https://www.heroku.com/free) for automated deployment;
- [Mailjet](https://www.mailjet.com/pricing/) as an email service alternative (default);
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
```console
make run
```
Access the API documentation on http://localhost:8000/docs and use the default `API_KEY` to authenticate (check it on `Settings` class).

You can run the app and test its API as is, but no emails will be sent. To do so, you'll have to [set up an email service](#setting-up-an-email-service).

### Setting up an email service

The email service can be chosen by setting the `EMAIL_SERVICE` environment variable to one of the values available on `EmailService` enum ("mailjet" by default).

After choosing which service to use you'll need to:
1. Sign up on its platform;
2. Verify your email address as an authorized sender;
3. Generate and set the API key as environment variable (check `Settings` class for naming references);

The verified email address must be used either as the `from` attribute on requests or as the `DEFAUL_EMAIL_ADDRESS` environment variable.

If the available services do not suffice, you can [add a new email service integration](#adding-an-email-service-integration).

### Adding an email service integration

There are many email services available out there that you can choose from. If this project does not yet integrate with it, you can do so by:

1. Creating a `YourEmailServiceAdapter` class that extends `BaseAdapter` and implements its `send` method;
2. Adding a value to `EmailService` enum corresponding to your new service;
3. Mapping your new service on the `ADAPTERS` dictionary, so it can be chosen from by the `EMAIL_SERVICE` environment variable;
