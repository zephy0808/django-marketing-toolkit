django-marketing-toolkit
========================

A comprehensive Django package that provides essential marketing functionality including analytics tracking, landing pages, signup forms, and Active Campaign integration.

## Features

- 🔍 **Analytics Tracking**: Google Analytics, Google Tag Manager, Twitter Pixel, and Active Campaign event tracking
- 🎯 **Landing Pages**: Targeted landing pages with admin interface
- 📝 **Signup Forms**: Active Campaign integrated signup forms
- 🖼️ **Preview Slideshows**: Drag-and-drop sortable preview galleries
- ⚡ **Event Tracking**: Comprehensive event tracking with Active Campaign
- 🎨 **Template Tags**: Easy-to-use template tags for all tracking scripts

## Installation

### Using pip

```bash
pip install git+https://github.com/zephy0808/django-marketing-toolkit.git
```

Add to your `requirements.txt`:

```bash
-e git+https://github.com/zephy0808/django-marketing-toolkit.git#egg=django_marketing_toolkit
```

### Using pipenv

```bash
pipenv install git+https://github.com/zephy0808/django-marketing-toolkit.git#egg=django_marketing_toolkit
```

## Quick Start

Add the base package to your Django settings:

```python
INSTALLED_APPS = [
    # ... your other apps
    'eti_marketing',
]
```

## Configuration

### Analytics & Tracking

Configure tracking services by adding these settings to your `settings.py`:

```python
# Google Analytics
GOOGLE_ANALYTICS_ID = 'G-XXXXXXXXXX'

# Google Tag Manager
GOOGLE_TAGMANAGER_ID = 'GTM-XXXXXX'

# Active Campaign Event Tracking
ACTIVE_CAMPAIGN_EVENT_ACTID = 'your_numeric_id'

# Twitter Pixel
TWITTER_PIXEL_ID = 'your_twitter_pixel_id'
```

Add tracking scripts to your templates:

```html
{% load marketing %}

<html>
<head>
  <!-- Analytics tracking scripts -->
  {% google_analytics %}
  {% google_tagmanager %}
  {% active_campaign_event_tracker %}
  {% twitter_pixel_tracker %}
</head>
<body>
  <!-- GTM noscript fallback -->
  {% google_tagmanager_noscript %}
  
  <!-- Your content -->
</body>
</html>
```

### Landing Pages

Create targeted landing pages with rich content editing:

1. **Add to INSTALLED_APPS:**

```python
INSTALLED_APPS = [
    # ... your other apps
    'eti_marketing',
    'eti_marketing.landing_page',
    'ckeditor',
]
```

2. **Include URLs:**

```python
# urls.py
urlpatterns = [
    path('pages/', include('eti_marketing.landing_page.urls')),
]
```

3. **Run migrations:**

```bash
python manage.py migrate
```

4. **Configure site domain** in Django admin under **Sites** for proper "View on Site" functionality.

### Preview Slideshows

Add interactive, sortable preview galleries:

1. **Add to INSTALLED_APPS:**

```python
INSTALLED_APPS = [
    # ... your other apps
    'eti_marketing',
    'eti_marketing.preview',
    'ckeditor',
    'adminsortable2',
]
```

2. **Include URLs:**

```python
urlpatterns = [
    path('preview/', include('eti_marketing.preview.urls')),
]
```

3. **Run migrations:**

```bash
python manage.py migrate
```

### Active Campaign Integration

#### Signup Forms

Configure Active Campaign API settings:

```python
# Active Campaign API Configuration
ACTIVE_CAMPAIGN_API_URL = 'https://your-account.api-us1.com'
ACTIVE_CAMPAIGN_API_KEY = 'your_api_key'

# Optional: Auto-subscribe to lists
ACTIVE_CAMPAIGN_LIST_SUBSCRIPTIONS = [1, 2, 3]  # List IDs

# Optional: Track signup events
ACTIVE_CAMPAIGN_SIGNUP_EVENT = 'user_signup'
```

Add signup view to your URLs:

```python
# urls.py
from eti_marketing.views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]
```

#### Event Tracking

Configure event tracking settings:

```python
ACTIVE_CAMPAIGN_EVENT_ACTID = 'your_act_id'
ACTIVE_CAMPAIGN_EVENT_KEY = 'your_event_key'
```

Track events in your code:

```python
from eti_marketing.active_campaign import track_event

# Track a simple event
track_event('user@example.com', 'page_view')

# Track an event with additional data
track_event('user@example.com', 'purchase', {
    'product': 'Premium Plan',
    'amount': 99.99
})
```

## Customization

### Custom Templates

Override the base template used by all marketing templates:

```python
ETI_MARKETING_BASE_TEMPLATE = 'your_custom_base.html'
```

### Custom Signup Forms

Extend the signup form for additional fields:

```python
# forms.py
from eti_marketing.forms import SignupForm

class CustomSignupForm(SignupForm):
    company = forms.CharField(max_length=100)
    
    def save(self):
        # Custom save logic
        super().save()
```

Configure your custom form:

```python
ETI_MARKETING_SIGNUP_FORM_CLASS = 'myapp.forms.CustomSignupForm'
```

## Development

### Setup Development Environment

```bash
make init
```

### Available Commands

```bash
make migrations    # Generate new migrations
make test         # Run test suite
make lint         # Run code linting
make coverage     # Run tests with coverage report
```

## Requirements

- Django >= 3.2
- Python >= 3.8

### Optional Dependencies

- `django-ckeditor` - For rich text editing in landing pages
- `django-admin-sortable2` - For drag-and-drop sorting in preview app

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on GitHub or contact the development team.
