from .basket import Basket              # we called basket class , entire session

def basket(request):
    return {'basket': Basket(request)}