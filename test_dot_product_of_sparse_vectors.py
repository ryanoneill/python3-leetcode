from dot_product_of_two_sparse_vectors import SparseVector

def test_ex1():
    nums1 = [1,0,0,2,3]
    nums2 = [0,3,0,4,0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    result = v1.dotProduct(v2)
    assert result == 8

def test_ex2():
    nums1 = [0,1,0,0,0]
    nums2 = [0,0,0,0,2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    result = v1.dotProduct(v2)
    assert result == 0
