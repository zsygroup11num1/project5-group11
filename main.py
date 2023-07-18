import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.data_list = data_list
        self.tree = self.build_tree()

    def build_tree(self):
        tree = [self.hash_data(data) for data in self.data_list]

        while len(tree) > 1:
            tree_level = []
            for i in range(0, len(tree), 2):
                left_child = tree[i]
                right_child = tree[i + 1] if i + 1 < len(tree) else ''
                combined_hash = self.combine_hashes(left_child, right_child)
                tree_level.append(combined_hash)
            tree = tree_level

        return tree

    def hash_data(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def combine_hashes(self, left_hash, right_hash):
        combined_hash = left_hash + right_hash
        return self.hash_data(combined_hash)

    def get_root_hash(self):
        return self.tree[0]

# Example usage:
if __name__ == "__main__":
    data_list = ["Data1", "Data2", "Data3", "Data4", "Data5"]
    merkle_tree = MerkleTree(data_list)
    print("Merkle Tree Root Hash:", merkle_tree.get_root_hash())
