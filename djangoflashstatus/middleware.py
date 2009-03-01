class FlashStatusMiddleware:

    def process_request(self, request):
        """Convenience methods for adding status and error messages to django-flash."""
        request.__class__.add_status   = add_status
        request.__class__.add_error    = add_error
        request.__class__.add_message  = add_message


def add_message(self, key, msg):
    """Creates a list of messages for a particular key.

    Used to create lists of status and error messages but
    could be used to make other lists for the flash.
    """
    if key in self.flash:
        self.flash[key].append(msg)
    else:
        self.flash[key] = [msg]

def add_error(self, msg):
    add_message(self, 'errors', msg)

def add_status(self, msg):
    add_message(self, 'statuses', msg)