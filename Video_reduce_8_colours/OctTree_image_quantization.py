"""Image quantization algorithm using an OctTree.

A colour cube is recursively divided into 8 slices until each leaf node of the tree
represents a single colour (RGB value) in the image to be quantized. The number of
occurrences for each colour is recorded.

Branches of the tree with the fewest number of colour occurrences are merged together
and replaced with a leaf node representing the average colour of all its children.
This process is repeated until the desired number of leaves (colours) remains.

The image is then redrawn with these new colour averages.
"""

import sys

from PIL import Image

from BinaryHeap import BinaryHeapOT


class OctTree:
    """The outer OctTree data type, which holds all the tree's inner nodes.
    Each level of the tree represents a single slice through each dimension (x, y, z)
    of a colour cube evenly divided into 8 pieces.

    Each leaf node represents a single colour of the image to be reduced.

    The attribute "max_level" is set to 5 to limit the total depth of the tree in
    order to ignore the two least significant bits of colour information. This
    keeps the overall size of the tree much smaller without compromising on
    image quality.
    """
    def __init__(self):
        self.root = None
        self.max_level = 3
        self.num_leaves = 0
        self.all_leaves = []
        self.heap = BinaryHeapOT()

    def insert(self, r, g, b):
        """Add a new OTNode to the tree."""
        if not self.root:
            self.root = self.OTNode(outer=self)
        self.root.insert(r, g, b, 0, self)

    def find(self, r, g, b):
        """Find a node of a colour by its RGB values."""
        if self.root:
            return self.root.find(r, g, b, 0)

    def reduce(self, max_cubes):
        """Calls the inner class's merge function of a OTNode until the number
        of leaves is less than the desired max size.

        The int provided to this function dictates how many colours will be present
        in the the final image.
        """
        while len(self.all_leaves) > max_cubes:
            self.heap.heapify(self.all_leaves)
            smallest = self.find_min_cube()
            smallest.parent.merge()
            self.all_leaves.append(smallest.parent)
            self.num_leaves += 1

    def find_min_cube(self):
        """Return the node with the fewest number of pixels of that colour."""
        return self.heap.delete()

    class OTNode:
        """A single node of the OCTree, initialised with 8 children.

        Each node represents a slice of the colour cube at a particular level/depth.
        On the first level a node represents 1/8 of the cube, whereas a node on the
        deepest level representing 1/16,777,216 of the cube / a single RGB colour.
        """
        def __init__(self, parent=None, level=0, outer=None):
            self.red = 0
            self.green = 0
            self.blue = 0
            self.count = 0
            self.parent = parent
            self.level = level
            self.oTree = outer
            self.children = [None] * 8

        def compute_index(self, r, g, b, level):
            """Combine bits from each of the red, green and blue colour components
            with the current level on the tree to return an index between 0-7.
            """
            shift = 8 - level
            rc = r >> shift - 2 & 0x4
            gc = g >> shift - 1 & 0x2
            bc = b >> shift & 0x1
            return rc | gc | bc

        def insert(self, r, g, b, level, outer):
            """Traverse the tree/subtrees, creates nodes as needed until "max level"
            is reached. The data is then stored in each node along the path.
            """
            if level < self.oTree.max_level:
                idx = self.compute_index(r, g, b, level)
                if self.children[idx] is None:
                    self.children[idx] = outer.OTNode(
                        parent=self,
                        level=level + 1,
                        outer=outer
                    )
                self.children[idx].insert(r, g, b, level + 1, outer)
            else:
                if self.count == 0:
                    self.oTree.num_leaves += 1
                    self.oTree.all_leaves.append(self)
                # Add the colour components to any existing components and increment
                # the reference counter. This allows the average of any colour below the
                # current node in the colour cube to be calculated.
                self.red += r
                self.green += g
                self.blue += b
                self.count += 1

        def find(self, r, g, b, level):
            """Traverse the tree in search of a node matching the RGB value provided.
            Return the (r, g, b) tuple value to be used to represent the provided RBG value.
            """
            if level < self.oTree.max_level:
                idx = self.compute_index(r, g, b, level)
                if self.children[idx]:
                    return self.children[idx].find(r, g, b, level + 1)
                elif self.count > 0:
                    return (
                        self.red // self.count,
                        self.green // self.count,
                        self.blue // self.count
                    )
                else:
                    print("No leaf node to represent this colour.")
            else:
                return (
                    self.red // self.count,
                    self.green // self.count,
                    self.blue // self.count
                )

        def merge(self):
            """Called on a parent node to subsume all of its children and become a
            leaf node itself. When we merge a group of siblings we are taking a
            weighted average of the colours represented by each of those siblings.
            The resulting colour value is a good representation of those children.
            """
            for i in self.children:
                if i:
                    if i.count > 0:
                        self.oTree.all_leaves.remove(i)
                        self.oTree.num_leaves -= 1
                    else:
                        print("Recursively Merging non-leaf...")
                        i.merge()
                    self.count += i.count
                    self.red += i.red
                    self.green += i.green
                    self.blue += i.blue
            for i in range(8):
                self.children[i] = None

        def __lt__(self, val):
            self.count <= val.count and self.level >= val.level

        def __gt__(self, val):
            self.count >= val.count and self.level <= val.level

def build_and_display(filename):
    """Read, quantize and display an image."""
    im: Image = Image.open(filename)
    w, h = im.size
    ot = OctTree()

    for row in range(0, h):
        for col in range(0, w):
            r, g, b = im.getpixel((col, row))
            ot.insert(r, g, b)

    print(ot.heap)
    ot.reduce(8)
    print(ot.heap)

    # while not ot.heap.is_empty():
    #     item = ot.heap.delete()
    #     print(f"{item.count} {item.level}")

    for row in range(0, h):
        for col in range(0, w):
            r, g, b = im.getpixel((col, row))
            nr, ng, nb = ot.find(r, g, b)
            im.putpixel((col, row), (nr, ng, nb))

    im.show()


build_and_display("pp.jpg")
