from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import unittest
import operator


def build_Parse_Tree(fpexp):
    fplist = split_expression(fpexp)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def split_expression(a_string):
    final = [i for i in a_string if i != ' ']
    final_rng = len(final) - 1
    i = 0
    while i < final_rng:
        if final[i] in '0123456789':
            next_idx = i + 1
            while final[next_idx] in '0123456789' and next_idx < final_rng:
                final[i] += final[next_idx]
                final.pop(next_idx)
                final_rng = final_rng - 1
        i += 1
    return final


def evaluate(parse_Tree):
    leftC = parse_Tree.getLeftChild()
    rightC = parse_Tree.getRightChild()
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    if leftC and rightC:
        fn = operators[parse_Tree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parse_Tree.getRootVal()


class TestParseTree(unittest.TestCase):  # Testing binary searching with no slicing
    def setUp(self) -> None:
        pass

    def test_split(self):
        self.assertEqual(split_expression("( (100 + 5) *3 )"),
                         ['(', '(', '100', '+', '5', ')', '*', '3', ')'])
        self.assertEqual(split_expression("((10+5)*300)"),
                         ['(', '(', '10', '+', '5', ')', '*', '300', ')'])


def main():
    pt = build_Parse_Tree("( (10 + 5) *3 )")
    pt.postorder()
    print(split_expression("( (100 + 5) *3 )"))


if __name__ == '__main__':
    main()