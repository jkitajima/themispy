import unittest

from themispy.scrapy.readers import read_jsonlines_blob


class TestReadJsonlinesBlob(unittest.TestCase):
    """Test Class for ``read_jsonlines_blob`` function in ``readers.py``."""
    
    def test_blob_name_endswith_jsonl(self):
        """
        GIVEN user wants to read a jsonlines blob\n
        WHEN user passes blob name\n
        THEN assert exception is raised if blob name does not endswith ``.jsonl`` extension.
        """
        blob_name = 'filename.xml'
        
        with self.assertRaises(Exception):
            read_jsonlines_blob(blob=blob_name)


if __name__ == '__main__':
    unittest.main()
