import itertools

def exp_product(exp1,exp2):
    if not exp1:
        return exp2
    elif not exp2:
        return exp1
    else:
        res=itertools.product(exp1,exp2) 
       
        return set( [''.join(exp) for exp in res] ) 

        
        

def exp_to_the_nth(exp,n):
    if n: 
        res_exp=exp 
        for i in range(1,n): 
            res_exp=exp_product(res_exp,exp)
        return res_exp
    else:
        return set()
    

def integer_input(no_negatives=False):
    while True:
        try: 
            n = int(input("La expresión es L(L+DL)^n, ingrese el valor de n..."))
            if no_negatives:
                assert n>=0 
            return n
        except ValueError:
            print("Inserte un número...")
        except AssertionError:
            print("Inserte un número mayor o igual a 0...")
        

exp1=set( ["L"] ) 
exp2=set( ["L","DL"] ) 

n=integer_input(no_negatives=True)

result=exp_product( exp1 , exp_to_the_nth(exp2,n) )
                        
print(result)
