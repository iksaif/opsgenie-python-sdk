from unittest import TestCase

from opsgenie.core.config import Configuration, HttpConfiguration


class TestConfiguration(TestCase):
    def test_config(self):
        configuration = Configuration(apikey="API_KEY",
                                      http_config=HttpConfiguration(connect_timeout=20),
                                      proxy_config={'host': "HOST", 'port': "PORT", 'protocol': 'HTTPS'})

        configuration.validate()
        self.assertEqual('API_KEY', configuration.apikey)
        self.assertEqual(20, configuration.http_config.connect_timeout)
        self.assertEqual("HOST", configuration.proxy_config.host)
        self.assertEqual("PORT", configuration.proxy_config.port)
        self.assertEqual("https", configuration.proxy_config.protocol)