import os
from enum import Enum
from TaskQueue import TaskQueue


class FileNode:
    """
    FileNode class for building up a file tree
    """
    class NodeType(Enum):
        File: int = 0
        Dir: int = 1

    file_task_queue = TaskQueue()

    def __init__(self, url, node_type: NodeType = NodeType.File):
        self.url = url
        self.name = os.path.basename(self.url)
        self.child_nodes = dict()
        if os.path.exists(self.url):
            if os.path.isdir(self.url):
                self.node_type = FileNode.NodeType.Dir
                FileNode.file_task_queue.add_task(FileNode.load_directory_task(self))
            else:
                self.node_type = FileNode.NodeType.File
        else:
            self.node_type = node_type

    @property
    def node_size(self):
        return os.path.getsize(self.url)

    def load_directory(self):
        assert os.path.exists(self.url), "{} doesn't exist on the disk".format(self.url)
        assert self.node_type == FileNode.NodeType.Dir and os.path.isdir(self.url), \
            "Node should be a directory node!"
        items = os.listdir(self.url)
        for item in items:
            node = FileNode(url=os.path.join(self.url, item))
            self.add_child(node)
            # if node.node_type == FileNode.NodeType.Dir:

    def add_child(self, child):
        """
        Add a child node, only available for directory node.
        :param child: The child node to add.
        :return: Nothing.
        """
        assert type(child) is FileNode
        assert child.name not in self.child_nodes.keys(), "Child node '{}' already exists!".format(child.name)
        self.child_nodes[child.name] = child
        if not os.path.dirname(child.url) == self.url:
            child.url = os.path.join(self.url, child.name)   # update child.url

    def remove_child(self, child_name):
        """
        Remove a child node, only available for directory node.
        :param child_name: Name of the child node to remove.
        :return: Nothing.
        """
        assert type(child_name) is str
        assert child_name in self.child_nodes.keys(), "Child node '{}' doesn't exist!".format(child_name)
        del self.child_nodes[child_name]

    @staticmethod
    def load_directory_task(node):
        assert type(node) is FileNode

        def do_load_directory():
            node.load_directory()

        return do_load_directory

    @staticmethod
    def run_task_queue():
        while len(FileNode.file_task_queue.task_queue) > 0:
            FileNode.file_task_queue.task_queue[0]()
            del FileNode.file_task_queue.task_queue[0]
