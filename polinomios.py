class Polinomio:

    def __init__(self, coeficientes = []):
        self.coeficientes = coeficientes

    def __str__(self):
        """
        Representacion en formado de: a_0+a_1*x+a_2*x^2+..+a_n*x^n
        """
        poli= []
        i=0
        for c in self.coeficientes:
            poli.append("({0})*x^{1}".format(c,i))
            i = i + 1
        return('+'.join(poli)+'=0')
    
    def coefi(self):
        return(self.coeficientes)

    def eliminar_termino(self,termino):
        for i in range(len(self.coeficientes)):
            if self.coeficientes[i] == termino:
                self.coeficientes.pop(i)
                break
        return("Termino eliminado satisfactoriamente")

    def encontrar(self,termino):
        bandera = 0
        for i in range(len(self.coeficientes)):
            if self.coeficientes[i] == termino:
                bandera = 1
                break
        return("Termino encontrado satisfactoriamente" if bandera == 1 else "Termino no encontrado")


    def restar(self,p2):
        n = len(p2.coefi())
        m = len(self.coeficientes)
        p3 = []
        if n>m:
            for i in range(m):
                p3.append(self.coeficientes[i]-p2.coefi()[i])
            for i in p2.coefi()[-(n-m):]:
                p3.append(-i)
        elif m>n:
            for i in range(n):
                p3.append(self.coeficientes[i]-p2.coefi()[i])
            for i in self.coeficientes[-(m-n):]:
                p3.append(i)
        else:
            for i in range(n):
                p3.append(self.coeficientes[i]-p2.coefi()[i])
        self.coeficientes = p3
        return("Resta realizada correctamene")
             
        



    def dividir(self,termino):

        if termino != 0:
            for i in range(len(self.coeficientes)):
                self.coeficientes[i] = self.coeficientes[i]/termino
            return("Resta realizada correctamene")
        else:
            return("No se puede dividir entre 0")
              



poli1 = Polinomio([1,2,3,4,5,6,7,8,9])
poli2 = Polinomio([1,1,1,1,1,1,1,100,1,1,-5,35,35])
print(poli1)
print(poli1.coefi())
print(poli1.encontrar(5))
print(poli1.restar(poli2))
print(poli1.dividir(4))
print(poli1)
