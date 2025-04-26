from image_smoother import Solution

def test_ex1():
    img = [[1,1,1],[1,0,1],[1,1,1]]
    solution = Solution()
    result = solution.imageSmoother(img)
    assert result == [[0,0,0],[0,0,0],[0,0,0]]

def test_ex2():
    img = [[100,200,100],[200,50,200],[100,200,100]]
    solution = Solution()
    result = solution.imageSmoother(img)
    assert result == [[137,141,137],[141,138,141],[137,141,137]]
