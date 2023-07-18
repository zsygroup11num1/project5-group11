# project5-group11
定义MerkleTree类：我首先定义了一个名为MerkleTree的类，用于表示Merkle树。该类包含以下方法：

__init__方法：这是类的构造函数，用于初始化MerkleTree对象。它接受一个data_list参数，该参数是一个包含要存储在Merkle树中的数据的列表。

build_tree方法：这是构建Merkle树的核心方法。我首先将数据列表中的每个数据元素转换为叶子节点，并计算其哈希值，形成一个初始的树。然后，我使用while循环来迭代构建Merkle树，直到根节点形成。在每个迭代步骤中，我按照两两组合的方式计算父节点的哈希值，并构建下一层的树。这样不断迭代，直到树的根节点计算出来。

hash_data方法：这是一个辅助方法，用于计算给定数据的哈希值。在这里，我使用SHA-256哈希函数对数据进行哈希。

combine_hashes方法：这也是一个辅助方法，用于将两个子节点的哈希值组合成一个父节点的哈希值。在这里，我将左子节点和右子节点的哈希值串联在一起，并再次使用哈希函数对其进行哈希，得到父节点的哈希值。

get_root_hash方法：这是用于获取Merkle树的根节点哈希值的方法。根节点哈希值是整个Merkle树的唯一标识，可以用于验证数据的完整性。

Example usage：在代码的最后部分，我演示了如何使用MerkleTree类来构建Merkle树并获取其根节点的哈希值。

运行结果：<img width="582" alt="bf8610599146cccfd46c8979b2bc232" src="https://github.com/zsygroup11num1/project5-group11/assets/129477117/81dec6d3-4a8a-4b7b-aee1-6f871ba5b275">
