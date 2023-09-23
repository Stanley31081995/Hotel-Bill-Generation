#Hotel Bill Generation

n=input('Enter the name: ')
n1=int(input('Enter the contact no: '))

vada=7
idly=8
dosa=10

no_of_vada=int(input('How many vada: '))
no_of_idli=int(input('How many idly: '))
no_of_dosa=int(input('How many dosa: '))

Hotelname='Kirubha Bhavan'
Bill=(vada*no_of_vada) + (idly*no_of_idli) + (dosa*no_of_dosa)
print(Bill)
