from FileManager import *
from timeit import default_timer
from sys import argv, exit


if __name__ == '__main__':

    if '-h' in argv:
        print("""
tree by Zhirui Dai.
This program is a simple tree tool.
tree is a useful program to print the directory structure.
On Ubuntu, tree is provided by default.

The structure of this program:
|-- main.py
|   |-- FileManager.py: create the root, perform tree traversal and print the tree. 
|   |   |-- FileNode.py: load the content and create child nodes.
|   |   |   |-- TaskQueue.py: a simple task queue to avoid deep function call stack.
|-- UnitTest.py: Unit test script.
""")
        exit(0)

    file_manager = FileManager()
    if len(argv) > 1:
        url = os.path.expanduser(argv[1])
    else:
        url = input("Please input the directory path to build a tree: ")
        url = os.path.expanduser(url)

    assert os.path.exists(url), "{} doesn't exist!".format(url)
    begin = default_timer()
    file_manager.load_directory(url=url)
    file_manager.print_tree()
    end = default_timer()
    print("\nCPU time used: {}s".format(end - begin))
