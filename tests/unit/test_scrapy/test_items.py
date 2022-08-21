import unittest

from themispy.scrapy.items import FileDownloader


class TestFileDownloader(unittest.TestCase):
    """Test Class for ``FileDownloader`` class in ``items.py``."""
    
    def test_file_downloader_contains_file_attributes(self):
        """
        GIVEN user wants to use the Scrapy file downloader pipeline\n
        WHEN user defines Scrapy item class\n
        THEN assert that given class has properly attributes.
        """
        item = FileDownloader()
        self.assertIn('file_urls',item.fields.keys())
        self.assertIn('files', item.fields.keys())
    
    
if __name__ == '__main__':
    unittest.main()
