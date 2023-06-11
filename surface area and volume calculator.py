opt=input("Enter 1 to select sphere\nEnter 2 to select cylinder\nEnter 3 to select cone\nEnter 4 to collect rectangular prism\nEnter 5 to collect Triangle prism\n")
def sphere(r,pi=3.14):
    print("Surface area of sphere=",4*pi*r**2)
    print("Volume of sphere=",1.333*pi*r**3)

def cylinder(r,h,pi=3.14):
    print("Surface area of cylinder=",(2*pi*r**2)+2*pi*r*h)
    print("Volume of cylinder=",h*pi*r**2)
def cone(r,h,s,pi=3.14):
    print("Surface area of cone=",(pi*r**2)+pi*r*s)
    print("Volume of cone=",0.333*h*pi*r**2)
def rect_prsm(h,w,l):
    print("Surface area of rectangular prism=",2(lw+lh+wh))
    print("Volume of rectangular prism=",l*w*h)
def tri_prsm(s,h,b,l):
    print("Surface area of rectangular prism=",b*h+2*l*s+l*b)
    print("Volume of rectangular prism=",0.5*b*l*h)
    
    

if(opt==1):
    r=float(input("Enter radius:"))
    sphere(r,pi=3.14)
if(opt==2):
    r=float(input("Enter radius:"))
    h=float(input("Enter height;"))
    cylinder(r,h,pi=3.14)
if(opt==3):
    r=float(input("Enter radius:"))
    h=float(input("Enter height:"))
    s=float(input("Enter slant height:"))
    cone(r,h,s,pi=3.14)
if(opt==4):
    h=float(input("Enter height:"))
    w=float(input("Enter width:"))
    l=float(input("Enter length:"))
    rect_prsm(h,w,l)
if(opt==5):
    s=float(input("Enter slant height:"))
    h=float(input("Enter height:"))
    b=float(input("Enter breath:"))
    l=float(input("Enter length:"))
    tri_prsm(s,h,b,l)


    
