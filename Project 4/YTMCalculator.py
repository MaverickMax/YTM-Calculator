print('Please input corresponding values')
fv = float(input('face value:'))
pv = float(input('present value:'))
c = float(input('coupon rate:'))
t = float(input('years:'))
p = float(input('payments per year:'))

truet = t*p
coup = ((c/100)*fv)/p

print(fv,pv,c,t,p,coup,truet)

ytm = ((coup+((fv-pv))/truet)/((fv+pv)/2)*p)*100

print(ytm,)
input('press Enter to close')
