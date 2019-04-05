class A:
     def feat1(self):
         print("feat1 working")

     def feat2(self):
         print("feat2 working")

class B(A):                       #single inheritance
    def feat3(self):
        print("feat3 working")

    def feat4(self):
        print("feat4 working")

class C(B):                        #multilevel inheritance
    def feat5(self):
        print("feat5 working")

class D:
    def feat6(self):
        print("feat6 working")

class E(A,D):                        #multiple inheritance
    def feat7(self):
        print("feat7 working")

b1=B()
b1.feat1()
c1=C()
c1.feat2()
e1=E()
e1.feat1()