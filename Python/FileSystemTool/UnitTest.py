import unittest
from FileManager import FileManager


class TestFileManager(unittest.TestCase):
    """
    Test FileManager
    """

    def test_load_directory(self):
        """
        Test load_directory
        :return: nothing
        """
        file_manager = FileManager()
        file_manager.load_directory(r'/Users/daizhirui/Downloads/COMSOL')

    def test_print_tree(self):
        file_manager = FileManager()
        file_manager.load_directory(r'/Users/daizhirui/Downloads/COMSOL')
        file_manager.print_tree()


if __name__ == '__main__':
    unittest.main()
    # a_list = ['berkeley', 'ucla', 'columbia']
    #
    # for item in enumerate(a_list):
    #     print(item)
    #     print(type(item))
    # for index, value in enumerate(a_list):
    #     print('{} --> {}'.format(index, value))
