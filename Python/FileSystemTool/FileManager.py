from FileNode import *


class FileManager:

    def __init__(self):
        """
        init
        """
        self.root_path = os.curdir
        self.tree = None

    def load_directory(self, url=os.curdir):
        """
        Read and load the file tree.
        :param url: path of the directory
        :return: nothing
        """
        assert os.path.isdir(url), "{} is not a directory!".format(url)
        self.root_path = url
        self.tree = FileNode(self.root_path)
        self.tree.run_task_queue()

    def print_tree(self):
        print("Path of the root: {}".format(self.root_path))
        assert type(self.tree) is FileNode, "Please call load_directory before call print_tree!"
        print(".")

        node_stack = [self.tree]
        child_node_index_stack = [0]
        dir_count = 0
        file_count = 0

        while len(node_stack) > 0:
            current_node = node_stack.pop()
            current_depth = len(node_stack)
            current_child_names = sorted(current_node.child_nodes.keys())
            current_child_node_index = child_node_index_stack.pop()
            current_child_num = len(current_child_names)
            for index in range(current_child_node_index, current_child_num):
                child_node = current_node.child_nodes[current_child_names[index]]
                print('|   ' * current_depth, end='')
                print('{} {}'.format('└──' if index == current_child_num - 1 else '├──', child_node.name))

                if child_node.node_type == FileNode.NodeType.Dir:
                    dir_count += 1
                    node_stack.append(current_node)
                    child_node_index_stack.append(index + 1)
                    node_stack.append(child_node)
                    child_node_index_stack.append(0)
                    break
                else:
                    file_count += 1

        print("\n{} directory{}, {} file{}.".format(
            dir_count, 's' if dir_count > 0 else '', file_count, 's' if file_count > 0 else '')
        )


