import re
from django.conf import settings


class MobileTemplateView(object):
    """
    Change template_name based on domain.
    """
    template_name = NotImplemented

    @staticmethod
    def is_mobile(host):
        """
        Check if domain is matched to regex.

        :param host: hostname.
        :type host: str
        :rtype: bool
        :return: true if domain is mobile.
        """
        if hasattr(settings, 'MOBILE_DOMAIN_REGEX'):
            regex = re.compile(settings.MOBILE_DOMAIN_REGEX)
        else:
            regex = re.compile('^m.\.*.\.*.*')

        if regex.match(host):
            return True
        else:
            return False

    def get_template_names(self):
        """
        Overriding default method to be able change template_name dynamically.

        :rtype: list
        :return: template names list.
        """
        if self.is_mobile(self.request.get_host()):
            if hasattr(settings, 'MOBILE_TEMPLATES_PREFIX'):
                return [settings.MOBILE_TEMPLATES_PREFIX + self.template_name, ]
            else:
                return ['mobile/' + self.template_name, ]

        return [self.template_name]
