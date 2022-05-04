import pytest
@pytest.fixture(scope="class",autouse=True,params=[1,2,3])
def before(request):
    print("before %d" % request.param)
    return request.param

def test_022(before):
    print("test_022%d "% before)
def test_0333():
    print("test_0333")



class Test2:
    def test_5(self,before):
        print("5")
        print(before)

    def test_6(self):
        print("test_9")


if __name__ == "__main__":
    pytest.main(['twoo.py'])


