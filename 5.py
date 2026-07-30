class Node:
    def _init_(self,coeff,power):
        self.coeff = coeff
        self.power = power
        self.next = None
class polynomial:
    def _init_(self):
        self.head = None
    def insert(self,coeff,power):
        new = Node(coeff,power)
        if self.head is None:
            self.head =new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def add(self,p2):
        p = self.head
        q = p2.head
        result = polynomial()
        while p and q :
            if p.power == q.power:
                result.insert(p.coeff+q.coeff,p.power)
                p = p.next
                q = q.next
            elif p.power < q.power:
                result.insert(p.coeff,p.power)
                p = p.next
            else:
                result.insert(q.coeff,q.power)
                q = q.next
        while p:
            result.insert(p.coeff,p.power)
            p = p.next
        while q:
            result.insert(q.coeff,q.power)
            q = q.next
        return result
        def display(self):
            temp = self.head
            while temp:
                print(f"{temp.coeff}X^{temp.power}",end=" ")
                if temp.next:
                    print("+",end = " ")
                temp = temp.next
            print()

        p1 = polynomial()
        p2 = polynomial()
        n1 = int(input("Enter number of terms in polynomial:"))
        for i in range(n1):
            c = int(input("Enter coefficient:"))
            p = int(input("Enter power:"))
            p1.insert(c,p)
        n2 = int(input("Enter number of terms in polynomial 2:"))

        for i in range(n2):
            c = int(input("Enter coefficient:"))
            p = int(input("Enter power:"))
            p2.insert(c,p)
        print("\n Polynomial 1:")
        p1.display()
        print("Polynomial 2:")
        p2.display()
        result = p1.add(p2)
        print("Sum of Polynomials:")
        result.display()
       
